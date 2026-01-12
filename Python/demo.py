import unicodedata
import re

def normalizeQuery(input: str) -> str:
    """
    將輸入字串進行標準化：
    - 移除前後的所有 Unicode 空白字元
    - 將所有連續空白（Unicode 空白）合併為一個半形空白
    - 保留語言區分（不做大小寫轉換、不做 Unicode 正規化）
    - O(n) 時間複雜度
    """
    # 使用正則表達式處理所有 Unicode 空白
    # \s 包含所有 Unicode 空白
    # 先去除前後空白
    trimmed = re.sub(r'^\s+|\s+$', '', input)
    # 再將中間所有連續空白合併為一個半形空白
    normalized = re.sub(r'\s+', ' ', trimmed)
    return normalized