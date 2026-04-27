# FizzBuzz 網站 - 開發者指南

為開發者提供的完整開發和貢獻指南。

## 目錄

- [開發環境設置](#開發環境設置)
- [項目架構](#項目架構)
- [編碼規範](#編碼規範)
- [開發流程](#開發流程)
- [測試](#測試)
- [部署](#部署)
- [常見開發任務](#常見開發任務)
- [貢獻指南](#貢獻指南)

## 開發環境設置

### 1. 複製或下載專案

```bash
cd fizzbuzz_website
```

### 2. 建立虛擬環境

**Windows (PowerShell)**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 安裝開發依賴

```bash
pip install -r requirements.txt
```

### 4. 驗證環境

```bash
python --version  # 應該是 3.10 或更高
pip list  # 應該看到 Flask, pytest, black, flake8
```

### 5. 運行應用

```bash
python app/main.py
```

訪問 http://localhost:5000

## 項目架構

```
fizzbuzz_website/
│
├── app/                          # Flask 應用包
│   ├── __init__.py              # 包初始化
│   ├── main.py                  # Flask 應用、路由、API 端點
│   └── fizzbuzz.py              # FizzBuzz 核心邏輯
│
├── templates/                    # Jinja2 HTML 模板
│   └── index.html               # 主頁面
│
├── static/                       # 靜態資源
│   ├── style.css                # CSS 樣式
│   └── script.js                # 前端 JavaScript
│
├── tests/                        # pytest 單元測試
│   ├── __init__.py              # 包初始化
│   ├── test_fizzbuzz.py         # 核心邏輯測試
│   └── test_api.py              # API 端點測試
│
├── requirements.txt              # Python 依賴
├── README.md                     # 項目總覽
├── API_DOCUMENTATION.md          # API 參考
├── USER_GUIDE.md                # 使用者指南
└── DEVELOPER_GUIDE.md           # 本文件
```

### 代碼流程圖

```
HTTP 請求
   ↓
app/main.py (Flask 路由)
   ↓
app/fizzbuzz.py (核心邏輯)
   ↓
計算結果
   ↓
JSON 響應
   ↓
前端 (templates/index.html + static/script.js)
   ↓
用戶看到結果
```

## 編碼規範

### Python 代碼規範

#### 變數命名

**必須使用大寫下劃線**:
```python
# ✅ 正確
INPUT_NUMBER = 15
FIZZBUZZ_RESULT = "FizzBuzz"
RESULT_LIST = []

# ❌ 錯誤
input_number = 15
fizzbuzzResult = "FizzBuzz"
resultList = []
```

#### 函式命名

使用 snake_case（小寫下劃線）:
```python
# ✅ 正確
def fizzbuzz_single(number: int) -> str:
    pass

def fizzbuzz_range(start_number: int, end_number: int) -> list:
    pass

# ❌ 錯誤
def FizzBuzzSingle(number: int) -> str:
    pass

def fizzbuzz_single_number(number: int) -> str:
    pass
```

#### 類別命名

使用 PascalCase:
```python
# ✅ 正確
class TestFizzBuzz:
    pass

# ❌ 錯誤
class test_fizzbuzz:
    pass
```

#### 註釋語言

**所有註釋必須使用繁體中文**:
```python
# ✅ 正確
# 檢查是否能被 15 整除
if number % 15 == 0:
    return "FizzBuzz"

# ❌ 錯誤
# Check if divisible by 15
if number % 15 == 0:
    return "FizzBuzz"
```

#### PEP 8 遵守

```python
# ✅ 正確
def fizzbuzz_single(number: int) -> str:
    """計算單一數字的 FizzBuzz 結果。"""
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

# ❌ 錯誤
def fizzbuzz_single(number:int)->str:
    if number%15==0:return"FizzBuzz"
    elif number%3==0:return"Fizz"
```

#### 導入順序

```python
# 標準庫
import json
import sys
from pathlib import Path

# 第三方庫
from flask import Flask, render_template

# 本地應用
from app.fizzbuzz import fizzbuzz_single
```

### 函式和類別文檔字符串

```python
def fizzbuzz_range(START_NUMBER: int, END_NUMBER: int) -> list:
    """
    計算指定範圍內所有數字的 FizzBuzz 結果。

    參數:
        START_NUMBER: 範圍開始（包含）
        END_NUMBER: 範圍結束（包含）

    返回:
        包含 FizzBuzz 結果的列表

    異常:
        ValueError: 如果 START_NUMBER 大於 END_NUMBER
    """
    # 實現...
```

## 開發流程

### 1. 建立功能分支

```bash
git checkout -b feature/your-feature-name
```

### 2. 編寫代碼

遵循編碼規範，編寫新功能。

### 3. 編寫或更新測試

```bash
# 添加測試到 tests/ 目錄
python -m pytest tests/ -v
```

所有新功能必須有對應的單元測試。

### 4. 格式化代碼

```bash
black app/ tests/
```

### 5. 檢查代碼質量

```bash
flake8 app/ tests/
```

### 6. 最後驗證

```bash
# 運行所有測試
pytest tests/ -v

# 運行應用並手動測試
python app/main.py
```

### 7. 提交並推送

```bash
git add .
git commit -m "描述你的改動"
git push origin feature/your-feature-name
```

### 8. 創建 Pull Request

在 GitHub 上創建 PR 並等待審核。

## 測試

### 測試框架

使用 **pytest** 進行單元測試。

### 運行測試

```bash
# 運行所有測試
pytest tests/

# 運行特定文件
pytest tests/test_fizzbuzz.py

# 運行特定測試
pytest tests/test_fizzbuzz.py::TestFizzBuzzSingle::test_fizzbuzz_single_fizzbuzz

# 詳細輸出
pytest -v tests/

# 顯示列印信息
pytest -s tests/
```

### 測試覆蓋率

```bash
# 生成覆蓋率報告
pytest --cov=app tests/

# 詳細覆蓋率報告
pytest --cov=app --cov-report=html tests/
```

### 編寫測試

```python
import pytest
from app.fizzbuzz import fizzbuzz_single

class TestFizzBuzz:
    """FizzBuzz 測試類別"""

    def test_fizzbuzz_number(self):
        """測試 FizzBuzz 數字"""
        assert fizzbuzz_single(15) == "FizzBuzz"

    def test_invalid_input(self):
        """測試無效輸入"""
        with pytest.raises(ValueError):
            fizzbuzz_range(10, 5)
```

## 部署

### 開發環境

```bash
python app/main.py  # debug=True，會自動重新加載
```

### 生產環境

使用 **Gunicorn** 和 **Nginx**。

#### 1. 安裝 Gunicorn

```bash
pip install gunicorn
```

#### 2. 創建 WSGI 入口點

修改 `app/main.py`：

```python
if __name__ == "__main__":
    # 開發環境
    APP.run(debug=True)

# 生產環境用這個
# gunicorn -w 4 app.main:APP
```

#### 3. 運行應用

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app.main:APP
```

#### 4. 部署到雲平台

**Heroku**:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

**PythonAnywhere**:
1. 上傳代碼
2. 配置虛擬環境
3. 配置 Web 應用設置

## 常見開發任務

### 任務 1：添加新的 API 端點

**步驟**:

1. 在 `app/fizzbuzz.py` 中添加邏輯函式

```python
def fizzbuzz_custom(NUMBER: int, DIVISOR: int) -> str:
    """自定義 FizzBuzz 邏輯"""
    if NUMBER % DIVISOR == 0:
        return f"Custom{DIVISOR}"
    return str(NUMBER)
```

2. 在 `app/main.py` 中添加路由

```python
@APP.route("/api/fizzbuzz/custom/<int:number>/<int:divisor>")
def api_fizzbuzz_custom(number, divisor):
    """自定義 FizzBuzz API"""
    RESULT = fizzbuzz_custom(number, divisor)
    return jsonify({"success": True, "result": RESULT})
```

3. 在 `tests/test_api.py` 中添加測試

```python
def test_api_fizzbuzz_custom(self, CLIENT):
    """測試自定義 API"""
    RESPONSE = CLIENT.get("/api/fizzbuzz/custom/10/2")
    DATA = json.loads(RESPONSE.data)
    assert DATA["success"] is True
```

4. 測試並提交

### 任務 2：修改前端樣式

1. 編輯 `static/style.css`
2. 在瀏覽器中刷新查看效果（可能需要清除緩存）
3. 驗證響應式設計

### 任務 3：優化 FizzBuzz 邏輯

1. 修改 `app/fizzbuzz.py` 中的函式
2. 更新相關的單元測試
3. 運行所有測試確保無破壞

```bash
pytest tests/ -v
```

### 任務 4：添加新的依賴

1. 安裝包：`pip install package-name`
2. 更新 `requirements.txt`：`pip freeze > requirements.txt`
3. 提交更新

### 任務 5：修復 Bug

1. 創建 issue 或 bug 分支
2. 編寫重現 bug 的測試
3. 修復代碼
4. 確保測試通過
5. 創建 PR

## 貢獻指南

### 貢獻流程

1. **報告 Issue**
   - 清楚描述問題
   - 提供重現步驟
   - 包括你的環境信息

2. **提交 PR**
   - 對應一個 issue
   - 清晰的提交信息
   - 包括測試
   - 遵循編碼規範

3. **代碼審核**
   - 維護者會審核 PR
   - 可能需要進行修改
   - 批准後合併到 main

### 提交信息規範

```
type(scope): subject

詳細說明（可選）

修復 #123
```

**Type 類型**:
- `feat`: 新功能
- `fix`: Bug 修復
- `docs`: 文件更新
- `style`: 代碼格式
- `refactor`: 代碼重構
- `test`: 測試相關
- `chore`: 構建或依賴

**範例**:
```
feat(api): 添加自定義 FizzBuzz 端點

支持用戶自定義除數和被除數。

修復 #45
```

### 代碼審核檢查清單

提交 PR 前確保：

- [ ] ✅ 代碼遵循 PEP 8 和公司規範
- [ ] ✅ 變數使用大寫下劃線命名
- [ ] ✅ 所有註釋使用繁體中文
- [ ] ✅ 編寫了相應的單元測試
- [ ] ✅ 所有測試通過：`pytest tests/ -v`
- [ ] ✅ 代碼通過格式化：`black app/ tests/`
- [ ] ✅ 代碼通過質量檢查：`flake8 app/ tests/`
- [ ] ✅ 更新了相應的文檔
- [ ] ✅ 提交信息清晰有意義

## 故障排除

### 問題：測試失敗

```bash
# 運行失敗的測試以查看詳細信息
pytest -vvs tests/test_file.py::TestClass::test_method
```

### 問題：導入錯誤

```bash
# 確認虛擬環境已激活
# 重新安裝依賴
pip install -r requirements.txt
```

### 問題：代碼風格錯誤

```bash
# 自動修復風格問題
black app/ tests/
flake8 app/ tests/  # 查看問題列表
```

### 問題：應用無法啟動

```bash
# 檢查詳細錯誤
python -m flask run --debug

# 或直接運行
python app/main.py
```

---

## 有用的資源

- 📚 [Flask 官方文檔](https://flask.palletsprojects.com/)
- 🧪 [pytest 文檔](https://docs.pytest.org/)
- 📏 [PEP 8 風格指南](https://pep8.org/)
- 🔍 [Black 代碼格式化](https://black.readthedocs.io/)
- 🐍 [Python 官方文檔](https://docs.python.org/)

---

**感謝你的貢獻！** 🙏

如有問題，歡迎提出 Issue 或討論。
