"""
Python.demo 的 Docstring
    撰寫一個純函式：
    寫一個函式，接收整數陣列並回傳排序後的去重結果
    - 名稱：deduplicate_and_sort
- 輸入：list of int
- 輸出：排序後去重的 list of int
- 若輸入含非整數，拋出 ValueError("Invalid input")
- 加入清楚的 docstring（說明參數與回傳）
- 通過 flake8/black 格式檢查
- 通過 pytest 測試（test_dedup.py）
- 使用明確的輸入驗證（僅允許 int）
- 對 None/空值顯式處理
- 保持循環複雜度低（不做過度巢狀）
- cyclomatic complexity < 5
- 文件字串（docstring）完整描述例外情況
"""
def unique_sorted(arr):
    """
    接收一個整數陣列並回傳排序後的去重結果

    參數:
    arr (list of int): 要處理的整數陣列

    回傳:
    list of int: 排序後且去重的整數陣列
    """
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("Invalid input")   
    return sorted(set(arr)) 

def deduplicate_and_sort(arr):
    """
    接收一個整數陣列並回傳排序後的去重結果

    參數:
    arr (list of int): 要處理的整數陣列

    回傳:
    list of int: 排序後且去重的整數陣列

    例外情況:
    ValueError: 當輸入陣列包含非整數元素時拋出
    """
    if arr is None:
        return []
    if not isinstance(arr, list):
        raise ValueError("Invalid input")
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("Invalid input")
    return sorted(set(arr))