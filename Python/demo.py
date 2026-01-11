from __future__ import annotations

from typing import List


def deduplicate_and_sort(input_list: List[int]) -> List[int]:
    """
    接收一個整數列表，回傳排序後去重的整數列表。

    參數:
        input_list (List[int]): 要處理的整數列表。

    回傳:
        List[int]: 去重並由小到大排序後的整數列表。

    例外:
        ValueError("Invalid input"): 當 input_list 不是 list 或包含非整數元素時拋出。
    """
    if not isinstance(input_list, list):
        raise ValueError("Invalid input")
    if not all(isinstance(x, int) for x in input_list):
        raise ValueError("Invalid input")
    return sorted(set(input_list))