from flask import Flask, render_template
from service.calculation import CalculationService

app = Flask(__name__)

calculation_service = CalculationService()

@app.route('/')
def index():
    # 各画面遷移用のルートと名前
    routes = [
        {"name": "計算処理", "path": "/calculation"}
    ]
    # テンプレートに値を渡す
    return render_template("index.html", routes=routes)

@app.route('/calculation')
def calculation():
    # サービスから文字列を取得
    output = calculation_service.get_output()
    # テンプレートに値を渡す
    return render_template("output.html", output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
