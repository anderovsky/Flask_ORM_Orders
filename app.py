from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mariadbtest:mariadbtest@mariadb114.r5.websupport.sk:3306/mariadbtest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from customer import Customer
from order import Order
@app.route('/')
def hello_world():  # put application's code here
    return 'Evidencia objednávok v e-shope'

# POSTMAN http://127.0.0.1:5000/customers
@app.route("/customers")
def customers_all():
    customers = Customer.query.all()
    customers_dict = []
    for customer in customers:
        customers_dict.append(customer.dict())
    return jsonify(customers_dict)

@app.route("/orders")
def orders_all():
    orders = Order.query.all()
    orders_dict = []
    for order in orders:
        orders_dict.append(order.dict())
    return jsonify(orders_dict)

if __name__ == '__main__':
    app.run()
