# 情境 Demo
## 命名
- 變數命名

```python
aaa = 1

for i in range(10):
    aaa += i * i + 1
```
```python
def calculate_bmi(height, weight):
    aaa = weight / (height * height)
    return aaa
```
- 函數命名
```python
def cal(height, weight):
    bmi = weight / (height * height)
    return bmi
```
- 函數註解
```python
def add(a, b):
    return a + b
```
- 修正程式
```python
def add(a, b):
    return a - b
```
- 解釋程式碼
```

```
- 產生測試程式
```
用 /tests 產生
```
- 產生文件
```
專案文件
部署文件
```
- 無支援
```
棒球是什麼？
```
- Git Commit 說明
```
自動產生 Commit 內容
```
- 產生 HTTP 檔案
```
from flask import Flask, jsonify, request

app = Flask(__name__)

# 定義一個基本的路由
@app.route('/')
def home():
    return "Hello, Flask!"

# 定義一個 API 路由
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello, this is your data!',
        'status': 'success'
    }
    return jsonify(data)

# 啟動 Flask 應用程式
if __name__ == '__main__':
    app.run(debug=True)
    
產生 API 的 HTTP 檔案來測試 API
```
- Json to Class
```
  {
    "id": 1,
    "title": "Walk the dog",
    "dueBy": null,
    "isComplete": false
  }
```
- Python to CSharp
```python
def main():
    num1 = int(input("請輸入第一個數字："))
    num2 = int(input("請輸入第二個數字："))

    sum = num1 + num2
    print("兩個數字的和是：" + str(sum))

if __name__ == "__main__":
    main()
```
- Code Review
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    x = 10
    y = 5
    print("Add:", add(x, y))
    print("Subtract:", subtract(x, y))
    print("Multiply:", multiply(x, y))
    print("Divide:", divide(x, y))

if __name__ == "__main__":
    main()
```
- 重構
```python
number = 10

if number > 0:
    print("Number is positive.")
    if number > 5:
        print("Number is greater than 5.")
        if number > 8:
            print("Number is greater than 8.")
        else:
            print("Number is 6 or 7.")
    else:
        print("Number is 1 to 5.")
else:
    print("Number is non-positive.")
```