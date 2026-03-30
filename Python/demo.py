# 由 GitHub Copilot 產生
# 本建議未參考任何 GitHub 原始碼

def fizzbuzz(N):
    for I in range(1, N + 1):
        if I % 15 == 0:
            print("FizzBuzz")
        elif I % 3 == 0:
            print("Fizz")
        elif I % 5 == 0:
            print("Buzz")
        else:
            print(I)
if __name__ == "__main__":
    N = int(input("Enter a number: "))
    fizzbuzz(N)