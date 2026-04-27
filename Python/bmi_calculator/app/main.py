# 由 GitHub Copilot 產生
"""
Flask應用主入口
提供Web服務和API端點
"""

from flask import Flask, render_template, request, jsonify
from bmi import BMI_CALCULATOR, HEALTH_CLASSIFIER

# 初始化Flask應用
APP = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')


@APP.route('/')
def home():
    """首頁路由，返回主頁面"""
    return render_template('index.html')


@APP.route('/api/calculate', methods=['POST'])
def calculate_bmi():
    """
    API端點：計算BMI
    期望的JSON格式：{"height": 170, "weight": 65}
    """
    try:
        # 獲取請求數據
        DATA = request.get_json()
        HEIGHT_CM = float(DATA.get('height'))
        WEIGHT_KG = float(DATA.get('weight'))
        
        # 計算BMI
        BMI_VALUE = BMI_CALCULATOR.calculate(HEIGHT_CM, WEIGHT_KG)
        
        # 獲取分類
        CLASSIFICATION = HEALTH_CLASSIFIER.classify(BMI_VALUE)
        
        return jsonify({
            "success": True,
            "bmi": BMI_VALUE,
            "category": CLASSIFICATION['category'],
            "description": CLASSIFICATION['description'],
            "color": CLASSIFICATION['color']
        })
    
    except ValueError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "計算出錯：" + str(e)
        }), 500


@APP.route('/api/health', methods=['GET'])
def health_check():
    """健康檢查端點"""
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    # 開發模式啟動
    APP.run(debug=True, host='0.0.0.0', port=5000)
