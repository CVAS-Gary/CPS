# 由 GitHub Copilot 產生
"""
BMI 計算功能的單元測試

此測試模組包含根據「BMI 測試案例.md」定義的測試案例。
"""

import unittest
from bmi import calculate_bmi


class TestCalculateBMI(unittest.TestCase):
    """BMI 計算的測試類別"""

    def test_calculate_bmi_normal_weight(self):
        """
        測試案例 1: 正常體重
        輸入: 體重 70 公斤, 身高 1.75 公尺
        預期輸出: BMI 值 22.86
        """
        WEIGHT = 70
        HEIGHT = 1.75
        EXPECTED_BMI = 22.86

        RESULT = calculate_bmi(WEIGHT, HEIGHT)

        self.assertEqual(RESULT, EXPECTED_BMI)

    def test_calculate_bmi_overweight(self):
        """
        測試案例 2: 過重
        輸入: 體重 85 公斤, 身高 1.75 公尺
        預期輸出: BMI 值 27.76
        """
        WEIGHT = 85
        HEIGHT = 1.75
        EXPECTED_BMI = 27.76

        RESULT = calculate_bmi(WEIGHT, HEIGHT)

        self.assertEqual(RESULT, EXPECTED_BMI)

    def test_calculate_bmi_underweight(self):
        """
        測試案例 3: 體重過輕
        輸入: 體重 50 公斤, 身高 1.75 公尺
        預期輸出: BMI 值 16.33
        """
        WEIGHT = 50
        HEIGHT = 1.75
        EXPECTED_BMI = 16.33

        RESULT = calculate_bmi(WEIGHT, HEIGHT)

        self.assertEqual(RESULT, EXPECTED_BMI)

    def test_calculate_bmi_zero_height_raises_error(self):
        """
        測試案例: 身高為零時應拋出 ValueError
        """
        WEIGHT = 70
        HEIGHT = 0

        with self.assertRaises(ValueError) as CONTEXT:
            calculate_bmi(WEIGHT, HEIGHT)

        self.assertEqual(str(CONTEXT.exception), "身高必須為正數")

    def test_calculate_bmi_negative_weight_raises_error(self):
        """
        測試案例: 體重為負數時應拋出 ValueError
        """
        WEIGHT = -70
        HEIGHT = 1.75

        with self.assertRaises(ValueError) as CONTEXT:
            calculate_bmi(WEIGHT, HEIGHT)

        self.assertEqual(str(CONTEXT.exception), "體重必須為正數")


if __name__ == "__main__":
    unittest.main()
