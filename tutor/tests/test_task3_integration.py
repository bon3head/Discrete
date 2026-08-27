import pytest
from mcp.client.client import Client
from tutor.mcp_server import mcp
from tutor.attempt_gate import _attempts
from tutor.resource_registry import _sessions

@pytest.fixture(autouse=True)
def clear_state():
    _attempts.clear()
    _sessions.clear()
    yield

@pytest.fixture
def client():
    return Client(mcp)

@pytest.mark.asyncio
async def test_l4_blocked_without_attempt(client):
    async with client:
        result = await client.call_tool("mcp_submit_response", arguments={
            "session_id": "test_session",
            "body": "normal",
            "hint_level": "L4",
            "citations": [],
            "next_step": "none"
        })
        assert result.is_error is True
        assert "L4_BLOCKED" in result.content[0].text

@pytest.mark.asyncio
async def test_l4_unlocked_after_attempt(client):
    async with client:
        await client.call_tool("mcp_submit_student_attempt", arguments={
            "session_id": "test_session",
            "attempt_body": "my work"
        })
        result = await client.call_tool("mcp_submit_response", arguments={
            "session_id": "test_session",
            "body": "normal",
            "hint_level": "L4",
            "citations": [],
            "next_step": "none"
        })
        assert not result.is_error

@pytest.mark.asyncio
async def test_combined_task1_2_3_chain(client):
    async with client:
        await client.call_tool("mcp_get_textbook_definition", arguments={
            "session_id": "test_session",
            "def_id": "1.1.3"
        })
        await client.call_tool("mcp_submit_student_attempt", arguments={
            "session_id": "test_session",
            "attempt_body": "attempt"
        })
        response = await client.call_tool("mcp_submit_response", arguments={
            "session_id": "test_session",
            "body": "normal",
            "hint_level": "L4",
            "citations": [],
            "next_step": "none"
        })
        assert not response.is_error
        
        valid = await client.call_tool("mcp_validate_citation", arguments={
            "session_id": "test_session",
            "cited_uri": "textbook://definition/1.1.3"
        })
        assert not valid.is_error
        assert valid.content[0].text == 'CITATION_VALID'
