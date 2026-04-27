# 開發指南 - BMI 計算器

## 概述

本指南涵蓋項目的開發流程、三個版本的實現細節和最佳實踐。

---

## 開發階段概述

本項目分為三個階段：

### 📌 第一階段：基礎版本 v1.0.0 ✅（已完成）

**目標**: 實現核心功能，可正常運行

**已實現的功能**
- ✅ BMI 計算核心邏輯
- ✅ 健康分類系統
- ✅ Flask Web 應用框架
- ✅ 響應式 Web UI
- ✅ RESTful API 端點
- ✅ 單元測試框架

**代碼結構**
```
bmi.py          - 計算和分類邏輯（兩個獨立類別）
main.py         - Flask 應用和路由（三個端點）
templates/      - 基礎 HTML（一個模板）
static/         - CSS 和 JavaScript（基礎樣式）
tests/          - 16 個單元測試
```

**測試覆蓋率**: ~90%

---

### 📌 第二階段：優化版本 v1.1.0 （計劃中）

**改進方向**
1. **數據持久化**
   - 添加 SQLite 數據庫
   - 保存計算歷史記錄
   - 用戶統計功能

2. **代碼結構優化**
   - 分離 models 和 services
   - 引入 database manager
   - 增強錯誤處理

3. **功能擴展**
   - 批量計算
   - 數據導出（CSV）
   - 計算歷史查詢

4. **性能優化**
   - 結果緩存
   - 數據庫索引
   - 前端資源優化

**新增模組**
```
app/
├── models.py         # 數據模型
├── database.py       # 數據庫管理器
└── services.py       # 業務邏輯層
```

**測試擴展**
- 數據庫操作測試
- 集成測試
- 性能基準測試

---

### 📌 第三階段：完整版本 v2.0.0 （計劃中）

**大規模功能**
1. **用戶系統**
   - 用戶註冊和登錄
   - 個人信息管理
   - 數據隱私保護

2. **高級分析**
   - 趨勢圖表
   - 月度/年度對比
   - 健康建議生成

3. **社交功能**
   - 目標分享
   - 進度追蹤
   - 社群互動

4. **移動優化**
   - 原生移動應用（考慮）
   - PWA 技術應用
   - 離線功能

---

## 版本對比表

| 功能 | v1.0.0 | v1.1.0 | v2.0.0 |
|------|--------|--------|--------|
| 基礎計算 | ✅ | ✅ | ✅ |
| Web UI | ✅ | ✅ | ✅ |
| API | ✅ | ✅ | ✅ |
| 歷史記錄 | ❌ | ✅ | ✅ |
| 數據庫 | ❌ | ✅ | ✅ |
| 用戶系統 | ❌ | ❌ | ✅ |
| 圖表分析 | ❌ | ⚡ | ✅ |
| 移動應用 | ❌ | ❌ | 📅 |

---

## 核心模組詳解

### 1. BMI 計算模組 (app/bmi.py)

```python
class BMI_CALCULATOR:
    """負責 BMI 值的計算"""
    
    @staticmethod
    def calculate(HEIGHT_CM, WEIGHT_KG):
        # 輸入驗證
        # BMI = 體重 / (身高²)
        # 返回保留一位小數的結果
```

**特點**
- 靜態方法設計，無狀態
- 完整的輸入驗證
- 單一職責原則

### 2. 健康分類模組 (app/bmi.py)

```python
class HEALTH_CLASSIFIER:
    """負責健康分類和建議"""
    
    @staticmethod
    def classify(BMI_VALUE):
        # 根據 BMI 值返回分類信息
        # 包含：分類、描述、顏色
```

**特點**
- 配置驅動的分類標準
- 包含視覺化顏色信息
- 提供健康建議文案

### 3. Flask 應用 (app/main.py)

```python
@APP.route('/', methods=['GET'])
def home():
    # 返回主頁

@APP.route('/api/calculate', methods=['POST'])
def calculate_bmi():
    # API 核心端點
    # 接收 JSON → 計算 → 返回結果

@APP.route('/api/health', methods=['GET'])
def health_check():
    # 服務監控端點
```

**特點**
- 簡潔的路由設計
- 完整的錯誤處理
- JSON 請求/響應

---

## 編碼規範

### 命名約定

```python
# 常數和全局變數：大寫 + 底線
HEIGHT_CM = 170
WEIGHT_KG = 65
MAX_HEIGHT = 250

# 函數和方法：蛇形命名
def calculate_bmi(height, weight):
    pass

# 類別：帕斯卡命名
class BMICalculator:
    pass

# 本地變數：蛇形命名
result_value = calculate_bmi(170, 65)
```

### 註解規範

