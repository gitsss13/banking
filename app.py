from flask import Flask, jsonify, request

app = Flask(__name__)

account = {
    "balance": 1000.0,
    "version": "v1"
}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "version": account["version"]})

@app.route("/balance", methods=["GET"])
def check_balance():
    return jsonify({"balance": round(account["balance"], 2), "version": account["version"]})

@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.get_json() or {}
    amount = float(data.get("amount", 0))

    if amount <= 0:
        return jsonify({"error": "Deposit amount must be greater than zero."}), 400

    account["balance"] += amount
    return jsonify({
        "message": "Deposit successful",
        "balance": round(account["balance"], 2),
        "version": account["version"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)