from CustomerDAO import CustomerDAO

def filterFemale(stream):
    for data in stream:
        if data.gender == "Female":
            yield data


def main():
    dao = CustomerDAO("customers_db.db")
    customers = dao.findAll()
    f_customers = filterFemale(customers)
    # l_cust = list(customers)
    # print(len(l_cust))
    

    for customer in f_customers:
        print(customer.first_name,customer.last_name)

if __name__=='__main__':
    main()
