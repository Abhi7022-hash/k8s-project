from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/api/products", methods=["GET"])
def get_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return jsonify(products)

@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (data["name"], data["price"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Product added"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
