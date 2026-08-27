import pytest
from mcp import Client
from tutor.mcp_server import mcp
import tutor.mcp_math_tools  # to register tools

@pytest.mark.asyncio
async def test_mcp_verify_equivalence_pass():
    async with Client(mcp, raise_exceptions=True) as client:
        result = await client.call_tool("mcp_verify_equivalence", {"expr1": "x + x", "expr2": "2*x"})
        assert not result.is_error
        assert result.content[0].text == "PASS"

@pytest.mark.asyncio
async def test_mcp_verify_equivalence_fail():
    async with Client(mcp, raise_exceptions=True) as client:
        result = await client.call_tool("mcp_verify_equivalence", {"expr1": "x + 1", "expr2": "x"})
        assert not result.is_error
        assert "FAIL" in result.content[0].text

@pytest.mark.asyncio
async def test_mcp_verify_proof():
    async with Client(mcp, raise_exceptions=True) as client:
        # Since it's flat arguments, maybe steps is a list of dicts?
        steps = [{"step_num": 1, "expr1": "x+x", "expr2": "2*x", "justification": "algebra"}]
        result = await client.call_tool("mcp_verify_proof", {"steps": steps})
        assert not result.is_error
        assert result.content[0].text == "PASS"
