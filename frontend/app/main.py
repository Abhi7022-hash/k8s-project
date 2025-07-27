from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_URL = "http://backend-service:5000/api/products"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        requests.post(API_URL, json={"name": name, "price": float(price)})
        return redirect("/")
    products = requests.get(API_URL).json()
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
