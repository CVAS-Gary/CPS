"""
撰寫一個純函式：
- 名稱：deduplicate_and_sort
- 輸入：list of int
- 輸出：排序後去重的 list of int
- 若輸入含非整數，拋出 ValueError("Invalid input")
- 加入清楚的 docstring（說明參數與回傳）
- 通過 flake8/black 格式檢查
- 通過 pytest 測試（test_dedup.py）
強化版本要求：
- 使用明確的輸入驗證（僅允許 int）
- 對 None/空值顯式處理
- 保持循環複雜度低（不做過度巢狀）
- 文件字串（docstring）完整描述例外情況

"""
def deduplicate_and_sort(input_list):
    """
    接收一個整數列表，移除重複並以遞增排序後回傳。
    若列表中包含非整數則拋出 ValueError("Invalid input")。

    參數:
    input_list (list of int): 需要去重並排序的整數列表。

    回傳:
    list of int: 去重並排序後的整數列表。

    拋出:
    ValueError: 如果輸入列表中包含非整數元素。
    """
    if input_list is None:
        raise ValueError("Invalid input: None is not allowed")
    if not all(isinstance(x, int) for x in input_list):
        raise ValueError("Invalid input")
    return sorted(set(input_list))
