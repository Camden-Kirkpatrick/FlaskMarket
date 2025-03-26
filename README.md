# Flask Market

Flask Market is a web application that simulates an online marketplace where users can sign up, log in, buy, and sell items. The application is built using Flask, SQLAlchemy, Flask-Login, and Flask-WTF.

## Features
- **User Authentication:** Users can register, log in, and log out.
- **Marketplace:** Users can browse items available for purchase.
- **Buying Items:** Users can purchase items if they have enough funds.
- **Selling Items:** Users can sell owned items back to the market.
- **Flashed Messages:** Notifications for successful or failed transactions.

---

## **Project Structure**
### **Root Directory**
- `run.py` - Entry point for running the application.

### **Market Folder**
- `__init__.py` - Initializes Flask app, database, and authentication.
- `models.py` - Database models (User, Item).
- `routes.py` - Application routes (Login, Register, Market, Logout).
- `forms.py` - Forms for user authentication and item transactions.

### **Templates Folder**
- `base.html` - Base template for navigation.
- `home.html` - Homepage.
- `login.html` - Login page.
- `register.html` - Registration page.
- `market.html` - Market listing page.

### **Includes Folder (Inside Templates)**
- `items_modals.html` - Purchase confirmation modal.
- `owned_items_modals.html` - Selling confirmation modal.

---

## **Installation & Setup**
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/FlaskMarket.git
cd FlaskMarket
```

### **2. Create a Virtual Environment & Install Dependencies**
```bash
python -m venv venv  
source venv/bin/activate
pip install -r requirements.txt
```  

### **3. Set Up the Database (Automatically Created on First Run)**
The database will be created automatically when you run the application. However, if you want to manually create it, run:
```bash
python
```
Then, inside the Python shell:

```bash
from market import db, app
with app.app_context():
    db.create_all()
```

### **4. Run the Application**
```bash
python run.py
```
Visit http://127.0.0.1:5000/ in your browser.

### **5. Adding an Item to the Database Manually**
If you want to add an item manually to the database, follow these steps:

Open the Python shell:
```bash
python
```
Run the following commands inside Python:

```bash
from market import db, app    
from market.models import Item

with app.app_context():       
    item = Item(name="Samsung Galaxy S24", price=1000, barcode="873625490290", description="desc")
    db.session.add(item)
    db.session.commit()
```
This will add Samsung Galaxy S24 to the database, and it will be available on the /market page.

---

## **Usage**
### **User Registration & Login**
- Navigate to /register to create an account.
- Navigate to /login to log in.

### **Buying & Selling Items**
- Browse items on the /market page.
- Click Purchase to buy an item.
- Click Sell on an owned item to return it to the market.

## **Dependencies**
- **Flask** - Web framework
- **Flask-SQLAlchemy** - Database ORM for handling data
- **Flask-Bcrypt** - Secure password hashing
- **Flask-Login** - Manages user authentication
- **Flask-WTF** - Handles form validation
- **WTForms** - Used with Flask-WTF for creating forms
- **Bootstrap (CDN)** - Used for styling the frontend

---

## License

This project is provided as-is, without warranty or guarantee. You are free to modify or extend it for your needs.

**Enjoy using the Flask Market!**