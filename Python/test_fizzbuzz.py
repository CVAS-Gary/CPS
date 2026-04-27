# 由 GitHub Copilot 產生
import pytest
from fizzbuzz import FIZZBUZZ

# Copilot Chat 未參考任何 GitHub 原始碼

def test_fizzbuzz_divisible_by_3():
    # 測試能被 3 整除但不能被 5 整除時回傳 'Fizz'
    INPUT = 9
    RESULT = FIZZBUZZ(INPUT)
    assert RESULT == 'Fizz'

def test_fizzbuzz_divisible_by_5():
    # 測試能被 5 整除但不能被 3 整除時回傳 'Buzz'
    INPUT = 10
    RESULT = FIZZBUZZ(INPUT)
    assert RESULT == 'Buzz'

def test_fizzbuzz_divisible_by_3_and_5():
    # 測試能同時被 3 和 5 整除時回傳 'FizzBuzz'
    INPUT = 15
    RESULT = FIZZBUZZ(INPUT)
    assert RESULT == 'FizzBuzz'

def test_fizzbuzz_not_divisible_by_3_or_5():
    # 測試不能被 3 或 5 整除時回傳數字字串
    INPUT = 7
    RESULT = FIZZBUZZ(INPUT)
    assert RESULT == '7'
