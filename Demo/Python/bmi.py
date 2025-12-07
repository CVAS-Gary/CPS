# 由 GitHub Copilot 產生
# 計算 BMI 的程式
# 輸入身高(公分)與體重(公斤)，輸出 BMI 值

身高 = float(input("請輸入身高(公分)："))
體重 = float(input("請輸入體重(公斤)："))

# 計算 BMI
BMI = 體重 / ((身高 / 100) ** 2)

print(f"您的 BMI 為：{BMI:.2f}")
