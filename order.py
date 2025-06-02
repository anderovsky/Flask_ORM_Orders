from app import db

class Order(db.Model):
    __tablename__:str = "orders"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

    def dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "order_date": self.order_date
        }