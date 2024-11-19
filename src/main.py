from flask import Flask, render_template
from services import StringService

app = Flask(__name__)
string_service = StringService()  # サービスのインスタンスを作成

@app.route('/')
def index():
    # サービスから文字列を取得
    output = string_service.get_output()
    # テンプレートに値を渡す
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
