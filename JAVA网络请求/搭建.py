from flask import Flask, request

app = Flask(__name__)

@app.route("/auth", methods=["post"])
def auth():
    user = request.form.get("user")
    pwd = request.form.get("pwd")

    return "成功了，你他妈真该死啊！"

if __name__ == "__main__":
    app.run(host="192.168.1.10", port="9999")