# 由 GitHub Copilot 產生

import pytest
import json
import sys
from pathlib import Path

# 添加父目錄到 Python 路徑，以便導入 app 模塊
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app.main import APP  # noqa: E402


@pytest.fixture
def CLIENT():
    """
    為測試提供 Flask 測試客戶端。

    返回:
        Flask 測試客戶端，可用於發送請求到應用
    """
    APP.config["TESTING"] = True
    with APP.test_client() as TEST_CLIENT:
        yield TEST_CLIENT


class TestAPIRoutes:
    """
    Flask API 路由的單元測試類別。
    """

    def test_index_route(self, CLIENT):
        """測試主頁路由應返回 200 狀態碼"""
        RESPONSE = CLIENT.get("/")
        assert RESPONSE.status_code == 200
        assert b"FizzBuzz" in RESPONSE.data

    def test_api_fizzbuzz_single_number_get(self, CLIENT):
        """測試 API 用 GET 方法計算單一數字"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?number=15")
        assert RESPONSE.status_code == 200

        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is True
        assert DATA["result"] == "FizzBuzz"

    def test_api_fizzbuzz_single_fizz(self, CLIENT):
        """測試 API 計算 Fizz 結果"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?number=3")
        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is True
        assert DATA["result"] == "Fizz"

    def test_api_fizzbuzz_single_buzz(self, CLIENT):
        """測試 API 計算 Buzz 結果"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?number=5")
        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is True
        assert DATA["result"] == "Buzz"

    def test_api_fizzbuzz_single_number(self, CLIENT):
        """測試 API 計算普通數字"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?number=7")
        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is True
        assert DATA["result"] == "7"

    def test_api_fizzbuzz_range_get(self, CLIENT):
        """測試 API 用 GET 方法計算範圍"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?start=1&end=5")
        assert RESPONSE.status_code == 200

        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is True
        EXPECTED_RESULT = ["1", "2", "Fizz", "4", "Buzz"]
        assert DATA["result"] == EXPECTED_RESULT

    def test_api_fizzbuzz_range_1_to_15(self, CLIENT):
        """測試 API 計算 1 到 15 的完整範圍"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?start=1&end=15")
        DATA = json.loads(RESPONSE.data)

        assert DATA["success"] is True
        EXPECTED_RESULT = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]
        assert DATA["result"] == EXPECTED_RESULT

    def test_api_fizzbuzz_single_post(self, CLIENT):
        """測試 API 用 POST 方法計算單一數字"""
        RESPONSE = CLIENT.post(
            "/api/fizzbuzz",
            data=json.dumps({"number": 15}),
            content_type="application/json",
        )
        assert RESPONSE.status_code == 200

        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is True
        assert DATA["result"] == "FizzBuzz"

    def test_api_fizzbuzz_range_post(self, CLIENT):
        """測試 API 用 POST 方法計算範圍"""
        RESPONSE = CLIENT.post(
            "/api/fizzbuzz",
            data=json.dumps({"start": 1, "end": 5}),
            content_type="application/json",
        )
        assert RESPONSE.status_code == 200

        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is True
        EXPECTED_RESULT = ["1", "2", "Fizz", "4", "Buzz"]
        assert DATA["result"] == EXPECTED_RESULT

    def test_api_fizzbuzz_missing_parameters(self, CLIENT):
        """測試 API 缺少必要參數應返回錯誤"""
        RESPONSE = CLIENT.get("/api/fizzbuzz")
        assert RESPONSE.status_code == 400

        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is False
        assert "必須提供" in DATA["error"]

    def test_api_fizzbuzz_invalid_number(self, CLIENT):
        """測試 API 接收非整數應返回錯誤"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?number=abc")
        assert RESPONSE.status_code == 400

        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is False

    def test_api_fizzbuzz_negative_number(self, CLIENT):
        """測試 API 接收負數應返回錯誤"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?number=-5")
        assert RESPONSE.status_code == 400

        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is False
        assert "正整數" in DATA["error"]

    def test_api_fizzbuzz_zero_number(self, CLIENT):
        """測試 API 接收零應返回錯誤"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?number=0")
        assert RESPONSE.status_code == 400

        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is False

    def test_api_fizzbuzz_range_start_greater_than_end(self, CLIENT):
        """測試 API 開始數字大於結束數字應返回錯誤"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?start=10&end=5")
        assert RESPONSE.status_code == 400

        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is False

    def test_api_fizzbuzz_range_too_large(self, CLIENT):
        """測試 API 範圍過大應返回錯誤"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?start=1&end=100000")
        assert RESPONSE.status_code == 400

        DATA = json.loads(RESPONSE.data)
        assert DATA["success"] is False
        assert "範圍過大" in DATA["error"]

    def test_api_fizzbuzz_404_not_found(self, CLIENT):
        """測試訪問不存在的路由應返回 404"""
        RESPONSE = CLIENT.get("/api/nonexistent")
        assert RESPONSE.status_code == 404

    def test_api_response_format(self, CLIENT):
        """測試 API 響應格式是否正確"""
        RESPONSE = CLIENT.get("/api/fizzbuzz?number=15")
        DATA = json.loads(RESPONSE.data)

        # 檢查必要的響應字段
        assert "success" in DATA
        assert "result" in DATA or "error" in DATA
