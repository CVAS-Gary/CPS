# 由 GitHub Copilot 產生
# 未引用外部 GitHub 資源

"""定義 API 路由並註冊到 Flask 應用上。"""

from flask import request, jsonify
from demo.models import (
    get_products,
    get_product,
    create_product,
    update_product,
    delete_product,
    add_to_cart,
    remove_from_cart,
    get_cart,
    checkout,
)
from demo.schemas import validate_add_to_cart_payload, validate_product_payload


def register_routes(APP):
    """將所有路由註冊到 `APP`。"""

    @APP.route("/products", methods=["GET"])
    def products_list():
        return jsonify(get_products())

    @APP.route("/products", methods=["POST"])
    def products_create():
        DATA = request.get_json() or {}
        OK, MSG = validate_product_payload(DATA, require_all=True)
        if not OK:
            return jsonify({"error": MSG}), 400
        NEW = create_product(NAME=DATA["name"], PRICE=DATA["price"], STOCK=DATA["stock"])
        return jsonify(NEW), 201

    @APP.route("/products/<int:product_id>", methods=["GET"])
    def product_detail(product_id):
        PRODUCT = get_product(product_id)
        if not PRODUCT:
            return jsonify({"error": "商品不存在"}), 404
        return jsonify(PRODUCT)

    @APP.route("/products/<int:product_id>", methods=["PUT"])
    def product_update(product_id):
        DATA = request.get_json() or {}
        OK, MSG = validate_product_payload(DATA, require_all=False)
        if not OK:
            return jsonify({"error": MSG}), 400
        UPDATED = update_product(product_id, NAME=DATA.get("name"), PRICE=DATA.get("price"), STOCK=DATA.get("stock"))
        if not UPDATED:
            return jsonify({"error": "商品不存在"}), 404
        return jsonify(UPDATED)

    @APP.route("/products/<int:product_id>", methods=["DELETE"])
    def product_delete(product_id):
        OK = delete_product(product_id)
        if not OK:
            return jsonify({"error": "商品不存在"}), 404
        return jsonify({"message": "已刪除商品"})

    @APP.route("/cart/<string:user_id>", methods=["GET"])
    def cart_get(user_id):
        return jsonify(get_cart(user_id))

    @APP.route("/cart/<string:user_id>", methods=["POST"])
    def cart_add(user_id):
        DATA = request.get_json() or {}
        OK, MSG = validate_add_to_cart_payload(DATA)
        if not OK:
            return jsonify({"error": MSG}), 400
        PRODUCT_ID = DATA.get("product_id")
        QUANTITY = DATA.get("quantity", 1)
        OK2, MSG2 = add_to_cart(user_id, PRODUCT_ID, QUANTITY)
        if not OK2:
            return jsonify({"error": MSG2}), 400
        return jsonify({"message": MSG2})

    @APP.route("/cart/<string:user_id>", methods=["DELETE"])
    def cart_remove(user_id):
        DATA = request.get_json() or {}
        PRODUCT_ID = DATA.get("product_id")
        OK, MSG = remove_from_cart(user_id, PRODUCT_ID)
        if not OK:
            return jsonify({"error": MSG}), 400
        return jsonify({"message": MSG})

    @APP.route("/checkout/<string:user_id>", methods=["POST"])
    def do_checkout(user_id):
        OK, RESULT = checkout(user_id)
        if not OK:
            return jsonify({"error": RESULT}), 400
        return jsonify(RESULT)
