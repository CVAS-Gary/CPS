import re
import unicodedata
def normalize_query(input: str) -> str:
    # 初始版本，待 Copilot 生成
    if not isinstance(input, str):
        raise ValueError("Input must be a string")
    # 使用正則表達式替換多重空白為單一空白，並去除前後空白
    normalized_str = re.sub(r'\s+', ' ', input).strip()
    # 特殊處理土耳其語的大寫 İ → i
    normalized_str = normalized_str.replace("İ", "i")

    # 使用 casefold，比 lower 更強大，能處理更多 Unicode 大小寫
    normalized_str = normalized_str.casefold()

    return normalized_str