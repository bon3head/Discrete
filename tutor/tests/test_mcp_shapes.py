import pytest
import asyncio
from unittest.mock import patch
from mcp.client.client import Client
from mcp.types import CallToolResult, TextContent, EmbeddedResource, TextResourceContents
from tutor.mcp_server import mcp

@pytest.fixture
def client():
    return Client(mcp)

@pytest.mark.asyncio
async def test_mermaid_shape(client):
    async with client:
        result = await client.call_tool('mcp_submit_response', arguments={
            'session_id': '123',
            'body': 'return_mermaid',
            'hint_level': 'L1',
            'citations': [],
            'next_step': ''
        })
        assert isinstance(result.content[0], TextContent)
        assert "```mermaid" in result.content[0].text
        assert '["Start"]' in result.content[0].text
        assert '["End (Node)"]' in result.content[0].text

@pytest.mark.asyncio
async def test_error_shape(client):
    async with client:
        result = await client.call_tool('mcp_submit_response', arguments={
            'session_id': '123',
            'body': 'return_error',
            'hint_level': 'L1',
            'citations': [],
            'next_step': ''
        })
        assert result.is_error is True
        assert isinstance(result.content[0], EmbeddedResource)
        assert isinstance(result.content[0].resource, TextResourceContents)
        assert result.content[0].resource.uri == 'error://sympy/trace'

@pytest.mark.asyncio
@patch('tutor.verify_engine.sympy.simplify')
async def test_timeout_mutation(mock_simplify, client):
    # Force a hang that exceeds the timeout
    def slow_simplify(*args, **kwargs):
        import time
        time.sleep(10)
        return 0
    mock_simplify.side_effect = slow_simplify
    
    async with client:
        result = await client.call_tool('mcp_verify_math_chunk', arguments={
            'session_id': '123',
            'claim': 'x == x',
            'context': ''
        })
        # Should catch timeout and return UNVERIFIABLE
        assert not result.is_error
        assert 'UNVERIFIABLE' in result.content[0].text
        assert 'TimeoutError' in result.content[0].text or 'timeout' in result.content[0].text.lower()

@pytest.mark.asyncio
async def test_ace_injection(client):
    async with client:
        result = await client.call_tool('mcp_verify_math_chunk', arguments={
            'session_id': '123',
            'claim': '().__class__.__base__.__subclasses__()[0] == 0',
            'context': ''
        })
        # The verify engine should block this or return an error gracefully
        assert 'FAIL: Parse Error' in result.content[0].text or result.is_error

