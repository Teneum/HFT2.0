import mysql.connector

password = "19211825Yomama123"

def initialize():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd=password)
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS finance")
        cur.execute("USE finance")
        cur.execute("""CREATE TABLE IF NOT EXISTS items(
                            ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            NAME VARCHAR(255),
                            CATEGORY VARCHAR(255), 
                            PRICE FLOAT(10),
                            AMOUNT FLOAT(10),
                            DATEOFPURCHASE DATE)
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

def add_item_data(itemname, itemcategory, itemprice, itemamount, dateofpurchase):
    # try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd=password, database="finance")
        cur = conn.cursor()
        sql = """INSERT INTO items(NAME, CATEGORY, PRICE, AMOUNT, DATEOFPURCHASE) VALUES(%s,%s,%s,%s,%s)"""
        cur.execute(sql, (itemname, itemcategory, itemprice, itemamount, dateofpurchase))
        conn.commit()
        conn.close()
        print("Task performed successfully")
    # except Exception as e:
    #     print(e)

def delete_item_data(itemid):
    try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd=password, database="finance")
        cur = conn.cursor()
        cur.execute("""DELETE FROM items WHERE ID = %s""", (itemid, ))
        conn.commit()
        conn.close()
        print("Task performed successfully")
    except Exception as e:
        print(e)

def get_item_data(itemname):

    try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd=password, database="finance")
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM items WHERE NAME = '{itemname}'""")
        data = cur.fetchall()
        container = []
        for i in data:
            hashmap = {
                    "ID": i[0],
                    "Name": i[1],
                    "Category": i[2],
                    "Price": i[3],
                    "Amount": i[4],
                    "DateOfPurchase": i[5]
                   }
            container.append(hashmap)
        conn.close()
        return container

    except Exception as e:
        print(e)
        return [{
            "ID": "None",
            "Name": "None",
            "Category": "None",
            "Price": "None",
            "Amount": "None",
            "DateOfPurchase": "None"
        }]

def get_item_data_by_category(category):
    try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd=password, database="finance")
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM items WHERE CATEGORY = '{category}'""")
        data = cur.fetchall()
        container = []
        for i in data:
            hashmap = {
                    "ID": i[0],
                    "Name": i[1],
                    "Category": i[2],
                    "Price": i[3],
                    "Amount": i[4],
                    "DateOfPurchase": i[5]
                   }
            container.append(hashmap)
        conn.close()
        return container
    except Exception as e:
        print(e)

def get_all_item_data():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd=password, database="finance")
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM items""")
        data = cur.fetchall()
        container = []
        for i in data:
            hashmap = {
                    "ID": i[0],
                    "Name": i[1],
                    "Category": i[2],
                    "Price": i[3],
                    "Amount": i[4],
                    "DateOfPurchase": i[5]
                   }
            container.append(hashmap)
        conn.close()
        return container
    except Exception as e:
        print(e)

def custom_sql(sql):
    try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd=password, database="finance")
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        field_names = [i[0] for i in cur.description]
        container = []
        for i in data:
            hashmap = dict(zip(field_names, i))
            container.append(hashmap)
        conn.close()
        return container
    except Exception as e:
        print(e)

