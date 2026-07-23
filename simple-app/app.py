from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Simple Web Server!"

@app.route("/first")
def first():
    return {
        "endpoint": "/first",
        "message": "This is the first endpoint"
    }

@app.route("/second")
def second():
    return {
        "endpoint": "/second",
        "message": "This is the second endpoint"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
