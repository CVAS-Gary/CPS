# BMI 計算器 - 健康體重管理系統

## 📋 項目概述

一個現代化的 Python Flask Web 應用，用於快速計算 BMI（身體質量指數）並獲得健康分類建議。

**版本**: 1.0.0（基礎版本）  
**開發語言**: Python 3.10+  
**前端**: HTML5 + CSS3 + Vanilla JavaScript  
**後端**: Flask  
**測試框架**: pytest

---

## ✨ 核心功能

- ✅ **即時BMI計算** - 輸入身高和體重，秒速獲得BMI值
- ✅ **健康分類** - 自動分類為：低體重/正常/過重/肥胖
- ✅ **友好界面** - 響應式設計，支援桌面、平板、手機
- ✅ **輸入驗證** - 客戶端和服務器雙層驗證
- ✅ **RESTful API** - 易於集成的API端點

---

## 🏗️ 項目結構

```
bmi_calculator/
├── app/
│   ├── __init__.py          # 應用初始化
│   ├── bmi.py               # BMI計算核心邏輯
│   └── main.py              # Flask應用主入口
├── templates/
│   └── index.html           # HTML模板
├── static/
│   ├── style.css            # 樣式表
│   └── script.js            # 前端邏輯
├── tests/
│   ├── __init__.py
│   └── test_bmi.py          # 單元測試
├── docs/
│   ├── API_DOCUMENTATION.md # API文件
│   ├── DEVELOPER_GUIDE.md   # 開發指南
│   └── USER_GUIDE.md        # 用戶指南
├── README.md                # 本文件
├── requirements.txt         # 依賴清單
└── .gitignore              # Git忽略文件
```

---

## 🚀 快速開始

### 1️⃣ 環境準備

**克隆或下載項目**
```bash
cd bmi_calculator
```

**創建虛擬環境（Windows PowerShell）**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**創建虛擬環境（macOS/Linux）**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2️⃣ 安裝依賴

```bash
pip install -r requirements.txt
```

### 3️⃣ 運行應用

```bash
python app/main.py
```

應用將在 `http://localhost:5000` 啟動

### 4️⃣ 訪問應用

在瀏覽器中打開：
```
http://localhost:5000
```

---

## 🧪 運行測試

**運行所有測試**
```bash
pytest tests/ -v
```

**運行帶覆蓋率的測試**
```bash
pytest tests/ --cov=app --cov-report=html
```

**運行特定測試**
```bash
pytest tests/test_bmi.py::TestBMICalculator::test_normal_calculation -v
```

---

## 📡 API 端點

### 計算 BMI

**端點**: `POST /api/calculate`

**請求示例**
```bash
curl -X POST http://localhost:5000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"height": 170, "weight": 65}'
```

**請求參數**
| 參數 | 類型 | 說明 | 範圍 |
|------|------|------|------|
| height | float | 身高（公分） | 50-250 |
| weight | float | 體重（公斤） | 20-300 |

**成功響應 (200)**
```json
{
  "success": true,
  "bmi": 22.5,
  "category": "正常體重",
  "description": "體重正常，請保持健康生活方式",
  "color": "green"
}
```

**錯誤響應 (400)**
```json
{
  "success": false,
  "error": "身高和體重必須大於0"
}
```

---

## 📚 文檔

詳細文檔位於 `docs/` 目錄：

- [API 文檔](docs/API_DOCUMENTATION.md) - API端點詳細說明
- [開發指南](docs/DEVELOPER_GUIDE.md) - 二/三階段開發說明
- [用戶指南](docs/USER_GUIDE.md) - 使用教程和常見問題

---

## 🔍 BMI 分類標準

| 分類 | BMI 範圍 | 建議 |
|------|---------|------|
| 低體重 | < 18.5 | 增加營養攝取 |
| 正常體重 | 18.5 - 24.9 | 保持健康生活 |
| 過重 | 25.0 - 29.9 | 運動和飲食控制 |
| 肥胖 | ≥ 30.0 | 咨詢醫生 |

---

## 💡 代碼高亮

### 核心計算邏輯
```python
# 在 app/bmi.py 中
BMI_VALUE = WEIGHT_KG / (HEIGHT_M ** 2)
```

### 健康分類邏輯
```python
# 在 app/bmi.py 中，根據BMI值自動分類
if BMI_VALUE < 18.5:
    category = "低體重"
```

---

## 📝 命名規範

本項目遵循以下規範：

- **變數名**：全大寫 + 底線分隔（如 `HEIGHT_CM`, `WEIGHT_KG`）
- **函數名**：蛇形命名（如 `calculate_bmi()`）
- **類別名**：帕斯卡命名（如 `BMICalculator`）
- **註解**：繁體中文

---

## 🔧 技術棧

| 層級 | 技術 |
|------|------|
| 後端 | Flask 2.3.3 |
| 前端 | HTML5 + CSS3 + Vanilla JS |
| 測試 | pytest 7.4.0 |
| 依賴管理 | pip + requirements.txt |
| Python | 3.10+ |

---

## 📋 版本歷史

### v1.0.0 - 基礎版本（當前）
- ✅ 基本BMI計算功能
- ✅ Web界面
- ✅ API端點
- ✅ 單元測試

### v1.1.0 - 優化版本（計劃中）
- 📅 數據持久化（歷史記錄）
- 📅 用戶認證
- 📅 進階統計圖表

### v2.0.0 - 完整版本（計劃中）
- 📅 數據庫集成
- 📅 用戶系統
- 📅 數據分析與可視化

---

## ⚠️ 免責聲明

本計算機僅供參考，**不能代替醫療建議**。  
如有任何健康疑慮，請咨詢專業醫生。

---

## 📧 支持與反饋

如有問題或建議，歡迎反饋！

---

## 📄 許可證

本項目由 GitHub Copilot 產生，供學習和參考使用。

---

**最後更新**: 2026年4月22日  
**作者**: GitHub Copilot
