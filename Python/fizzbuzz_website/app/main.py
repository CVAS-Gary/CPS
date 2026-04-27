# 由 GitHub Copilot 產生

from flask import Flask, render_template, request, jsonify
from app.fizzbuzz import fizzbuzz_single, fizzbuzz_range

# 初始化 Flask 應用
APP = Flask(
    __name__, template_folder="../templates", static_folder="../static"
)


@APP.route("/")
def index():
    """
    主頁路由，返回 HTML 界面。

    返回:
        使用者界面的 HTML 頁面
    """
    return render_template("index.html")


@APP.route("/api/fizzbuzz", methods=["GET", "POST"])
def api_fizzbuzz():
    """
    FizzBuzz API 端點，支持單一數字或範圍計算。

    方法:
        GET/POST 參數:
        - number: 單一數字（整數）
        - start: 範圍開始（整數）
        - end: 範圍結束（整數）

    返回:
        JSON 格式的結果或錯誤信息
        成功範例:
            {"success": true, "result": "FizzBuzz"}
            {"success": true, "result": ["Fizz", "Buzz", "FizzBuzz", ...]}
        錯誤範例:
            {"success": false, "error": "錯誤信息"}
    """
    # 從 GET 或 POST 請求中提取參數
    REQUEST_DATA = request.args if request.method == "GET" else request.json
    if REQUEST_DATA is None:
        REQUEST_DATA = {}

    try:
        # 如果提供了單一數字參數
        if "number" in REQUEST_DATA:
            INPUT_NUMBER = int(REQUEST_DATA.get("number"))
            # 驗證輸入範圍
            if INPUT_NUMBER < 1:
                return jsonify({"success": False, "error": "數字必須為正整數"}), 400

            FIZZBUZZ_RESULT = fizzbuzz_single(INPUT_NUMBER)
            return jsonify({"success": True, "result": FIZZBUZZ_RESULT})

        # 如果提供了範圍參數
        elif "start" in REQUEST_DATA and "end" in REQUEST_DATA:
            START_NUMBER = int(REQUEST_DATA.get("start"))
            END_NUMBER = int(REQUEST_DATA.get("end"))

            # 驗證輸入
            if START_NUMBER < 1 or END_NUMBER < 1:
                ERROR_MSG = "開始和結束數字都必須為正整數"
                return jsonify({"success": False, "error": ERROR_MSG}), 400

            if END_NUMBER - START_NUMBER > 10000:
                ERROR_MSG = "範圍過大，最多支持 10000 個數字"
                return jsonify({"success": False, "error": ERROR_MSG}), 400

            FIZZBUZZ_RESULT = fizzbuzz_range(START_NUMBER, END_NUMBER)
            return jsonify({"success": True, "result": FIZZBUZZ_RESULT})

        else:
            # 沒有提供必要參數
            return (
                jsonify(
                    {
                        "success": False,
                        "error": "必須提供 'number' 參數或 'start' 和 'end' 參數",
                    }
                ),
                400,
            )

    except ValueError as VALUE_ERROR:
        # 捕獲值錯誤（如輸入不是整數）
        return jsonify({"success": False, "error": str(VALUE_ERROR)}), 400
    except Exception as GENERAL_ERROR:
        # 捕獲其他異常
        ERROR_MSG = f"伺服器錯誤: {str(GENERAL_ERROR)}"
        return jsonify({"success": False, "error": ERROR_MSG}), 500


@APP.errorhandler(404)
def page_not_found(ERROR):
    """
    處理 404 錯誤的路由。

    參數:
        ERROR: Flask 錯誤對象

    返回:
        JSON 格式的錯誤信息
    """
    return jsonify({"success": False, "error": "找不到請求的資源"}), 404


@APP.errorhandler(500)
def internal_error(ERROR):
    """
    處理 500 錯誤的路由。

    參數:
        ERROR: Flask 錯誤對象

    返回:
        JSON 格式的錯誤信息
    """
    return jsonify({"success": False, "error": "伺服器內部錯誤"}), 500


if __name__ == "__main__":
    # 開發環境下運行 Flask 應用
    APP.run(debug=True, host="0.0.0.0", port=5000)
