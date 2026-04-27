# FizzBuzz 計算器

> 一個互動式 FizzBuzz 計算網站，使用 Flask 和 Python 開發。

## 📋 目錄

- [功能](#功能)
- [技術棧](#技術棧)
- [系統要求](#系統要求)
- [安裝](#安裝)
- [使用方法](#使用方法)
- [文件說明](#文件說明)
- [測試](#測試)
- [常見問題](#常見問題)
- [貢獻](#貢獻)

## 功能

✨ **主要功能**

- 🔢 **單一數字計算** - 輸入一個數字，立即得到 FizzBuzz 結果
- 📊 **範圍計算** - 計算指定範圍內所有數字的 FizzBuzz 結果
- 📈 **統計信息** - 自動統計 Fizz、Buzz 和 FizzBuzz 的出現次數
- 🎨 **優雅的界面** - 響應式設計，支援桌面和移動設備
- ⚡ **快速 API** - 基於 REST 的後端 API，支持 GET 和 POST 請求

### FizzBuzz 規則

- 如果數字能被 **15 整除**（3 和 5 的最小公倍數），返回 **FizzBuzz**
- 如果數字能被 **3 整除**，返回 **Fizz**
- 如果數字能被 **5 整除**，返回 **Buzz**
- 否則返回 **該數字本身**

## 技術棧

| 層級 | 技術 |
|------|------|
| **後端** | Python 3.10+、Flask 2.3.3 |
| **前端** | HTML5、CSS3、原生 JavaScript |
| **測試** | pytest、Flask 測試客戶端 |
| **代碼質量** | black、flake8 |

## 系統要求

- **Python**: 3.10 或更高版本
- **操作系統**: Windows、macOS、Linux
- **瀏覽器**: 支援現代 JavaScript 的任何瀏覽器

## 安裝

### 1. 克隆或下載專案

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

### 3. 安裝依賴

```bash
pip install -r requirements.txt
```

## 使用方法

### 啟動應用

```bash
python app/main.py
```

應用將在 `http://localhost:5000` 啟動。

### 訪問網站

在瀏覽器中打開 `http://localhost:5000`，你將看到以下界面：

1. **單一數字計算區域** - 輸入一個數字，點擊「計算」
2. **範圍計算區域** - 輸入開始和結束數字，點擊「計算」
3. **統計信息區域** - 自動顯示結果統計

### API 使用

詳細的 API 文檔請查看 [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)。

#### 快速範例

**計算單一數字 (GET)**
```bash
curl "http://localhost:5000/api/fizzbuzz?number=15"
```

響應:
```json
{
  "success": true,
  "result": "FizzBuzz"
}
```

**計算範圍 (GET)**
```bash
curl "http://localhost:5000/api/fizzbuzz?start=1&end=5"
```

響應:
```json
{
  "success": true,
  "result": ["1", "2", "Fizz", "4", "Buzz"]
}
```

## 文件說明

### 項目結構

```
fizzbuzz_website/
├── app/                          # Flask 應用主目錄
│   ├── __init__.py              # 包初始化文件
│   ├── main.py                  # Flask 應用和路由定義
│   └── fizzbuzz.py              # 核心 FizzBuzz 邏輯
├── templates/                    # HTML 模板
│   └── index.html               # 主頁面
├── static/                       # 靜態資源
│   ├── style.css                # CSS 樣式
│   └── script.js                # JavaScript 邏輯
├── tests/                        # 單元測試
│   ├── __init__.py              # 包初始化文件
│   ├── test_fizzbuzz.py         # FizzBuzz 核心函式測試
│   └── test_api.py              # API 路由測試
├── requirements.txt              # Python 依賴列表
└── README.md                     # 本文件
```

### 核心文件說明

| 文件 | 說明 |
|------|------|
| `app/fizzbuzz.py` | 包含 `fizzbuzz_single()` 和 `fizzbuzz_range()` 函式 |
| `app/main.py` | Flask 應用、路由和 API 端點 |
| `templates/index.html` | 用戶界面 HTML |
| `static/style.css` | 界面樣式和響應式設計 |
| `static/script.js` | 前端交互邏輯 |
| `tests/test_fizzbuzz.py` | 核心函式的單元測試 |
| `tests/test_api.py` | API 路由的單元測試 |

## 測試

### 運行所有測試

```bash
pytest tests/
```

### 運行特定測試

```bash
# 只運行 FizzBuzz 邏輯測試
pytest tests/test_fizzbuzz.py

# 只運行 API 測試
pytest tests/test_api.py
```

### 帶詳細輸出的測試

```bash
pytest -v tests/
```

### 測試覆蓋率

```bash
pytest --cov=app tests/
```

### 測試包括的場景

✅ FizzBuzz 邏輯測試
- 單一數字計算（Fizz、Buzz、FizzBuzz、普通數字）
- 範圍計算
- 邊界情況和大數字
- 輸入驗證和錯誤處理

✅ API 測試
- GET 和 POST 請求
- 正確的返回格式
- 錯誤情況處理
- 參數驗證

## 常見問題

### Q: 我可以修改 FizzBuzz 的規則嗎？

A: 可以！修改 `app/fizzbuzz.py` 中的 `fizzbuzz_single()` 函式。例如：
```python
def fizzbuzz_single(number: int) -> str:
    if number % 15 == 0:
        return "自定義結果"
    # ... 其他邏輯
```

### Q: 如何修改端口號？

A: 在 `app/main.py` 的最後一行修改：
```python
if __name__ == "__main__":
    APP.run(debug=True, host="0.0.0.0", port=8000)  # 改為 8000
```

### Q: 支援的最大範圍是多少？

A: 當前限制為 10,000 個數字。可在 `app/main.py` 的 `api_fizzbuzz()` 函式中修改：
```python
if END_NUMBER - START_NUMBER > 10000:  # 改為你想要的值
```

### Q: 如何在生產環境部署？

A: 查看 [DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md) 中的部署部分。

## 貢獻

### 開發環境設置

1. 建立虛擬環境並安裝依賴（見安裝部分）
2. 修改代碼
3. 運行測試確保無破壞
4. 使用 black 格式化代碼：`black app/ tests/`
5. 使用 flake8 檢查風格：`flake8 app/ tests/`

### 代碼標準

- 遵循 PEP 8 風格指南
- 變數名使用大寫下劃線（`MY_VARIABLE`）
- 代碼註釋使用繁體中文
- 所有新功能需要添加相應的單元測試

詳細指南見 [DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md)。

---

## 許可證

本專案開源發布。

## 聯繫方式

如有問題或建議，歡迎提出 Issue 或 Pull Request。

---

**祝你使用愉快！** 🎉
