# 由 GitHub Copilot 產生


def fizzbuzz_single(number: int) -> str:
    """
    計算單一數字的 FizzBuzz 結果。

    參數:
        number: 要進行 FizzBuzz 計算的整數

    返回:
        FizzBuzz 計算結果字符串
        - 如果能被 15 整除，返回 'FizzBuzz'
        - 如果能被 3 整除，返回 'Fizz'
        - 如果能被 5 整除，返回 'Buzz'
        - 否則返回該數字的字符串形式
    """
    # 檢查是否能被 15 整除（3 和 5 的最小公倍數）
    if number % 15 == 0:
        return "FizzBuzz"
    # 檢查是否能被 3 整除
    elif number % 3 == 0:
        return "Fizz"
    # 檢查是否能被 5 整除
    elif number % 5 == 0:
        return "Buzz"
    # 都不符合，返回數字本身
    else:
        return str(number)


def fizzbuzz_range(START_NUMBER: int, END_NUMBER: int) -> list:
    """
    計算指定範圍內所有數字的 FizzBuzz 結果。

    參數:
        START_NUMBER: 範圍開始（包含）
        END_NUMBER: 範圍結束（包含）

    返回:
        包含 FizzBuzz 結果的列表

    異常:
        ValueError: 如果 START_NUMBER 大於 END_NUMBER 或數字不合法
    """
    # 驗證輸入參數
    if START_NUMBER > END_NUMBER:
        raise ValueError("START_NUMBER 不能大於 END_NUMBER")

    if START_NUMBER < 1:
        raise ValueError("START_NUMBER 必須為正整數")

    # 計算範圍內所有數字的 FizzBuzz 結果
    RESULT_LIST = []
    for CURRENT_NUMBER in range(START_NUMBER, END_NUMBER + 1):
        FIZZBUZZ_RESULT = fizzbuzz_single(CURRENT_NUMBER)
        RESULT_LIST.append(FIZZBUZZ_RESULT)

    return RESULT_LIST
