import pytest
import asyncio
from mcp import Client
from tutor.mcp_server import mcp
import tutor.mcp_math_tools
import uuid

@pytest.mark.asyncio
async def test_mcp_concurrency_and_boundaries():
    """
    Stress test the MCP server under concurrent load with various edge cases:
    - Valid math
    - Syntax errors
    - Strings containing double underscores (which the parser safely blocks)
    """
    async with Client(mcp, raise_exceptions=True) as client:
        # Prepare 20 concurrent requests
        tasks = []
        for i in range(20):
            if i % 4 == 0:
                # Valid math
                tasks.append(client.call_tool("mcp_verify_equivalence", {"expr1": f"x + {i}", "expr2": f"{i} + x"}))
            elif i % 4 == 1:
                # Invalid math
                tasks.append(client.call_tool("mcp_verify_equivalence", {"expr1": f"x + {i}", "expr2": f"y"}))
            elif i % 4 == 2:
                # Syntax error
                tasks.append(client.call_tool("mcp_verify_equivalence", {"expr1": f"x + * {i}", "expr2": f"y"}))
            else:
                # Edge case string that must be blocked gracefully (Parse Error)
                tasks.append(client.call_tool("mcp_verify_equivalence", {"expr1": f"__import__('os')", "expr2": "y"}))
                
        results = await asyncio.gather(*tasks)
        
        # Verify no requests crashed the server and all returned CallToolResult
        assert len(results) == 20
        for i, res in enumerate(results):
            if i % 4 == 0:
                assert not res.is_error
                assert "PASS" in res.content[0].text
            elif i % 4 == 1:
                assert not res.is_error
                assert "FAIL" in res.content[0].text
            elif i % 4 == 2 or i % 4 == 3:
                # Syntax errors and blocked strings return ERROR
                assert res.is_error
                assert "ERROR" in res.content[0].text or "Parse Error" in res.content[0].text

@pytest.mark.asyncio
async def test_mcp_attempt_gate_race_condition():
    """
    Test rapid out-of-order state requests to ensure the Attempt Gate 
    correctly blocks L4 walkthroughs under pressure.
    """
    session_id = f"test-session-{uuid.uuid4()}"
    
    async with Client(mcp, raise_exceptions=True) as client:
        # Fire 10 rapid requests for an L4 walkthrough BEFORE submitting an attempt
        tasks = []
        for _ in range(10):
            tasks.append(client.call_tool("mcp_submit_response", {
                "session_id": session_id,
                "body": "Give me the answer",
                "hint_level": "L4",
                "citations": [],
                "next_step": "None"
            }))
            
        results = await asyncio.gather(*tasks)
        
        # All 10 requests should be blocked
        for res in results:
            assert res.is_error
            assert "L4_BLOCKED" in res.content[0].text
            
        # Now submit a valid attempt
        attempt_res = await client.call_tool("mcp_submit_student_attempt", {
            "session_id": session_id,
            "attempt_body": "I tried x + y"
        })
        assert not attempt_res.is_error
        
        # Now an L4 request should succeed
        l4_res = await client.call_tool("mcp_submit_response", {
            "session_id": session_id,
            "body": "Give me the answer",
            "hint_level": "L4",
            "citations": [],
            "next_step": "None"
        })
        assert not l4_res.is_error
        assert "PASS" in l4_res.content[0].text
