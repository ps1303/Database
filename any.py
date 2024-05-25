import sqlite3
conn=sqlite3.connect("inventory.db")
cursor=conn.cursor()

# cursor.execute("SELECT * FROM products")
# products = cursor.fetchall()

# for product in products:
#     print(product)

# # cursor.execute("INSERT INTO products VALUES (?,?,?,?,?,?)",(6,'Brown Rice','8 kg', 206, 106, ))
# # conn.commit()

# cursor.close()
# conn.close()


# To export table as CSV file
import sqlite3
import csv

# Replace with your database file path
db_file = "inventory.db"

# Connect to database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Table to export (replace with your table name)
table_name = "products"

# Get table data
cursor.execute(f"SELECT * FROM {table_name}")
data = cursor.fetchall()

# Create CSV writer
with open("products.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write header row (optional)
    writer.writerow([column[0] for column in cursor.description])  # Get column names

    # Write data rows
    writer.writerows(data)

# Close connections
cursor.close()
conn.close()

print(f"Exported table '{table_name}' to products.csv")
