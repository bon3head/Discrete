import pytest
from tutor.corpus_parser import parse_corpus_block, get_section_text

def test_parse_corpus_block_positive_match():
    result = parse_corpus_block('Definition', '1.1.3', corpus_root='corpus/active')
    assert result is not None
    assert len(result) > 0
    assert 'Definition 1.1.3' in result

def test_parse_corpus_block_isolation():
    result = parse_corpus_block('Definition', '1.1.3', corpus_root='corpus/active')
    assert result is not None
    # Assuming 1.1.4 or 1.1.5 or something else is in the same file
    assert '1.1.4' not in result
    assert '1.1.5' not in result
    # We want to be absolutely sure it doesn't leak into the next section
    # Let's ensure there are no other block headers in the extracted block
    assert result.count('**Definition') == 1
    assert result.count('**Example') == 0

def test_parse_corpus_block_missing():
    result = parse_corpus_block('Definition', '99.99.99', corpus_root='corpus/active')
    assert result is None

def test_parse_corpus_block_exercise():
    result = parse_corpus_block('Exercise', '1', corpus_root='corpus/active')
    assert result is None or isinstance(result, str)
    if result is not None:
        assert 'Exercise 1' in result
        
def test_get_section_text():
    result = get_section_text('ch01', corpus_root='corpus/active')
    assert result is not None
    assert len(result) > 0
    assert 'Section 1.1' in result
