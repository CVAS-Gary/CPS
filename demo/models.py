# 由 GitHub Copilot 產生
# 未引用外部 GitHub 資源

"""資料模型（記憶體儲存）：商品、購物車、訂單。"""

from typing import List, Dict, Optional

# 商品試資料（記憶體）
PRODUCTS: List[Dict] = [
    {"id": 1, "name": "蘋果", "price": 10.0, "stock": 100},
    {"id": 2, "name": "香蕉", "price": 5.0, "stock": 200},
]

PRODUCT_ID_COUNTER = 3

# CARTS: user_id -> list of {product_id, quantity}
CARTS: Dict[str, List[Dict]] = {}

ORDERS: List[Dict] = []
ORDER_ID_COUNTER = 1


def get_products() -> List[Dict]:
    """回傳所有商品（簡單記憶體查詢）。"""
    return PRODUCTS


def get_product(PRODUCT_ID: int) -> Optional[Dict]:
    """以 id 取得商品，找不到回傳 None。"""
    for PRODUCT in PRODUCTS:
        if PRODUCT["id"] == PRODUCT_ID:
            return PRODUCT
    return None


def create_product(NAME: str, PRICE: float, STOCK: int) -> Dict:
    """建立新商品並回傳該商品資料。"""
    global PRODUCT_ID_COUNTER
    NEW_PRODUCT = {"id": PRODUCT_ID_COUNTER, "name": NAME, "price": PRICE, "stock": STOCK}
    PRODUCTS.append(NEW_PRODUCT)
    PRODUCT_ID_COUNTER += 1
    return NEW_PRODUCT


def update_product(PRODUCT_ID: int, NAME: Optional[str] = None, PRICE: Optional[float] = None, STOCK: Optional[int] = None) -> Optional[Dict]:
    """更新指定商品，找不到回傳 None，成功回傳更新後商品。"""
    PRODUCT = get_product(PRODUCT_ID)
    if not PRODUCT:
        return None
    if NAME is not None:
        PRODUCT["name"] = NAME
    if PRICE is not None:
        PRODUCT["price"] = PRICE
    if STOCK is not None:
        PRODUCT["stock"] = STOCK
    return PRODUCT


def delete_product(PRODUCT_ID: int) -> bool:
    """刪除指定商品，成功回傳 True，找不到回傳 False。"""
    global PRODUCTS
    ORIG_LEN = len(PRODUCTS)
    PRODUCTS = [P for P in PRODUCTS if P["id"] != PRODUCT_ID]
    return len(PRODUCTS) != ORIG_LEN


def add_to_cart(USER_ID: str, PRODUCT_ID: int, QUANTITY: int = 1):
    """將商品加入使用者購物車，回傳 (成功, 訊息)。"""
    PRODUCT = get_product(PRODUCT_ID)
    if not PRODUCT:
        return False, "商品不存在"
    if PRODUCT["stock"] < QUANTITY:
        return False, "庫存不足"
    CARTS.setdefault(USER_ID, [])
    for ITEM in CARTS[USER_ID]:
        if ITEM["product_id"] == PRODUCT_ID:
            ITEM["quantity"] += QUANTITY
            break
    else:
        CARTS[USER_ID].append({"product_id": PRODUCT_ID, "quantity": QUANTITY})
    return True, "已加入購物車"


def remove_from_cart(USER_ID: str, PRODUCT_ID: int):
    """從購物車移除商品，回傳 (成功, 訊息)。"""
    if USER_ID not in CARTS:
        return False, "購物車為空"
    CARTS[USER_ID] = [IT for IT in CARTS[USER_ID] if IT["product_id"] != PRODUCT_ID]
    return True, "已移除商品"


def get_cart(USER_ID: str) -> List[Dict]:
    """取得使用者購物車內容。"""
    return CARTS.get(USER_ID, [])


def checkout(USER_ID: str):
    """結帳：檢查庫存、扣庫存、建立訂單，回傳 (成功, 訂單或錯誤訊息)。"""
    global ORDER_ID_COUNTER
    CART = get_cart(USER_ID)
    if not CART:
        return False, "購物車為空"
    TOTAL = 0.0
    for ITEM in CART:
        PRODUCT = get_product(ITEM["product_id"])
        if not PRODUCT or PRODUCT["stock"] < ITEM["quantity"]:
            return False, f"商品 {ITEM['product_id']} 庫存不足或不存在"
        TOTAL += PRODUCT["price"] * ITEM["quantity"]
    # 扣庫存
    for ITEM in CART:
        PRODUCT = get_product(ITEM["product_id"])
        PRODUCT["stock"] -= ITEM["quantity"]
    ORDER = {"id": ORDER_ID_COUNTER, "user_id": USER_ID, "items": CART.copy(), "total": TOTAL}
    ORDERS.append(ORDER)
    ORDER_ID_COUNTER += 1
    CARTS[USER_ID] = []
    return True, ORDER
