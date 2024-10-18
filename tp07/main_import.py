import csv
import sqlite3

def main():
    
    con = sqlite3.connect("customers_db.db")

    sql_insert = """INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address)
    VALUES (?,?,?,?,?)
    """
    with open('MOCK_DATA.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            del row['id']
            con.execute(sql_insert,list(row.values()))
    
    con.commit()
    con.close()

if __name__=='__main__':
    main()
