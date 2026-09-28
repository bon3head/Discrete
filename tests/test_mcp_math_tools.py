import pytest
from mcp import Client
from tutor.mcp_server import mcp
import tutor.mcp_math_tools  # to register tools

async def test_mcp_verify_equivalence_pass():
    async with Client(mcp, raise_exceptions=True) as client:
        result = await client.call_tool("mcp_verify_equivalence", {"expr1": "x + x", "expr2": "2*x"})
        assert not result.is_error
        assert result.content[0].text == "PASS"

async def test_mcp_verify_equivalence_fail():
    async with Client(mcp, raise_exceptions=True) as client:
        result = await client.call_tool("mcp_verify_equivalence", {"expr1": "x + 1", "expr2": "x"})
        assert not result.is_error
        assert "FAIL" in result.content[0].text

async def test_mcp_verify_proof():
    async with Client(mcp, raise_exceptions=True) as client:
        # Since it's flat arguments, maybe steps is a list of dicts?
        steps = [{"step_num": 1, "expr1": "x+x", "expr2": "2*x", "justification": "algebra"}]
        result = await client.call_tool("mcp_verify_proof", {"steps": steps})
        assert not result.is_error
        assert result.content[0].text == "PASS"

async def test_mcp_verify_equivalence_timeout_fallback():
    """RED TEAM MUTATION: Mock the engine to throw a TimeoutError and prove it maps to UNVERIFIABLE."""
    from unittest.mock import patch, AsyncMock
    
    mock_func = AsyncMock(side_effect=TimeoutError("SymPy execution exceeded timeout"))
        
    with patch("tutor.mcp_math_tools.verify_equivalence_safe", new=mock_func):
        async with Client(mcp, raise_exceptions=True) as client:
            result = await client.call_tool("mcp_verify_equivalence", {"expr1": "x", "expr2": "y"})
            assert not result.is_error # The protocol succeeds
            assert "UNVERIFIABLE" in result.content[0].text
