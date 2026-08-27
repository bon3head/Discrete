import pytest
from tutor.attempt_gate import record_attempt, has_attempt, _attempts

@pytest.fixture(autouse=True)
def clear_attempts():
    _attempts.clear()
    yield

def test_no_attempt_blocks_l4():
    assert has_attempt('x') is False

def test_attempt_unlocks_l4():
    record_attempt('x', 'some work')
    assert has_attempt('x') is True

def test_cross_session_attempt_isolation():
    record_attempt('s5', 'work')
    assert has_attempt('s6') is False
