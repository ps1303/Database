import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def updateBLOB(id, photo):
    try:
        sqliteConnection = sqlite3.connect('inventory.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_update_blob_query = """ UPDATE products
                                       SET photo = ?
                                       WHERE id = ?"""

        empPhoto = convertToBinaryData(photo)
        # Convert data into tuple format
        data_tuple = (empPhoto, id)
        cursor.execute(sqlite_update_blob_query, data_tuple)
        sqliteConnection.commit()
        print(f"Image for product ID {id} updated successfully as a BLOB into the table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")

# Example usage:
updateBLOB(1, "C:\\Users\\hp\\Desktop\\db\\inv\\maida.jpg")
updateBLOB(2, "C:\\Users\\hp\\Desktop\\db\\inv\\41RLYdZ6L4L.jpg")
updateBLOB(3, "C:\\Users\\hp\\Desktop\\db\\inv\\wheat.jpg")
updateBLOB(4, "C:\\Users\\hp\\Desktop\\db\\inv\\rice flour.jpg")
updateBLOB(5, "C:\\Users\\hp\\Desktop\\db\\inv\\basmati-rice.jpg")
