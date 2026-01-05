def normalize_query(input: str) -> str:
    # 初始版本，待 Copilot 生成
    if not isinstance(input, str):
        raise ValueError("Input must be a string")
    import re
    # 使用正則表達式替換多重空白為單一空白，並去除前後空白
    normalized_str = re.sub(r'\s+', ' ', input).strip()
    return normalized_str