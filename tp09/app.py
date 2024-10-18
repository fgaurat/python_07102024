from flask import Flask,render_template
from CustomerDAO import CustomerDAO

# flask --app apptruc.py run
app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/index_ugly")
def index_ugly():
    dao = CustomerDAO("customers_db.db")
    customers = dao.findAll()
    html=""
    for customer in customers:
        html+=f"<li>{customer.last_name} {customer.first_name}</li>"
        
    return "<ul>"+html+"</ul>"

@app.route("/")
def index():
    dao = CustomerDAO("customers_db.db")
    customers = dao.findAll()
    return render_template('customers.html',customers=customers)