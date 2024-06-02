import sqlite3
import pandas as pd
import pyarrow as pa
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def create_database():
    """Function to create a database."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("create_tables.sql")
            if sql_file.exists():
                with open(sql_file, "r") as file:
                    sql_script = file.read()
                conn.executescript(sql_script)
                print("Tables created successfully.")
            else: 
                print(f"SQL file {sql_file} does not exist.")    
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def main():
    create_database()
    create_tables()

if __name__ == "__main__":
    main()    