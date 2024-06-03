import sqlite3
import pandas as pd
import pyarrow as pa
import pathlib
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method

## Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def insert_records():
    """Function to read and execute SQL statements to insert data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("insert_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)

def update_records():
    """Function to read and execute SQL statements to update data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("update_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data updated successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)       

def delete_records():
    """Function to read and execute SQL statements to delete data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("delete_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data deleted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e) 

def query_aggregation():
    """Function to read and execute SQL statements to aggregate data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_aggregation.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data aggregated successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)                  

def query_filter():
    """Function to read and execute SQL statements to filter data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_filter.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data filtered successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)   

def query_sorting():
    """Function to read and execute SQL statements to sort data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_sorting.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data sorted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)        

def query_group_by():
    """Function to read and execute SQL statements to group data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_group_by.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data grouped successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)         

def query_join():
    """Function to read and execute SQL statements to join data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_join.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data joined successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)           

def main():
    insert_records()
    update_records()
    delete_records()
    query_aggregation()
    query_filter()
    query_sorting()
    query_group_by()
    query_join()
   

if __name__ == "__main__":
    main()        

logging.info("Program ended")  # add this at the end of the main method