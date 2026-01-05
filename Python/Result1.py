'''
任務：請在 src/normalize_query.py 實作 normalize_query(input: str) → str。
限制：
- 純函式，不依賴外部狀態
- O(n) 時間複雜度
- 處理 Unicode 空白，壓縮成單一空白
- 一般情況轉小寫，但保留土耳其 i
- 保留 emoji 與 combining marks
驗收：tests/test_normalize_query.py 所有測試通過
'''
import unicodedata
import re

def normalize_query(input: str) -> str:
    # Unicode whitespace pattern
    whitespace_re = re.compile(r'\s+', flags=re.UNICODE)
    # Lowercase, but preserve Turkish dotted/dotless i
    def smart_lower(char):
        # Turkish i: U+0130 (İ), U+0069 (i), U+0131 (ı)
        # Only lowercase if not Turkish I (İ, ı)
        if char == '\u0130':  # LATIN CAPITAL LETTER I WITH DOT ABOVE
            return char
        if char == '\u0131':  # LATIN SMALL LETTER DOTLESS I
            return char
        return char.lower()
    # Normalize to NFC to preserve emoji and combining marks
    normalized = unicodedata.normalize('NFC', input)
    lowered = ''.join(smart_lower(c) for c in normalized)
    # Replace all unicode whitespace with single space, strip ends
    compressed = whitespace_re.sub(' ', lowered).strip()
    return compressed