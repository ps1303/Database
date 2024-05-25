import sqlite3
conn=sqlite3.connect("inventory.db")
cursor=conn.cursor()

# cursor.execute("SELECT * FROM products")
# products = cursor.fetchall()

# for product in products:
#     print(product)

#  cursor.execute("INSERT INTO products VALUES (?,?,?,?,?,?)",(6,'Brown Rice','8 kg', 206, 106, ))
#  conn.commit()

# cursor.close()
# conn.close()


# To export table as CSV file
import sqlite3
import csv

db_file = "inventory.db"

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

table_name = "products"

cursor.execute(f"SELECT * FROM {table_name}")
data = cursor.fetchall()

with open("products.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([column[0] for column in cursor.description])  # Get column names

    writer.writerows(data)

cursor.close()
conn.close()

print(f"Exported table '{table_name}' to products.csv")
