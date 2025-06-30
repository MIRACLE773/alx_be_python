#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (change credentials if needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MJMUSIC"  
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
