from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Deploy Serverless está funcionando!"

if __name__ == "__main__":
    app.run(debug=True)