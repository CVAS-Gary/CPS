# 由 GitHub Copilot 產生
# 未參考任何 GitHub 原始碼

def add(A, B):
    return A + B

def subtract(A, B):
    return A - B

def multiply(A, B):
    return A * B

def divide(A, B):
    # 檢查除數是否為零
    if B == 0:
        raise ValueError("無法除以零")
    return A / B

def main():
    X = 10
    Y = 5
    print("加法:", add(X, Y))
    print("減法:", subtract(X, Y))
    print("乘法:", multiply(X, Y))
    print("除法:", divide(X, Y))

if __name__ == "__main__":
    main()