# 由 GitHub Copilot 產生
# 未參考任何 GitHub 原始碼
import os
import secrets
from datetime import datetime, timezone

import pyodbc
from flask import Flask, jsonify, request
from werkzeug.security import check_password_hash

APP = Flask(__name__)

DB_SERVER = os.getenv("DB_SERVER", "localhost")
DB_NAME = os.getenv("DB_NAME", "APP_DB")
DB_USER = os.getenv("DB_USER", "sa")
DB_PASSWORD = os.getenv("DB_PASSWORD", "YourStrong!Passw0rd")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")


def get_connection():
    CONNECTION_STRING = (
        f"DRIVER={{{DB_DRIVER}}};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_NAME};"
        f"UID={DB_USER};"
        f"PWD={DB_PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(CONNECTION_STRING)


@APP.post("/api/login")
def login():
    DATA = request.get_json(silent=True) or {}
    USERNAME = (DATA.get("username") or "").strip()
    PASSWORD = DATA.get("password") or ""

    if not USERNAME or not PASSWORD:
        return jsonify({"message": "username 與 password 為必填"}), 400

    SQL = """
        SELECT USER_ID, USERNAME, PASSWORD_HASH, IS_ACTIVE
        FROM USERS
        WHERE USERNAME = ?
    """

    try:
        with get_connection() as CONN:
            CURSOR = CONN.cursor()
            CURSOR.execute(SQL, USERNAME)
            ROW = CURSOR.fetchone()
    except pyodbc.Error:
        return jsonify({"message": "資料庫連線或查詢失敗"}), 500

    if ROW is None:
        return jsonify({"message": "帳號或密碼錯誤"}), 401

    USER_ID = ROW[0]
    DB_USERNAME = ROW[1]
    PASSWORD_HASH = ROW[2]
    IS_ACTIVE = ROW[3]

    if not IS_ACTIVE:
        return jsonify({"message": "帳號已停用"}), 403

    if not check_password_hash(PASSWORD_HASH, PASSWORD):
        return jsonify({"message": "帳號或密碼錯誤"}), 401

    ACCESS_TOKEN = secrets.token_urlsafe(32)
    NOW_ISO = datetime.now(timezone.utc).isoformat()

    return (
        jsonify(
            {
                "message": "登入成功",
                "user": {"user_id": USER_ID, "username": DB_USERNAME},
                "access_token": ACCESS_TOKEN,
                "issued_at": NOW_ISO,
            }
        ),
        200,
    )


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000, debug=True)