import pytest
from demo import normalizeQuery


def test_given_empty_string_when_normalize_then_return_empty():
    # Given
    INPUT = ""
    # When
    RESULT = normalizeQuery(INPUT)
    # Then
    assert RESULT == ""


def test_given_only_whitespace_when_normalize_then_return_empty():
    # Given
    INPUT1 = "     "
    INPUT2 = "\t\n\r"
    # When
    RESULT1 = normalizeQuery(INPUT1)
    RESULT2 = normalizeQuery(INPUT2)
    # Then
    assert RESULT1 == ""
    assert RESULT2 == ""


def test_given_leading_trailing_spaces_when_normalize_then_trimmed():
    # Given
    INPUT1 = "   hello world   "
    INPUT2 = "\thello\n"
    # When
    RESULT1 = normalizeQuery(INPUT1)
    RESULT2 = normalizeQuery(INPUT2)
    # Then
    assert RESULT1 == "hello world"
    assert RESULT2 == "hello"


def test_given_unicode_whitespace_when_normalize_then_collapsed():
    # Given
    INPUT1 = "\u2003hello\u3000world\u2002"
    INPUT2 = "a\u2003\u3000b"
    # When
    RESULT1 = normalizeQuery(INPUT1)
    RESULT2 = normalizeQuery(INPUT2)
    # Then
    assert RESULT1 == "hello world"
    assert RESULT2 == "a b"


def test_given_mixed_whitespace_when_normalize_then_collapsed():
    # Given
    INPUT1 = "a\tb\nc\r\nd"
    INPUT2 = "a \t\n b"
    # When
    RESULT1 = normalizeQuery(INPUT1)
    RESULT2 = normalizeQuery(INPUT2)
    # Then
    assert RESULT1 == "a b c d"
    assert RESULT2 == "a b"


def test_given_multiple_consecutive_whitespace_when_normalize_then_collapsed():
    # Given
    INPUT1 = "a     b    c"
    INPUT2 = "a\u2003\u2003b\u3000\u3000c"
    # When
    RESULT1 = normalizeQuery(INPUT1)
    RESULT2 = normalizeQuery(INPUT2)
    # Then
    assert RESULT1 == "a b c"
    assert RESULT2 == "a b c"


def test_given_no_whitespace_when_normalize_then_unchanged():
    # Given
    INPUT1 = "abc"
    INPUT2 = "hello"
    # When
    RESULT1 = normalizeQuery(INPUT1)
    RESULT2 = normalizeQuery(INPUT2)
    # Then
    assert RESULT1 == "abc"
    assert RESULT2 == "hello"


def test_given_single_character_with_spaces_when_normalize_then_trimmed():
    # Given
    INPUT = " a "
    # When
    RESULT = normalizeQuery(INPUT)
    # Then
    assert RESULT == "a"


def test_given_case_sensitive_string_when_normalize_then_case_preserved():
    # Given
    INPUT1 = "Hello World"
    INPUT2 = "ABC xyz"
    # When
    RESULT1 = normalizeQuery(INPUT1)
    RESULT2 = normalizeQuery(INPUT2)
    # Then
    assert RESULT1 == "Hello World"
    assert RESULT2 == "ABC xyz"


def test_given_language_specific_characters_when_normalize_then_preserved():
    # Given
    INPUT1 = "İstanbul"
    INPUT2 = "i I ı İ"
    # When
    RESULT1 = normalizeQuery(INPUT1)
    RESULT2 = normalizeQuery(INPUT2)
    # Then
    assert RESULT1 == "İstanbul"
    assert RESULT2 == "i I ı İ"


def test_given_fullwidth_punctuation_when_normalize_then_preserved():
    # Given
    INPUT = "  a ！ b　"
    # When
    RESULT = normalizeQuery(INPUT)
    # Then
    assert RESULT == "a ！ b"
