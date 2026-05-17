# 由 GitHub Copilot 產生

import pytest
from math_ops import add


class TestAdd:
    """測試 add 函式的單元測試類別"""

    def test_add_positive_numbers(self):
        """測試兩個正數的相加"""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """測試兩個負數的相加"""
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        """測試正數和負數的相加"""
        assert add(5, -3) == 2

    def test_add_zero(self):
        """測試與零的相加"""
        assert add(0, 0) == 0
        assert add(5, 0) == 5

    def test_add_floats(self):
        """測試浮點數的相加"""
        assert add(1.5, 2.5) == 4.0

    def test_add_large_numbers(self):
        """測試大數字的相加"""
        assert add(1000000, 2000000) == 3000000
