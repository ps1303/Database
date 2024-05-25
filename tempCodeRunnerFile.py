import sqlite3
conn=sqlite3.connect("inventory.db")
cursor=conn.cursor()

cursor.execute("SELECT * FROM products")
products = cursor.fetchall()

for product in products:
    print(product)