```python
# ✅ 好的註解 - 解釋 WHY
# 轉換身高單位，因為公式需要米為單位
HEIGHT_M = HEIGHT_CM / 100

# ❌ 不好的註解 - 只描述 WHAT
# HEIGHT_M = HEIGHT_CM / 100  # 計算 HEIGHT_M
```

### 代碼結構

```python
# 模組級別的常數
CLASSIFY_STANDARDS = {
    'underweight': (0, 18.5),
    'normal': (18.5, 24.9),
    ...
}

# 類別
class BMICalculator:
    """主要類別說明"""
    
    @staticmethod
    def calculate(...):
        """方法說明"""
        # 實現

    def helper_method(self):
        """輔助方法"""
        pass

# 模組函數
def utility_function():
    """實用函數"""
    pass
```

---

## 測試策略

### 測試金字塔

```
        /\
       /  \  端到端測試 (E2E)
      /____\
     /      \
    /        \ 集成測試
   /________\
  /          \
 /            \ 單元測試
/_____________\
```

### 測試覆蓋目標

- **單元測試**: > 85% 覆蓋率
- **集成測試**: 主要流程全覆蓋
- **E2E 測試**: 關鍵用戶場景

### 運行測試命令

```bash
# 基礎運行
pytest tests/ -v

# 帶覆蓋率
pytest tests/ --cov=app --cov-report=html

# 運行特定測試
pytest tests/test_bmi.py::TestBMICalculator -v

# 運行並停在第一個失敗
pytest tests/ -x

# 顯示最慢的 10 個測試
pytest tests/ --durations=10
```

---

## 性能考量

### v1.0.0 性能指標

| 指標 | 目標 | 實際 |
|------|------|------|
| 計算耗時 | < 1ms | ~0.1ms |
| API 響應 | < 100ms | ~50ms |
| 首頁加載 | < 2s | ~1.5s |

### 優化機會

- **緩存**: 熱門數據緩存
- **數據庫**: 索引優化（v1.1.0+）
- **前端**: 資源壓縮和懶加載

---

## 安全考量

### 當前版本

- ✅ 輸入驗證（範圍檢查）
- ✅ 類型檢查
- ✅ 錯誤消息不洩露內部詳情

### 未來版本計劃

- 📅 HTTPS 強制
- 📅 CSRF 保護
- 📅 SQL 注入防護（數據庫添加後）
- 📅 速率限制
- 📅 身份認證

---

## 依賴管理

### 當前依賴

```txt
Flask==2.3.3          # Web 框架
Werkzeug==2.3.7       # WSGI 工具集
pytest==7.4.0         # 測試框架
pytest-cov==4.1.0     # 覆蓋率報告
```

### 版本升級建議

- 定期檢查安全補丁
- 運行 `pip list --outdated`
- 測試後再升級依賴

---

## 常見開發任務

### 添加新的 API 端點

```python
@APP.route('/api/new-endpoint', methods=['GET', 'POST'])
def new_endpoint():
    """新端點實現"""
    try:
        # 業務邏輯
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

### 添加新的健康分類標準

編輯 `bmi.py` 中的 `classify()` 方法：

```python
if BMI_VALUE < NEW_THRESHOLD:
    return {
        "category": "新分類",
        "description": "新描述",
        "color": "新顏色"
    }
```

### 添加新的測試

```python
def test_new_feature():
    """測試新功能"""
    RESULT = FUNCTION_TO_TEST(params)
    assert RESULT == EXPECTED
```

---

## 版本發布檢查清單

### 發布前檢查

- [ ] 所有測試通過 (`pytest tests/ -v`)
- [ ] 代碼覆蓋率達標（> 85%）
- [ ] 無 linting 錯誤 (`flake8 app/`)
- [ ] 代碼格式正確 (`black app/`)
- [ ] 文檔已更新
- [ ] 版本號已更新
- [ ] CHANGELOG 已更新
- [ ] 無調試代碼遺留

### 發布步驟

1. 更新 `README.md` 版本號
2. 添加 `CHANGELOG.md` 條目
3. 運行完整測試套件
4. 提交代碼並標記版本
5. 部署到生產環境

---

## 故障排查

### 常見問題

**Q: Flask 應用無法啟動**
```bash
# 檢查端口是否被占用
netstat -ano | findstr :5000

# 使用不同端口
python app/main.py --port 5001
```

**Q: 測試失敗**
```bash
# 運行詳細模式
pytest tests/ -vv

# 查看完整追溯
pytest tests/ --tb=long
```

---

## 參考資源

- [Flask 官方文檔](https://flask.palletsprojects.com/)
- [pytest 使用指南](https://docs.pytest.org/)
- [Python 編碼規範 PEP 8](https://www.python.org/dev/peps/pep-0008/)

---

**最後更新**: 2026年4月22日
