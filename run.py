"""
set FLASK_APP=market.py
set FLASK_DEBUG=1
flask run

>>> from market import db, app
>>> with app.app_context():
...     db.create_all()

>>> from market import db, app, Item
>>> with app.app_context():
...     item1 = Item(name="Samsung Galaxy S24", price=1000, barcode="873625490290", description="desc")
...     db.session.add(item1)
...     db.session.commit()

>>> with app.app_context():
...     Item.query.all()
...
[Item Samsung Galaxy S24, Item IPhone 16]

>>> with app.app_context():
...     for item in Item.query.all():
...             item.name
...             item.price
...
...
'Samsung Galaxy S24'
1000
'IPhone 16'
1000

>>> with app.app_context():
...     for item in Item.query.filter_by(name="IPhone 16"):
...             item.name
...
'IPhone 16'




>>> from market import db, app
>>> with app.app_context():
...     db.drop_all()

>>> with app.app_context():
...     db.create_all()

>>> from market.models import db, User, Item
>>> with app.app_context():
...     u1 = User(username="nedmac", password_hash="123456", email_address="nedmac@gmail.com")

>>> with app.app_context():
...     db.session.add(u1)
...     db.session.commit()
...
>>> with app.app_context():
...     User.query.all()
...
[<User 1>]
"""

from market import app

if __name__ == "__main__":
    app.run(debug=True)