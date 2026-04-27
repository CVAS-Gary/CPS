# 項目結構說明 - BMI 計算器

## 目錄結構

```
bmi_calculator/                    # 項目根目錄
│
├── app/                           # 應用程式代碼
│   ├── __init__.py               # 應用初始化模組
│   ├── bmi.py                    # BMI計算和分類邏輯
│   └── main.py                   # Flask應用主入口
│
├── templates/                     # HTML模板目錄
│   └── index.html                # 主頁面模板
│
├── static/                        # 靜態資源目錄
│   ├── style.css                 # 樣式表（CSS）
│   └── script.js                 # 前端邏輯（JavaScript）
│
├── tests/                         # 測試目錄
│   ├── __init__.py               # 測試模組初始化
│   └── test_bmi.py               # BMI計算測試
│
├── docs/                          # 文檔目錄
│   ├── API_DOCUMENTATION.md      # API端點文檔
│   ├── DEVELOPER_GUIDE.md        # 開發指南和版本規劃
│   └── USER_GUIDE.md             # 用戶使用指南
│
├── README.md                      # 項目主README（快速開始）
├── run.py                         # 應用啟動腳本
├── requirements.txt               # 依賴清單
├── .gitignore                     # Git忽略文件
└── STRUCTURE.md                   # 本文件（目錄結構說明）
```

---

## 各目錄詳解

### 📁 app/ - 應用程式核心

| 文件 | 說明 | 責責任 |
|------|------|--------|
| `__init__.py` | 包初始化 | 包標識 |
| `bmi.py` | BMI計算模組 | BMI計算和健康分類 |
| `main.py` | Flask應用 | Web服務和API路由 |

**依賴關係**
```
main.py → imports bmi.py → BMI_CALCULATOR, HEALTH_CLASSIFIER
```

---

### 📁 templates/ - HTML模板

| 文件 | 說明 | 功能 |
|------|------|------|
| `index.html` | 主頁面 | 表單和結果顯示 |

**模板語言**: Jinja2（Flask內置）  
**特點**: 使用 `{{ url_for() }}` 動態加載靜態資源

---

### 📁 static/ - 前端資源

| 文件 | 類型 | 功能 |
|------|------|------|
| `style.css` | 樣式表 | 頁面美化和響應式設計 |
| `script.js` | JavaScript | 表單驗證和API交互 |

**加載順序**
1. HTML加載（index.html）
2. CSS應用樣式（style.css）
3. JavaScript添加交互（script.js）

---

### 📁 tests/ - 測試套件

| 文件 | 說明 | 測試數量 |
|------|------|---------|
| `__init__.py` | 包初始化 | - |
| `test_bmi.py` | BMI測試 | 16個測試 |

**測試類別**
- `TestBMICalculator` - 計算邏輯測試
- `TestHealthClassifier` - 分類邏輯測試

**測試涵蓋**
- 正常計算
- 邊界值檢驗
- 異常輸入處理

---

### 📁 docs/ - 文檔目錄

| 文件 | 受眾 | 內容 |
|------|------|------|
| `API_DOCUMENTATION.md` | 開發者 | API端點、參數、響應 |
| `DEVELOPER_GUIDE.md` | 開發者 | 版本規劃、架構、編碼規範 |
| `USER_GUIDE.md` | 終端用戶 | 使用教程、FAQ、健康建議 |

---

## 文件依賴圖

```
┌─ main.py ─┐
│           └──→ bmi.py
│               ├── BMI_CALCULATOR
│               └── HEALTH_CLASSIFIER
│
├─ templates/index.html
│   ├── 加載 static/style.css
│   └── 加載 static/script.js
│
└─ script.js
    └── 發送 POST /api/calculate
        └── 接收 main.py 的響應
```

---

## 數據流

### 用戶操作流程

```
1. 用戶打開頁面
   └→ GET / 
      └→ Flask返回 templates/index.html

2. 用戶填寫表單並提交
   └→ script.js 監聽表單提交
      └→ 客戶端驗證輸入
         └→ AJAX POST /api/calculate
            └→ main.py 接收請求

3. 後端計算
   └→ main.py 調用 bmi.py
      ├─ BMI_CALCULATOR.calculate()
      └─ HEALTH_CLASSIFIER.classify()

4. 返回結果
   └→ main.py 返回 JSON
      └→ script.js 解析並顯示
         └→ 用戶看到結果
```

---

## 模組責任

### bmi.py (計算模組)
- ✅ 計算 BMI 值
- ✅ 分類健康狀況
- ✅ 驗證輸入

**無責任**
- ❌ 不處理HTTP請求
- ❌ 不管理數據庫
- ❌ 不處理前端邏輯

### main.py (應用模組)
- ✅ 定義路由
- ✅ 處理HTTP請求
- ✅ 錯誤處理
- ✅ 調用業務邏輯

**無責任**
- ❌ 不進行計算邏輯
- ❌ 不處理UI展示

### 前端 (HTML/CSS/JS)
- ✅ 用戶界面
- ✅ 表單驗證
- ✅ API調用

**無責任**
- ❌ 不進行複雜計算
- ❌ 不存儲敏感數據

---

## 版本演進

### v1.0.0 (當前)
```
bmi_calculator/
├── app/
│   ├── bmi.py
│   └── main.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── tests/
    └── test_bmi.py
```

### v1.1.0 (計劃中)
```
bmi_calculator/
├── app/
│   ├── bmi.py
│   ├── main.py
│   ├── database.py      ← 新增
│   ├── models.py        ← 新增
│   └── services.py      ← 新增
├── templates/
│   ├── index.html
│   └── history.html     ← 新增
└── tests/
    ├── test_bmi.py
    ├── test_database.py ← 新增
    └── test_api.py      ← 新增
```

---

## 編碼標準一致性

### 命名慣例

```
✓ 變數: UPPERCASE_WITH_UNDERSCORE
✓ 函數: snake_case
✓ 類別: PascalCase
✓ 常數: UPPERCASE_WITH_UNDERSCORE
✓ 私有: _leading_underscore
✓ 魔法: __double_underscore__
```

### 文件命名

```
✓ 模組: lowercase_with_underscores.py
✓ 測試: test_module_name.py
✓ HTML: lowercase-with-dash.html
✓ CSS: lowercase-with-dash.css
✓ JS: camelCase.js (通常) 或 snake_case.js
```

---

## 構建和部署

### 本地運行

```bash
# 方式1：直接運行主模組
python app/main.py

# 方式2：使用run.py
python run.py
```

### 生產部署 (計劃)

```bash
# 使用 Gunicorn
gunicorn app:APP

# 使用 uWSGI
uwsgi --http :5000 --wsgi-file app/main.py --callable APP
```

---

## 擴展性設計

### 添加新功能

1. **新計算類別**
   ```
   app/calculators/
   ├── bmi_calculator.py
   ├── body_fat_calculator.py    ← 新增
   └── __init__.py
   ```

2. **新路由**
   ```python
   # 在 main.py 中添加
   @APP.route('/api/body-fat', methods=['POST'])
   def calculate_body_fat():
       ...
   ```

3. **新測試**
   ```
   tests/
   ├── test_bmi.py
   └── test_body_fat.py          ← 新增
   ```

---

## 質量指標

| 指標 | v1.0.0 | 目標 |
|------|--------|------|
| 測試覆蓋率 | 90% | > 85% |
| 代碼行數 | ~400 | 精簡 |
| 模組數 | 3 | 管理 |
| 文檔頁數 | 4 | 完整 |

---

**更新日期**: 2026年4月22日  
**版本**: v1.0.0
