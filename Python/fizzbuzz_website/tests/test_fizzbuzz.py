# 由 GitHub Copilot 產生

import pytest
from app.fizzbuzz import fizzbuzz_single, fizzbuzz_range


class TestFizzBuzzSingle:
    """
    FizzBuzz 單一數字計算的單元測試類別。
    測試各種邊界情況和正常情況。
    """

    def test_fizzbuzz_single_fizzbuzz(self):
        """測試能被 15 整除的數字應返回 'FizzBuzz'"""
        assert fizzbuzz_single(15) == "FizzBuzz"
        assert fizzbuzz_single(30) == "FizzBuzz"
        assert fizzbuzz_single(45) == "FizzBuzz"

    def test_fizzbuzz_single_fizz(self):
        """測試能被 3 整除但不能被 5 整除的數字應返回 'Fizz'"""
        assert fizzbuzz_single(3) == "Fizz"
        assert fizzbuzz_single(6) == "Fizz"
        assert fizzbuzz_single(9) == "Fizz"
        assert fizzbuzz_single(12) == "Fizz"

    def test_fizzbuzz_single_buzz(self):
        """測試能被 5 整除但不能被 3 整除的數字應返回 'Buzz'"""
        assert fizzbuzz_single(5) == "Buzz"
        assert fizzbuzz_single(10) == "Buzz"
        assert fizzbuzz_single(20) == "Buzz"
        assert fizzbuzz_single(25) == "Buzz"

    def test_fizzbuzz_single_number(self):
        """測試既不能被 3 也不能被 5 整除的數字應返回該數字的字符串"""
        assert fizzbuzz_single(1) == "1"
        assert fizzbuzz_single(2) == "2"
        assert fizzbuzz_single(4) == "4"
        assert fizzbuzz_single(7) == "7"
        assert fizzbuzz_single(8) == "8"
        assert fizzbuzz_single(97) == "97"

    def test_fizzbuzz_single_large_numbers(self):
        """測試大數字"""
        assert fizzbuzz_single(300) == "FizzBuzz"
        assert fizzbuzz_single(999) == "Fizz"
        assert fizzbuzz_single(1000) == "Buzz"


class TestFizzBuzzRange:
    """
    FizzBuzz 範圍計算的單元測試類別。
    測試各種範圍情況和邊界條件。
    """

    def test_fizzbuzz_range_single_number(self):
        """測試範圍只包含一個數字的情況"""
        RESULT = fizzbuzz_range(1, 1)
        assert RESULT == ["1"]

    def test_fizzbuzz_range_small(self):
        """測試小範圍的計算結果"""
        RESULT = fizzbuzz_range(1, 5)
        EXPECTED = ["1", "2", "Fizz", "4", "Buzz"]
        assert RESULT == EXPECTED

    def test_fizzbuzz_range_to_fifteen(self):
        """測試 1 到 15 的完整計算"""
        RESULT = fizzbuzz_range(1, 15)
        EXPECTED = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]
        assert RESULT == EXPECTED

    def test_fizzbuzz_range_custom_start(self):
        """測試自定義開始位置的範圍"""
        RESULT = fizzbuzz_range(10, 15)
        EXPECTED = ["Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
        assert RESULT == EXPECTED

    def test_fizzbuzz_range_large(self):
        """測試較大的範圍"""
        RESULT = fizzbuzz_range(1, 30)
        # 驗證結果長度
        assert len(RESULT) == 30
        # 驗證特定位置的值
        assert RESULT[14] == "FizzBuzz"  # 第 15 個元素（索引 14）應為 FizzBuzz
        assert RESULT[29] == "FizzBuzz"  # 第 30 個元素（索引 29）應為 FizzBuzz

    def test_fizzbuzz_range_invalid_start_greater_than_end(self):
        """測試開始數字大於結束數字應拋出異常"""
        with pytest.raises(ValueError):
            fizzbuzz_range(10, 5)

    def test_fizzbuzz_range_invalid_negative_start(self):
        """測試開始數字為負數應拋出異常"""
        with pytest.raises(ValueError):
            fizzbuzz_range(-5, 10)

    def test_fizzbuzz_range_invalid_zero_start(self):
        """測試開始數字為零應拋出異常"""
        with pytest.raises(ValueError):
            fizzbuzz_range(0, 10)


class TestFizzBuzzEdgeCases:
    """
    FizzBuzz 的邊界情況測試。
    """

    def test_divisible_by_three_and_five(self):
        """確保倍數規則正確：15, 30, 45... 返回 FizzBuzz"""
        for NUMBER in [15, 30, 45, 60, 75, 90, 105]:
            assert (
                fizzbuzz_single(NUMBER) == "FizzBuzz"
            ), f"{NUMBER} 應返回 FizzBuzz"

    def test_not_divisible_by_three_or_five(self):
        """確保非倍數正確返回數字"""
        for NUMBER in [1, 2, 4, 7, 8, 11, 13, 14, 16]:
            assert fizzbuzz_single(NUMBER) == str(NUMBER)

    def test_fizzbuzz_count_in_range(self):
        """驗證 1-100 範圍內 FizzBuzz 的數量"""
        RESULT = fizzbuzz_range(1, 100)
        FIZZBUZZ_COUNT = RESULT.count("FizzBuzz")
        # 1-100 中被 15 整除的數：15, 30, 45, 60, 75, 90 共 6 個
        assert FIZZBUZZ_COUNT == 6

    def test_fizz_count_in_range(self):
        """驗證 1-100 範圍內 Fizz 的數量"""
        RESULT = fizzbuzz_range(1, 100)
        FIZZ_COUNT = RESULT.count("Fizz")
        # 1-100 中被 3 整除但不被 15 整除的數有 27 個
        # (33 個被 3 整除的數 - 6 個被 15 整除的數 = 27)
        assert FIZZ_COUNT == 27

    def test_buzz_count_in_range(self):
        """驗證 1-100 範圍內 Buzz 的數量"""
        RESULT = fizzbuzz_range(1, 100)
        BUZZ_COUNT = RESULT.count("Buzz")
        # 1-100 中被 5 整除但不被 15 整除的數有 14 個
        # (20 個被 5 整除的數 - 6 個被 15 整除的數 = 14)
        assert BUZZ_COUNT == 14
