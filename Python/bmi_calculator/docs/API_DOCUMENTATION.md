# API 文檔 - BMI 計算器

## 概述

本文檔詳細說明 BMI 計算器 Web 應用的所有 API 端點。

**基礎 URL**: `http://localhost:5000`  
**內容類型**: `application/json`

---

## 端點列表

| 方法 | 端點 | 說明 |
|------|------|------|
| GET | `/` | 首頁（HTML頁面） |
| POST | `/api/calculate` | 計算BMI |
| GET | `/api/health` | 健康檢查 |

---

## 詳細端點說明

### 1. 計算 BMI

#### 請求

```
POST /api/calculate
Content-Type: application/json
```

**參數**

| 參數 | 類型 | 必需 | 範圍 | 說明 |
|------|------|------|------|------|
| height | float | ✅ | 50-250 | 身高（公分） |
| weight | float | ✅ | 20-300 | 體重（公斤） |

**示例請求**

```bash
curl -X POST http://localhost:5000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "height": 170,
    "weight": 65
  }'
```

**JavaScript 示例**

```javascript
const response = await fetch('/api/calculate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    height: 170,
    weight: 65
  })
});

const data = await response.json();
console.log(data);
```

#### 響應

**成功 (200 OK)**

```json
{
  "success": true,
  "bmi": 22.5,
  "category": "正常體重",
  "description": "體重正常，請保持健康生活方式",
  "color": "green"
}
```

**參數說明**

| 字段 | 類型 | 說明 |
|------|------|------|
| success | boolean | 操作是否成功 |
| bmi | float | 計算的BMI值 |
| category | string | 健康分類 |
| description | string | 健康建議 |
| color | string | UI顏色代碼 |

**錯誤 (400 Bad Request)**

```json
{
  "success": false,
  "error": "身高和體重必須大於0"
}
```

**服務器錯誤 (500 Internal Server Error)**

```json
{
  "success": false,
  "error": "計算出錯：[錯誤詳情]"
}
```

---

### 2. 健康檢查

#### 請求

```
GET /api/health
```

#### 響應

**成功 (200 OK)**

```json
{
  "status": "ok"
}
```

---

## 健康分類定義

| 分類 | BMI 範圍 | color 值 | 說明 |
|------|---------|----------|------|
| 低體重 | < 18.5 | blue | 體重過輕，建議增加營養攝取 |
| 正常體重 | 18.5-24.9 | green | 體重正常，請保持健康生活方式 |
| 過重 | 25.0-29.9 | orange | 體重超標，建議適度運動和飲食控制 |
| 肥胖 | ≥ 30.0 | red | 體重明顯超標，強烈建議就醫諮詢 |

---

## 錯誤代碼

| 狀態碼 | 說明 |
|--------|------|
| 200 | 請求成功 |
| 400 | 請求參數錯誤（無效輸入） |
| 500 | 服務器內部錯誤 |

---

## 常見問題

### Q1: BMI 的計算公式是什麼？

**答**: BMI = 體重(kg) / 身高(m)²

例如：身高 170cm，體重 65kg
- 身高轉換為米：170 ÷ 100 = 1.7m
- BMI = 65 ÷ (1.7²) = 65 ÷ 2.89 = 22.49 ≈ 22.5

### Q2: 支援小數點輸入嗎？

**答**: 支援。體重可以輸入 65.5 等小數值，身高通常輸入整數。

### Q3: 有速率限制嗎？

**答**: 基礎版本沒有速率限制。未來版本將添加。

### Q4: 數據會被保存嗎？

**答**: 基礎版本不保存數據，計算結果僅在當前會話內有效。v1.1.0 版本將添加持久化功能。

### Q5: API 是否支援 CORS？

**答**: 基礎版本在同域內工作。需要跨域支援時，在未來版本中添加。

---

## 使用示例

### Python 示例

```python
import requests

URL = 'http://localhost:5000/api/calculate'
PAYLOAD = {
    'height': 170,
    'weight': 65
}

response = requests.post(URL, json=PAYLOAD)
data = response.json()

if data['success']:
    print(f"BMI: {data['bmi']}")
    print(f"分類: {data['category']}")
    print(f"建議: {data['description']}")
else:
    print(f"錯誤: {data['error']}")
```

### HTML 表單示例

```html
<form id="bmiForm">
  <input type="number" id="height" placeholder="身高（公分）">
  <input type="number" id="weight" placeholder="體重（公斤）">
  <button type="submit">計算</button>
</form>

<div id="result"></div>

<script>
document.getElementById('bmiForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const response = await fetch('/api/calculate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      height: parseFloat(document.getElementById('height').value),
      weight: parseFloat(document.getElementById('weight').value)
    })
  });
  
  const data = await response.json();
  document.getElementById('result').textContent = 
    `BMI: ${data.bmi} - ${data.category}`;
});
</script>
```

---

## 版本更新日誌

### v1.0.0（當前）
- 基礎 API 實現
- BMI 計算和分類
- 輸入驗證

---

**最後更新**: 2026年4月22日
