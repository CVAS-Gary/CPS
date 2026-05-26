#!/bin/bash
# 由 GitHub Copilot 產生
# 根據 docs/task.md 建立 Flask Login API 專案骨架

# 建立專案目錄並進入
mkdir -p flask_login_api && cd flask_login_api && \

# 建立虛擬環境並啟動
python3 -m venv .venv && source .venv/bin/activate && \

# 安裝相依套件
pip install flask pytest && \

# 建立測試目錄
mkdir -p tests && \

# 產生主程式 app.py
cat > app.py << 'EOF'
# 由 GitHub Copilot 產生
from flask import Flask, request, jsonify
import sqlite3

APP = Flask(__name__)

def get_db():
    # 建立資料庫連線
    CONN = sqlite3.connect("users.db")
    CONN.row_factory = sqlite3.Row
    return CONN

def init_db():
    # 初始化資料庫與使用者資料表
    CONN = get_db()
    CONN.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    CONN.commit()
    CONN.close()

@APP.route("/login", methods=["POST"])
def login():
    # 使用參數化查詢防止 SQL Injection
    DATA = request.get_json()
    USERNAME = DATA.get("username")
    PASSWORD = DATA.get("password")
    CONN = get_db()
    ROW = CONN.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (USERNAME, PASSWORD)
    ).fetchone()
    CONN.close()
    if ROW:
        return jsonify({"message": "登入成功"}), 200
    return jsonify({"message": "帳號或密碼錯誤"}), 401

if __name__ == "__main__":
    init_db()
    APP.run(debug=True)
EOF

# 產生測試檔案
cat > tests/test_login.py << 'EOF'
# 由 GitHub Copilot 產生
import pytest
import sqlite3
from app import APP, init_db

@pytest.fixture
def CLIENT():
    APP.config["TESTING"] = True
    with APP.test_client() as C:
        init_db()
        yield C

def test_login_success(CLIENT):
    # 測試登入成功情境
    CONN = sqlite3.connect("users.db")
    CONN.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("admin", "1234"))
    CONN.commit()
    CONN.close()
    RESP = CLIENT.post("/login", json={"username": "admin", "password": "1234"})
    assert RESP.status_code == 200

def test_login_fail(CLIENT):
    # 測試登入失敗情境
    RESP = CLIENT.post("/login", json={"username": "nobody", "password": "wrong"})
    assert RESP.status_code == 401
EOF

# 匯出相依套件清單
pip freeze > requirements.txt

echo "✅ Flask 專案骨架建立完成！"
echo "執行測試：pytest tests/"
