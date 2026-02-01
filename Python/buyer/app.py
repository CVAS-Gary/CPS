# 由 GitHub Copilot 產生
# 本檔案未參考任何 GitHub 原始碼

"""
專案初始化說明：
- 這是 buyer 網站專案的主程式入口。
- 請根據需求擴充 Flask 應用程式。
"""

from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def index():
    return 'Buyer 網站首頁'

if __name__ == '__main__':
    APP.run(debug=True)
