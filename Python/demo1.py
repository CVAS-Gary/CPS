# 請撰寫一個 normalize_query(input: str) → str 函式，限制：必須是純函式、O(n)、處理 Unicode 空白，驗收：pytest 測試涵蓋空字串、多重空白、特殊字元。
def normalize_query(input_str):
    """
    接收一個字串，移除多餘的空白字元並標準化 Unicode 空白，回傳處理後的字串。

    參數:
    input_str (str): 需要標準化的輸入字串。

    回傳:
    str: 標準化後的字串，移除多重空白並處理 Unicode 空白。

    拋出:
    ValueError: 如果輸入不是字串類型。
    """
    if not isinstance(input_str, str):
        raise ValueError("Invalid input: input must be a string")

    import re
    # 使用正則表達式替換多重空白為單一空白，並去除前後空白
    normalized_str = re.sub(r'\s+', ' ', input_str).strip()
    return normalized_str