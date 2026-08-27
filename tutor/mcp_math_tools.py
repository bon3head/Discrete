from pydantic import BaseModel
from typing import List, Optional
from mcp.types import CallToolResult, TextContent
from tutor.mcp_server import mcp
from tutor.verify_engine import verify_equivalence_safe

class ProofStep(BaseModel):
    step_num: int
    expr1: str
    expr2: str
    justification: str

@mcp.tool()
async def mcp_verify_equivalence(expr1: str, expr2: str) -> CallToolResult:
    try:
        is_equiv = await verify_equivalence_safe(expr1, expr2)
        if is_equiv:
            return CallToolResult(content=[TextContent(type="text", text='PASS')])
        else:
            return CallToolResult(content=[TextContent(type="text", text='FAIL: Expressions are not mathematically equivalent')])
    except Exception as e:
        return CallToolResult(is_error=True, content=[TextContent(type="text", text=f'FAIL: {str(e)}')])

@mcp.tool()
async def mcp_verify_proof(steps: List[ProofStep]) -> CallToolResult:
    try:
        for step in steps:
            is_equiv = await verify_equivalence_safe(step.expr1, step.expr2)
            if not is_equiv:
                return CallToolResult(content=[TextContent(type="text", text=f'FAIL at step {step.step_num}: {step.expr1} != {step.expr2}')])
        return CallToolResult(content=[TextContent(type="text", text='PASS')])
    except Exception as e:
        return CallToolResult(is_error=True, content=[TextContent(type="text", text=f'FAIL: {str(e)}')])
