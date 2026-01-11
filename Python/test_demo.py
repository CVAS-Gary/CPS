from demo import normalizeQuery

# pytest 測試
def test_normalizeQuery_empty():
    assert normalizeQuery("") == ""

def test_normalizeQuery_only_spaces():
    assert normalizeQuery("     ") == ""

def test_normalizeQuery_leading_trailing_spaces():
    assert normalizeQuery("   hello world   ") == "hello world"

def test_normalizeQuery_unicode_whitespace():
    assert normalizeQuery("\u2003hello\u3000world\u2002") == "hello world"
    assert normalizeQuery("a\u2003\u3000b") == "a b"

def test_normalizeQuery_mixed_whitespace():
    assert normalizeQuery("a\tb\nc\r\nd") == "a b c d"
    assert normalizeQuery("a \t\n b") == "a b"

def test_normalizeQuery_fullwidth_punctuation():
    assert normalizeQuery("  a ！ b　") == "a ！ b"

def test_normalizeQuery_language_sensitive():
    assert normalizeQuery("İstanbul is not istanbul") == "İstanbul is not istanbul"
    assert normalizeQuery("i I ı İ") == "i I ı İ"

def test_normalizeQuery_no_whitespace():
    assert normalizeQuery("abc") == "abc"

def test_normalizeQuery_single_character():
    assert normalizeQuery(" a ") == "a"

def test_normalizeQuery_multiple_consecutive_whitespace():
    assert normalizeQuery("a     b    c") == "a b c"
    assert normalizeQuery("a\u2003\u2003b\u3000\u3000c") == "a b c"