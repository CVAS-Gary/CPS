# 由 GitHub Copilot 產生
# 未引用外部 GitHub 資源

"""簡單資料驗證函式（示範用途）。"""


def validate_add_to_cart_payload(DATA: dict) -> (bool, str):
    """驗證加入購物車的 payload，回傳 (成功, 訊息)。"""
    if not isinstance(DATA, dict):
        return False, "請提供 JSON 物件"
    if "product_id" not in DATA:
        return False, "缺少 product_id"
    if not isinstance(DATA.get("product_id"), int):
        return False, "product_id 必須為整數"
    if not isinstance(DATA.get("quantity", 1), int):
        return False, "quantity 必須是整數"
    if DATA.get("quantity", 1) <= 0:
        return False, "quantity 必須大於 0"
    return True, "OK"


def validate_product_payload(DATA: dict, require_all: bool = True) -> (bool, str):
    """驗證建立或更新商品的 payload。

    Args:
        DATA: 傳入的 JSON 物件。
        require_all: 建立時要求所有欄位，更新時可選。
    """
    if not isinstance(DATA, dict):
        return False, "請提供 JSON 物件"
    if require_all:
        for KEY in ("name", "price", "stock"):
            if KEY not in DATA:
                return False, f"缺少 {KEY}"
    if "name" in DATA and not isinstance(DATA["name"], str):
        return False, "name 必須為字串"
    if "price" in DATA:
        if not (isinstance(DATA["price"], int) or isinstance(DATA["price"], float)):
            return False, "price 必須為數字"
        if DATA["price"] < 0:
            return False, "price 必須大於或等於 0"
    if "stock" in DATA:
        if not isinstance(DATA["stock"], int):
            return False, "stock 必須為整數"
        if DATA["stock"] < 0:
            return False, "stock 必須大於或等於 0"
    return True, "OK"
