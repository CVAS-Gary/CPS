# 由 GitHub Copilot 產生
# 未引用外部 GitHub 資源

"""Flask 應用啟動檔，提供可測試的工廠函式 create_app。"""

from flask import Flask
from typing import Optional, Dict
from demo.routes import register_routes


def create_app(config: Optional[Dict] = None):
    """建立並回傳 Flask 應用實例（工廠函式）。

    Args:
        config: 可選的設定字典。
    """
    APP = Flask(__name__)
    if config:
        APP.config.update(config)
    register_routes(APP)
    return APP


# 建立預設模組等級的 APP 物件，供現有測試或直接執行使用。
APP = create_app()


if __name__ == "__main__":
    APP.run(debug=True)
