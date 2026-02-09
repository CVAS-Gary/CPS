# 由 GitHub Copilot 產生
# 未引用外部 GitHub 資源

"""使用 pytest 的 API 測試案例，覆蓋商品 CRUD、購物車與結帳情境。"""

from demo.app import APP


def test_get_products():
    CLIENT = APP.test_client()
    R = CLIENT.get("/products")
    assert R.status_code == 200
    DATA = R.get_json()
    assert isinstance(DATA, list)


def test_product_crud_and_errors():
    CLIENT = APP.test_client()
    # 建立商品
    R = CLIENT.post("/products", json={"name": "鳳梨", "price": 12.5, "stock": 50})
    assert R.status_code == 201
    NEW = R.get_json()
    NEW_ID = NEW["id"]
    assert NEW["name"] == "鳳梨"

    # 取得商品
    R = CLIENT.get(f"/products/{NEW_ID}")
    assert R.status_code == 200

    # 更新商品
    R = CLIENT.put(f"/products/{NEW_ID}", json={"price": 15.0})
    assert R.status_code == 200
    UPDATED = R.get_json()
    assert UPDATED["price"] == 15.0

    # 刪除商品
    R = CLIENT.delete(f"/products/{NEW_ID}")
    assert R.status_code == 200

    # 刪除不存在的商品
    R = CLIENT.delete(f"/products/{99999}")
    assert R.status_code == 404


def test_cart_and_checkout_flow_and_errors():
    CLIENT = APP.test_client()
    USER_ID = "testuser"
    # 確認商品存在（使用商品 id 1）
    R = CLIENT.get("/products")
    DATA = R.get_json()
    assert len(DATA) >= 1
    EXISTING_ID = DATA[0]["id"]

    # 嘗試加入不存在的商品
    R = CLIENT.post(f"/cart/{USER_ID}", json={"product_id": 999999, "quantity": 1})
    assert R.status_code == 400

    # 嘗試加入庫存過多的商品（以大數量嘗試）
    R = CLIENT.post(f"/cart/{USER_ID}", json={"product_id": EXISTING_ID, "quantity": 999999})
    assert R.status_code == 400

    # 正常加入購物車
    R = CLIENT.post(f"/cart/{USER_ID}", json={"product_id": EXISTING_ID, "quantity": 1})
    assert R.status_code == 200

    # 取得購物車
    R = CLIENT.get(f"/cart/{USER_ID}")
    DATA = R.get_json()
    assert len(DATA) >= 1

    # 結帳成功或失敗取決於庫存，至少回傳 JSON
    R = CLIENT.post(f"/checkout/{USER_ID}")
    assert R.status_code in (200, 400)
