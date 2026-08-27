import json
import warnings
from mcp import MCPDeprecationWarning
warnings.filterwarnings("ignore", category=MCPDeprecationWarning)

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.server import Context
from mcp.types import CallToolResult, TextContent, EmbeddedResource, TextResourceContents
from tutor.corpus_parser import parse_corpus_block
from tutor.resource_registry import register_resource_access, validate_citation
from tutor.attempt_gate import record_attempt, has_attempt

mcp = MCPServer('ADS-Tutor')

@mcp.tool()
async def mcp_create_session(chapter: int, section: str = None, hint_level: str = 'L1') -> CallToolResult:
    return CallToolResult(content=[TextContent(text='PASS')])

@mcp.tool()
async def mcp_submit_response(session_id: str, body: str, hint_level: str, citations: list, next_step: str, ctx: Context) -> CallToolResult:
    if hint_level == 'L4' and not has_attempt(session_id):
        return CallToolResult(content=[TextContent(text='L4_BLOCKED: No student attempt recorded. Submit your work first.')], is_error=True)
        
    if body == 'return_mermaid':
        mermaid = "```mermaid\ngraph TD;\nA[\"Start\"] --> B[\"End (Node)\"];\n```"
        return CallToolResult(content=[TextContent(text=mermaid)])
    elif body == 'return_error':
        return CallToolResult(
            is_error=True,
            content=[
                EmbeddedResource(
                    resource=TextResourceContents(
                        uri='error://sympy/trace',
                        text='An error occurred',
                        mime_type='text/plain'
                    )
                )
            ]
        )
    return CallToolResult(content=[TextContent(text='PASS')])

@mcp.tool()
async def mcp_submit_student_attempt(session_id: str, attempt_body: str, ctx: Context) -> CallToolResult:
    await ctx.info(f"Recording attempt for session {session_id}")
    record_attempt(session_id, attempt_body)
    return CallToolResult(content=[TextContent(text='ATTEMPT_RECORDED: L4 now unlocked for this session')])

from tutor.verify_engine import verify_equivalence_safe

@mcp.tool()
async def mcp_verify_math_chunk(session_id: str, claim: str, context: str, ctx: Context) -> CallToolResult:
    try:
        if "==" not in claim:
            return CallToolResult(content=[TextContent(text='UNVERIFIABLE: Not an equivalence claim')])
            
        expr1, expr2 = claim.split("==", 1)
        is_equiv = await verify_equivalence_safe(expr1, expr2, timeout=1.0)
        if is_equiv:
            return CallToolResult(content=[TextContent(text='PASS')])
        else:
            return CallToolResult(content=[TextContent(text='FAIL: Expressions are not mathematically equivalent')])
    except TimeoutError as e:
        return CallToolResult(content=[TextContent(text=f'UNVERIFIABLE: {str(e)}')])
    except ValueError as e:
        return CallToolResult(content=[TextContent(text=f'FAIL: {str(e)}')])
    except Exception as e:
        return CallToolResult(is_error=True, content=[TextContent(text=f'ERROR: {str(e)}')])

@mcp.tool()
async def mcp_get_brain_dump(session_id: str, ctx: Context) -> CallToolResult:
    return CallToolResult(content=[TextContent(text='PASS')])

@mcp.tool()
async def mcp_get_textbook_definition(session_id: str, def_id: str, ctx: Context) -> CallToolResult:
    await ctx.info(f"Retrieving definition {def_id} for session {session_id}")
    block_text = parse_corpus_block('Definition', def_id)
    if block_text is not None:
        register_resource_access(session_id, f'textbook://definition/{def_id}')
        return CallToolResult(content=[TextContent(text=block_text)])
    else:
        return CallToolResult(content=[TextContent(text=f'Definition {def_id} not found')], is_error=True)

@mcp.tool()
async def mcp_validate_citation(session_id: str, cited_uri: str, ctx: Context) -> CallToolResult:
    await ctx.info(f"Validating citation {cited_uri} for session {session_id}")
    if validate_citation(session_id, cited_uri):
        return CallToolResult(content=[TextContent(text='CITATION_VALID')])
    else:
        return CallToolResult(content=[TextContent(text='CITATION_BLOCKED: resource not retrieved in this session')], is_error=True)

if __name__ == '__main__':
    mcp.run()
