111
# 由 GitHub Copilot 產生
# 參考來源: 無
# filepath: d:\OneDrive\CloudRiches\Source Code\Python\demo.py
# ...existing code...
def fizz_buzz():
    # 遍歷 1 到 100 的所有整數
    for I in range(1, 101):
        # 檢查是否同時能被 3 和 5 整除
        if I % 3 == 0 and I % 5 == 0:
            print("FizzBuzz")
        # 檢查是否能被 3 整除
        elif I % 3 == 0:
            print("Fizz")
        # 檢查是否能被 5 整除
        elif I % 5 == 0:
            print("Buzz")
        # 其他情況直接輸出數字
        else:
            print(I)


# ...existing code...
if __name__ == "__main__":
    fizz_buzz()
# ...existing code...
222