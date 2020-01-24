from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dba.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(60), nullable=False)
    password = db.Column(db.VARCHAR(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.password}')"


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(20), unique=True, nullable=False)
    medicine = db.Column(db.VARCHAR(60), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost_price = db.Column(db.BIGINT, nullable=False)
    sell_price = db.Column(db.BIGINT, nullable=False)
    no_of_goods = db.Column(db.Integer, nullable=False)
    final_price = db.Column(db.BIGINT, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    expire_date = db.Column(db.DateTime, nullable=False)
    buy_date = db.Column(db.DateTime, nullable=False)
    drugstore_name = db.Column(db.VARCHAR(20), nullable=False)
    final_profit = db.Column(db.BIGINT, nullable=False)

    def __repr__(self):
        return f"Activities('{self.medicine}', '{self.quantity}', '{self.expire_date}', '{self.barcode}','{self.cost_price}', '{self.sell_price}', '{self.final_price}', '{self.created_at}', '{self.final_profit}')"


class Expire(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    medicine = db.Column(db.VARCHAR(60), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    no_of_goods = db.Column(db.Integer, nullable=False)
    expire_date = db.Column(db.DateTime, nullable=False)
    drugstore_name = db.Column(db.VARCHAR(20), nullable=False)
    buy_date = db.Column(db.DateTime, nullable=False)


def __repr__(self):
    return f"Expire('{self.medicine}','{self.no_of_goods}', '{self.quantity}', '{self.expire_date}')"


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    medicine = db.Column(db.VARCHAR(60), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost_price = db.Column(db.BIGINT, nullable=False)
    sell_price = db.Column(db.BIGINT, nullable=False)
    expire_date = db.Column(db.DateTime, nullable=False)
    buy_date = db.Column(db.DateTime, nullable=False)
    drugstore_name = db.Column(db.VARCHAR(20), nullable=False)
    no_of_goods = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Inventory('{self.medicine}', '{self.quantity}', '{self.expire_date}', '{self.barcode}', '{self.cost_price}', '{self.sell_price}')"


class Newgoods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    medicine = db.Column(db.VARCHAR(60), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost_price = db.Column(db.BIGINT, nullable=False)
    sell_price = db.Column(db.BIGINT, nullable=False)
    expire_date = db.Column(db.DateTime, nullable=False)
    buy_date = db.Column(db.DateTime, nullable=False)
    drugstore_name = db.Column(db.VARCHAR(20), nullable=False)
    no_of_goods = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Newgoods('{self.barcode}', '{self.no_of_goods}','{self.buy_date}','{self.expire_date}','{self.sell_price}','{self.cost_price}','{self.quantity}','{self.medicine}', '{self.drugstore_name}')"


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    medicine = db.Column(db.VARCHAR(60), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.BIGINT, nullable=False)
    final_price = db.Column(db.BIGINT, nullable=False)
    cost_price = db.Column(db.BIGINT, nullable=False)
    sell_price = db.Column(db.BIGINT, nullable=False)
    expire_date = db.Column(db.DateTime, nullable=False)
    profit = db.Column(db.BIGINT, nullable=False)
    drugstore_name = db.Column(db.VARCHAR(20), nullable=False)
    no_of_goods = db.Column(db.Integer, nullable=False)
    invoice_no = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Invoice('{self.medicine}', '{self.quantity}','{self.price}', '{self.expire_date}', '{self.cost_price}', '{self.sell_price}', '{self.profit}')"


class Invoices(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    medicine = db.Column(db.VARCHAR(60), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.BIGINT, nullable=False)
    invoice_no = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Invoices('{self.medicine}', '{self.quantity}','{self.price}','{self.invoice_no}')"
