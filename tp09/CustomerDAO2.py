

import sqlite3
from Customer import Customer
from CustomerCreate import CustomerCreate

class CustomerDAO:


    def __init__(self,db_name) -> None:
        self.__con = sqlite3.connect(db_name)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type,exc_value,exc_traceback):

        if exc_type is None:
            self.__con.commit()
        else:
            self.__con.rollback()
        
        self.__con.close()
        self.__con = None



    def __del__(self):
        if self.__con is not None:
            self.__con.close()


    def find_all(self):
        sql = "SELECT * FROM customers_tbl"
        cur = self.__con.cursor()
        rs = cur.execute(sql)
        field_names = [i[0] for i in cur.description]
        for row in rs:
            d = dict(zip(field_names,row))
            c= Customer(**d)
            yield c

    def create(self, customer: CustomerCreate) -> Customer:
        sql = """INSERT INTO customers_tbl (first_name, last_name, email, gender, ip_address) 
                VALUES (?, ?, ?, ?, ?)"""
        cur = self.__con.cursor()
        cur.execute(sql, (customer.first_name, customer.last_name, customer.email, customer.gender, customer.ip_address))
        self.__con.commit()
        new_id = cur.lastrowid  # Récupérer l'ID généré
        # Retourner l'objet Customer complet avec l'id généré
        return Customer(id=new_id, **customer.model_dump())
