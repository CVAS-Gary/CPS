def add(x: int, y: int) -> int:
	"""
	將兩個整數相加並回傳其和。
	Args:
		x (int): 第一個加數
		y (int): 第二個加數
	Returns:
		int: 兩數之和
	"""
	return x + y
# Red: 撰寫 add(x, y) 的 pytest 測試
import pytest

def test_add():
	assert add(1, 2) == 3
	assert add(-1, 1) == 0
	assert add(0, 0) == 0
