# Inventory Management API

A simple REST API built using **Python Flask** and **SQLAlchemy** to manage product inventory.

## Features

- Add products
- View all products
- Update product details
- Delete products
- Search products by name
- Calculate total inventory value

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite

## API Endpoints

### Get all products

GET /products

### Add product

POST /products

Example request:

{
"name": "Laptop",
"price": 50000
}

### Update product

PUT /products/<id>

### Delete product

DELETE /products/<id>

### Search product

GET /products/search?name=Phone

### Total inventory value

GET /inventory/value

## Running Locally

1. Clone the repository

git clone https://github.com/yourusername/inventory-api.git

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

## Author

Hafizur Rahaman