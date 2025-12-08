# 由 GitHub Copilot 產生
# 計算 BMI 的程式
# 輸入身高(公分)與體重(公斤)，輸出 BMI 值

height_cm = float(input("請輸入身高(公分)："))
weight_kg = float(input("請輸入體重(公斤)："))

# 計算 BMI
bmi = weight_kg / ((height_cm / 100) ** 2)

print(f"您的 BMI 為：{bmi:.2f}")
