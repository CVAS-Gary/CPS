# Demo：簡易 Python 購物 API
# Demo：簡易 Python 購物 API

此範例在 `demo/` 下提供一個簡單的 Flask REST API，包含商品查詢、商品 CRUD、購物車管理與結帳流程。

快速開始：

1. 建議建立並啟用虛擬環境

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. 啟動應用

   ```powershell
   .venv\Scripts\python.exe -m demo.app
   ```

3. 執行測試

   ```powershell
   .venv\Scripts\python.exe -m pytest demo -q
   ```

API 路由（摘要）：

- `GET /products` - 取得商品清單
- `POST /products` - 新增商品，JSON: {"name":str, "price":number, "stock":int}
- `GET /products/<id>` - 取得單一商品
- `PUT /products/<id>` - 更新商品，JSON 可包含任意欄位 {"name","price","stock"}
- `DELETE /products/<id>` - 刪除商品
- `GET /cart/<user_id>` - 取得購物車
- `POST /cart/<user_id>` - 加入購物車，JSON: {"product_id":int, "quantity":int}
- `DELETE /cart/<user_id>` - 從購物車刪除，JSON: {"product_id":int}
- `POST /checkout/<user_id>` - 結帳

範例請求 (curl)：

```bash
curl -X POST http://localhost:5000/products -H "Content-Type: application/json" -d '{"name":"梨子","price":8.5,"stock":30}'
curl -X POST http://localhost:5000/cart/testuser -H "Content-Type: application/json" -d '{"product_id":1,"quantity":2}'
curl -X POST http://localhost:5000/checkout/testuser
```

上述變更包括：新增商品 CRUD 路由、驗證、及測試。
