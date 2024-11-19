# 基本となるPythonイメージを指定
FROM python:3.11

# 作業ディレクトリを指定
WORKDIR /app

# 必要なPythonパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー
COPY ./src ./src

# コンテナ起動時に実行されるコマンド
CMD ["python", "src/main.py"]
