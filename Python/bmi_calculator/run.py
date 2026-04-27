# 由 GitHub Copilot 產生
"""
BMI 計算器應用
計算身體質量指數並提供健康分類建議
"""

from app.main import APP

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=5000)
