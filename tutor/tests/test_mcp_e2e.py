import pytest
import subprocess
import json
from mcp.client.client import Client
from mcp.types import CallToolResult, TextContent, EmbeddedResource, TextResourceContents
from tutor.mcp_server import mcp
from tutor.resource_registry import _sessions
from tutor.attempt_gate import _attempts

@pytest.fixture(autouse=True)
def reset_state():
    _sessions.clear()
    _attempts.clear()
    yield
    _sessions.clear()
    _attempts.clear()

@pytest.fixture
def client():
    return Client(mcp)

@pytest.mark.asyncio
async def test_full_tutoring_loop(client):
    session_id = 'e2e_test_session'
    
    async with client:
        # 1. Create session
        res = await client.call_tool('mcp_create_session', arguments={'chapter': 1, 'section': '1.1', 'hint_level': 'L1'})
        assert not res.is_error
        
        # 2. L1 Hint (no attempt required)
        res = await client.call_tool('mcp_submit_response', arguments={
            'session_id': session_id,
            'body': 'normal',
            'hint_level': 'L1',
            'citations': [],
            'next_step': ''
        })
        assert not res.is_error
        assert res.content[0].text == 'PASS'
        
        # 3. L4 blocked (no attempt yet)
        res = await client.call_tool('mcp_submit_response', arguments={
            'session_id': session_id,
            'body': 'normal',
            'hint_level': 'L4',
            'citations': [],
            'next_step': ''
        })
        assert res.is_error
        assert 'L4_BLOCKED' in res.content[0].text
        
        # 4. Retrieve textbook definition
        res = await client.call_tool('mcp_get_textbook_definition', arguments={
            'session_id': session_id,
            'def_id': '1.1.3'
        })
        assert not res.is_error
        
        # 5. Submit student attempt
        res = await client.call_tool('mcp_submit_student_attempt', arguments={
            'session_id': session_id,
            'attempt_body': 'A is subset of B means every element of A is in B'
        })
        assert not res.is_error
        assert 'ATTEMPT_RECORDED' in res.content[0].text
        
        # 6. L4 unlocked
        res = await client.call_tool('mcp_submit_response', arguments={
            'session_id': session_id,
            'body': 'normal',
            'hint_level': 'L4',
            'citations': [],
            'next_step': ''
        })
        assert not res.is_error
        
        # 7. Citation validation PASS
        res = await client.call_tool('mcp_validate_citation', arguments={
            'session_id': session_id,
            'cited_uri': 'textbook://definition/1.1.3'
        })
        assert not res.is_error
        
        # 8. Citation validation BLOCK
        res = await client.call_tool('mcp_validate_citation', arguments={
            'session_id': session_id,
            'cited_uri': 'textbook://definition/9.9.9'
        })
        assert res.is_error
        assert 'CITATION_BLOCKED' in res.content[0].text
        
        # 9. Mermaid shape check
        res = await client.call_tool('mcp_submit_response', arguments={
            'session_id': session_id,
            'body': 'return_mermaid',
            'hint_level': 'L1',
            'citations': [],
            'next_step': ''
        })
        assert not res.is_error
        assert '```mermaid' in res.content[0].text
        assert '["' in res.content[0].text
        
        # 10. Error trace shape check
        res = await client.call_tool('mcp_submit_response', arguments={
            'session_id': session_id,
            'body': 'return_error',
            'hint_level': 'L1',
            'citations': [],
            'next_step': ''
        })
        assert res.is_error
        assert isinstance(res.content[0], EmbeddedResource)
        assert res.content[0].resource.uri == 'error://sympy/trace'

def test_ide_hook_defense():
    # Run block_bash_tutoring.sh
    bad_cmd = "echo '{\"toolCall\":{\"args\":{\"CommandLine\":\"python3 tutor/cli.py\"}}}' | /var/home/justin/PROJECTS/New-Paltz/Fall2026/Discrete/bin/block_bash_tutoring.sh"
    result = subprocess.run(bad_cmd, shell=True, capture_output=True, text=True)
    assert result.returncode == 0
    assert 'deny' in result.stdout.lower() or '"deny"' in result.stdout
    
    good_cmd = "echo '{\"toolCall\":{\"args\":{\"CommandLine\":\"ls\"}}}' | /var/home/justin/PROJECTS/New-Paltz/Fall2026/Discrete/bin/block_bash_tutoring.sh"
    result2 = subprocess.run(good_cmd, shell=True, capture_output=True, text=True)
    assert result2.returncode == 0
    assert 'allow' in result2.stdout.lower() or '"allow"' in result2.stdout

