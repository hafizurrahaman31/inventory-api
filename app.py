from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Inventory API is running"


@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])


@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()

    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "name and price are required"}), 400

    product = Product(name=data["name"], price=data["price"])
    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product added"})


@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    product.name = data["name"]
    product.price = data["price"]

    db.session.commit()

    return jsonify({"message": "Product updated"})


@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted"})


@app.route("/products/search", methods=["GET"])
def search_product():
    name = request.args.get("name")
    products = Product.query.filter(Product.name.contains(name)).all()

    return jsonify([p.to_dict() for p in products])


@app.route("/inventory/value", methods=["GET"])
def inventory_value():
    products = Product.query.all()
    total = sum(p.price for p in products)

    return jsonify({"total_inventory_value": total})



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)