import sqlite3
conn=sqlite3.connect("inventory.db")
cursor=conn.cursor()

# To print the table 'product'
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
for product in products:
    print(product)

# FOR INSERTING ANY ROW
# Replace with valid category and supplier IDs
category_id = 206
supplier_id = 106
# Data for the new product
new_product_data = (6, 'Black Beans', '1 kg', category_id, supplier_id, "covert into binary format first")
# Insert statement with placeholders for all columns
insert_query = "INSERT INTO products VALUES (?,?,?,?,?,?)"
# Execute the insert query with the prepared data
cursor.execute(insert_query, new_product_data)
conn.commit()



# FOR UPDATING
# Update a product price
cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (1,))
conn.commit()


# FOR DELETING
# Delete a product
cursor.execute("DELETE FROM products WHERE id = ?", (1,))
conn.commit()


cursor.close()
conn.close()