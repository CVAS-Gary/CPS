# 由 GitHub Copilot 產生
"""
BMI（身體質量指數）計算模組

此模組提供計算 BMI 的功能。
"""


def calculate_bmi(WEIGHT: float, HEIGHT: float) -> float:
    """
    計算身體質量指數 (BMI)。

    參數:
        WEIGHT: 體重（公斤）
        HEIGHT: 身高（公尺）

    回傳:
        BMI 值，四捨五入至小數點後兩位

    例外:
        ValueError: 當身高或體重為零或負數時
    """
    if HEIGHT <= 0:
        raise ValueError("身高必須為正數")
    if WEIGHT <= 0:
        raise ValueError("體重必須為正數")

    BMI_VALUE = WEIGHT / (HEIGHT * HEIGHT)
    return round(BMI_VALUE, 2)
