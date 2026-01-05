from src.normalize_query import normalize_query

def test_empty_string():
    assert normalize_query("") == ""

def test_multiple_spaces_and_tabs():
    assert normalize_query("  hello\t\tworld  ") == "hello world"

def test_unicode_whitespace():
    assert normalize_query("a\u00A0\u2003b") == "a b"

def test_locale_sensitive_case():
    assert normalize_query("İSTANBUL") == "istanbul"

def test_emoji_and_combining_marks():
    assert normalize_query("cafe\u0301 ☕") == "café ☕"