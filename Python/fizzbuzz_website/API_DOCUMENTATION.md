# FizzBuzz API 文檔

完整的 REST API 參考文檔。

## 目錄

- [基本信息](#基本信息)
- [端點](#端點)
- [請求格式](#請求格式)
- [響應格式](#響應格式)
- [錯誤碼](#錯誤碼)
- [範例](#範例)

## 基本信息

| 項目 | 內容 |
|------|------|
| **基礎 URL** | `http://localhost:5000` |
| **版本** | 1.0 |
| **內容類型** | `application/json` |
| **編碼** | UTF-8 |

## 端點

### 1. 主頁

返回 HTML 用戶界面。

```
GET /
```

**響應**
- 狀態碼: 200
- 內容類型: text/html
- 返回: HTML 頁面

**範例**
```bash
curl http://localhost:5000/
```

---

### 2. FizzBuzz 計算 API

計算單一數字或範圍內的 FizzBuzz 結果。

```
GET /api/fizzbuzz
POST /api/fizzbuzz
```

#### 支援的參數

| 參數 | 類型 | 必需 | 說明 |
|------|------|------|------|
| `number` | 整數 | 否* | 要計算的單一數字 |
| `start` | 整數 | 否** | 範圍的開始（包含） |
| `end` | 整數 | 否** | 範圍的結束（包含） |

\* 計算單一數字時必需
\*\* 計算範圍時兩個都必需

#### 參數限制

| 參數 | 最小值 | 最大值 |
|------|--------|--------|
| `number` | 1 | 1,000,000 |
| `start` | 1 | 1,000,000 |
| `end` | 1 | 1,000,000 |
| `end - start` | - | 10,000 |

#### 響應成功

**狀態碼**: 200

```json
{
  "success": true,
  "result": "FizzBuzz" 或 ["1", "2", "Fizz", ...]
}
```

#### 響應錯誤

**狀態碼**: 400 或 500

```json
{
  "success": false,
  "error": "錯誤信息說明"
}
```

---

## 請求格式

### GET 請求

**URL 參數格式**

```
GET /api/fizzbuzz?parameter1=value1&parameter2=value2
```

**範例**

```bash
curl "http://localhost:5000/api/fizzbuzz?number=15"
curl "http://localhost:5000/api/fizzbuzz?start=1&end=20"
```

### POST 請求

**Content-Type**: `application/json`

**請求體格式**

```json
{
  "number": 15
}
```

或

```json
{
  "start": 1,
  "end": 20
}
```

**範例**

```bash
curl -X POST http://localhost:5000/api/fizzbuzz \
  -H "Content-Type: application/json" \
  -d '{"number": 15}'

curl -X POST http://localhost:5000/api/fizzbuzz \
  -H "Content-Type: application/json" \
  -d '{"start": 1, "end": 20}'
```

---

## 響應格式

### 成功響應

所有成功的請求返回 JSON 對象：

```json
{
  "success": true,
  "result": "計算結果"
}
```

**result 字段的類型**

- **單一數字** (number 參數): 字符串
  - `"Fizz"` - 能被 3 整除
  - `"Buzz"` - 能被 5 整除
  - `"FizzBuzz"` - 能被 15 整除
  - `"1"`, `"2"`, 等 - 普通數字

- **範圍計算** (start 和 end 參數): 字符串數組
  - 例: `["1", "2", "Fizz", "4", "Buzz", ...]`

### 錯誤響應

所有錯誤的請求返回 JSON 對象：

```json
{
  "success": false,
  "error": "詳細的錯誤信息"
}
```

---

## 錯誤碼

| HTTP 狀態碼 | 說明 | 常見原因 |
|-------------|------|---------|
| 200 | OK | 請求成功 |
| 400 | Bad Request | 參數無效、缺少參數、參數超出範圍 |
| 404 | Not Found | 訪問的路由不存在 |
| 500 | Internal Server Error | 伺服器內部錯誤 |

### 常見錯誤信息

| 錯誤信息 | 原因 | 解決方案 |
|---------|------|---------|
| `必須提供 'number' 參數或 'start' 和 'end' 參數` | 缺少必要參數 | 提供 number 或 start/end |
| `數字必須為正整數` | 輸入的數字不是正整數 | 輸入 ≥ 1 的整數 |
| `開始數字不能大於結束數字` | start > end | 確保 start ≤ end |
| `範圍過大，最多支持 10000 個數字` | 範圍超過限制 | 減小範圍大小 |
| `找不到請求的資源` | 404 錯誤 | 檢查 URL 是否正確 |

---

## 範例

### 範例 1: 計算單一 FizzBuzz 數字 (GET)

**請求**
```bash
curl "http://localhost:5000/api/fizzbuzz?number=15"
```

**響應**
```json
{
  "success": true,
  "result": "FizzBuzz"
}
```

### 範例 2: 計算單一 Fizz (GET)

**請求**
```bash
curl "http://localhost:5000/api/fizzbuzz?number=9"
```

**響應**
```json
{
  "success": true,
  "result": "Fizz"
}
```

### 範例 3: 計算普通數字 (GET)

**請求**
```bash
curl "http://localhost:5000/api/fizzbuzz?number=7"
```

**響應**
```json
{
  "success": true,
  "result": "7"
}
```

### 範例 4: 計算範圍 (GET)

**請求**
```bash
curl "http://localhost:5000/api/fizzbuzz?start=1&end=15"
```

**響應**
```json
{
  "success": true,
  "result": [
    "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
    "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"
  ]
}
```

### 範例 5: 使用 POST 計算範圍

**請求**
```bash
curl -X POST http://localhost:5000/api/fizzbuzz \
  -H "Content-Type: application/json" \
  -d '{"start": 10, "end": 20}'
```

**響應**
```json
{
  "success": true,
  "result": [
    "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
    "16", "17", "Fizz", "19", "Buzz"
  ]
}
```

### 範例 6: 錯誤 - 缺少參數

**請求**
```bash
curl "http://localhost:5000/api/fizzbuzz"
```

**響應**
```json
{
  "success": false,
  "error": "必須提供 'number' 參數或 'start' 和 'end' 參數"
}
```

**狀態碼**: 400

### 範例 7: 錯誤 - 無效的數字

**請求**
```bash
curl "http://localhost:5000/api/fizzbuzz?number=abc"
```

**響應**
```json
{
  "success": false,
  "error": "invalid literal for int() with base 10: 'abc'"
}
```

**狀態碼**: 400

### 範例 8: 錯誤 - 範圍過大

**請求**
```bash
curl "http://localhost:5000/api/fizzbuzz?start=1&end=50000"
```

**響應**
```json
{
  "success": false,
  "error": "範圍過大，最多支持 10000 個數字"
}
```

**狀態碼**: 400

---

## 使用建議

### 1. 循序漸進地增加範圍

```bash
# 好的做法：先測試小範圍
curl "http://localhost:5000/api/fizzbuzz?start=1&end=100"

# 然後逐漸增大
curl "http://localhost:5000/api/fizzbuzz?start=1&end=5000"
```

### 2. 錯誤處理

在客戶端代碼中檢查 `success` 字段：

```javascript
const response = await fetch('/api/fizzbuzz?number=15');
const data = await response.json();

if (data.success) {
  console.log('結果:', data.result);
} else {
  console.error('錯誤:', data.error);
}
```

### 3. 性能考慮

- 避免頻繁調用相同的請求
- 考慮在客戶端緩存結果
- 對於大範圍計算，預期回應時間可能更長

---

## 變更日誌

### 版本 1.0 (2026-04-22)

- ✅ 初始版本發布
- ✅ 支援單一數字計算
- ✅ 支援範圍計算
- ✅ GET 和 POST 請求支援
- ✅ 完整的錯誤處理

---

更多問題？查看 [README.md](./README.md) 或 [USER_GUIDE.md](./USER_GUIDE.md)。
