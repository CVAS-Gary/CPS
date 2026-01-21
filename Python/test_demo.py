import pytest
from demo import normalizeQuery


def test_normalizeQuery_empty():
    """Test with empty string"""
    assert normalizeQuery("") == ""


def test_normalizeQuery_only_spaces():
    """Test with only whitespace"""
    assert normalizeQuery("     ") == ""
    assert normalizeQuery("\t\n\r") == ""


def test_normalizeQuery_leading_trailing_spaces():
    """Test trimming leading and trailing spaces"""
    assert normalizeQuery("   hello world   ") == "hello world"
    assert normalizeQuery("\thello\n") == "hello"


def test_normalizeQuery_unicode_whitespace():
    """Test Unicode whitespace characters"""
    assert normalizeQuery("\u2003hello\u3000world\u2002") == "hello world"
    assert normalizeQuery("a\u2003\u3000b") == "a b"


def test_normalizeQuery_mixed_whitespace():
    """Test mixed whitespace types"""
    assert normalizeQuery("a\tb\nc\r\nd") == "a b c d"
    assert normalizeQuery("a \t\n b") == "a b"


def test_normalizeQuery_multiple_consecutive_whitespace():
    """Test collapsing multiple spaces"""
    assert normalizeQuery("a     b    c") == "a b c"
    assert normalizeQuery("a\u2003\u2003b\u3000\u3000c") == "a b c"


def test_normalizeQuery_no_whitespace():
    """Test string without whitespace"""
    assert normalizeQuery("abc") == "abc"
    assert normalizeQuery("hello") == "hello"


def test_normalizeQuery_single_character():
    """Test single character with spaces"""
    assert normalizeQuery(" a ") == "a"


def test_normalizeQuery_preserves_case():
    """Test case preservation"""
    assert normalizeQuery("Hello World") == "Hello World"
    assert normalizeQuery("ABC xyz") == "ABC xyz"


def test_normalizeQuery_language_sensitive():
    """Test language-specific characters are preserved"""
    assert normalizeQuery("İstanbul") == "İstanbul"
    assert normalizeQuery("i I ı İ") == "i I ı İ"


def test_normalizeQuery_fullwidth_characters():
    """Test fullwidth punctuation is preserved"""
    assert normalizeQuery("  a ！ b　") == "a ！ b"
