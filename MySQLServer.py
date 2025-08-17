#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust user/password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # replace with your MySQL username
            password='your_password'  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Always close cursor and connection if they were opened
        try:
            if cursor:
                cursor.close()
        except NameError:
            pass
        try:
            if connection.is_connected():
                connection.close()
        except NameError:
            pass

if __name__ == "__main__":
    create_database()
