from typing import Union
from CustomerDAO import CustomerDAO
from Customer import Customer
from typing import List
from fastapi import FastAPI

app = FastAPI()


@app.get("/",response_model=List[Customer])
def get_customers():
    # dao = CustomerDAO("customers_db.db")
    with CustomerDAO("customers_db.db") as dao:
        all = dao.findAll()
    return all
    

