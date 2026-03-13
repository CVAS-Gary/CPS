# 由 GitHub Copilot 產生
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Python 計算機網站</h1><p>請使用 /calculate 端點進行計算。</p>"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    if not all([operation, isinstance(num1, (int, float)), isinstance(num2, (int, float))]):
        return jsonify({"error": "請提供有效的 operation, num1 和 num2"}), 400

    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({"error": "除數不能為零"}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "不支持的操作"}), 400

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)