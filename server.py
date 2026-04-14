from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

balance = 1000

@app.route("/balance", methods=["GET"])
def get_balance():
    return jsonify({"balance": balance})

@app.route("/deposit", methods=["POST"])
def deposit():
    global balance
    data = request.json
    amount = data.get("amount", 0)

    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    balance += amount
    return jsonify({"balance": balance})

@app.route("/withdraw", methods=["POST"])
def withdraw():
    global balance
    data = request.json
    amount = data.get("amount", 0)

    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    if amount > balance:
        return jsonify({"error": "Insufficient funds"}), 400

    balance -= amount
    return jsonify({"balance": balance})

if __name__ == "__main__":
    app.run(debug=True)