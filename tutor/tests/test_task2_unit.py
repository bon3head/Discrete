import pytest
from tutor.resource_registry import (
    register_resource_access,
    get_registered_resources,
    validate_citation,
    _sessions
)

def setup_function():
    _sessions.clear()

def test_register_and_get():
    register_resource_access('s1', 'textbook://definition/1.1.3')
    assert get_registered_resources('s1') == {'textbook://definition/1.1.3'}
    assert get_registered_resources('s2') == set()

def test_validate_citation():
    register_resource_access('s1', 'textbook://definition/1.1.3')
    assert validate_citation('s1', 'textbook://definition/1.1.3') is True
    assert validate_citation('s1', 'textbook://definition/1.1.4') is False
    assert validate_citation('s2', 'textbook://definition/1.1.3') is False
