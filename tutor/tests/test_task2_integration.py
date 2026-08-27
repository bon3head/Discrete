import pytest
from mcp.client.client import Client
from tutor.mcp_server import mcp
from tutor.resource_registry import _sessions

@pytest.fixture(autouse=True)
def clear_sessions():
    _sessions.clear()

@pytest.fixture
def client():
    return Client(mcp)

@pytest.mark.asyncio
async def test_retrieval_to_citation_pass(client):
    async with client:
        res1 = await client.call_tool("mcp_get_textbook_definition", arguments={"session_id": "s1", "def_id": "1.1.3"})
        assert not res1.is_error
        
        res2 = await client.call_tool("mcp_validate_citation", arguments={"session_id": "s1", "cited_uri": "textbook://definition/1.1.3"})
        assert not res2.is_error

@pytest.mark.asyncio
async def test_citation_without_retrieval_block(client):
    async with client:
        res = await client.call_tool("mcp_validate_citation", arguments={"session_id": "s2", "cited_uri": "textbook://definition/1.1.3"})
        assert res.is_error
        assert "CITATION_BLOCKED" in res.content[0].text

@pytest.mark.asyncio
async def test_cross_session_isolation(client):
    async with client:
        res1 = await client.call_tool("mcp_get_textbook_definition", arguments={"session_id": "s3", "def_id": "1.1.3"})
        assert not res1.is_error
        
        res2 = await client.call_tool("mcp_validate_citation", arguments={"session_id": "s4", "cited_uri": "textbook://definition/1.1.3"})
        assert res2.is_error
        assert "CITATION_BLOCKED" in res2.content[0].text
