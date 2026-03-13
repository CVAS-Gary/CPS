# 由 GitHub Copilot 產生
import pytest
from app import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Python 計算機網站" in response.data

def test_calculate_add():
    with app.test_client() as client:
        response = client.post('/calculate', json={"operation": "add", "num1": 5, "num2": 3})
        assert response.status_code == 200
        assert response.json["result"] == 8

def test_calculate_divide_by_zero():
    with app.test_client() as client:
        response = client.post('/calculate', json={"operation": "divide", "num1": 5, "num2": 0})
        assert response.status_code == 400
        assert "除數不能為零" in response.json["error"]

def test_calculate_invalid_operation():
    with app.test_client() as client:
        response = client.post('/calculate', json={"operation": "mod", "num1": 5, "num2": 3})
        assert response.status_code == 400
        assert "不支持的操作" in response.json["error"]