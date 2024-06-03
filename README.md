# datafun-05-sql-project-
# Module 5 Project
Melissa Stone Rogers, May 20, 2024

## Introduction
Professional project integrating Python and SQL, focusing on database interactions using SQLite.
Commands were used on a Mac machine running zsh.  

## How to Install and Run the Project
Create project repository in Github and clone to your machine.

```
git clone project.url
```

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Freeze Requirements

```
python3 -m pip freeze > requirements.txt
```

## Import Dependencies 

```
import sqlite3
import pandas as pd
import pyarrow as pa
import pathlib
import logging
```

## Define the Database File, Create Tables, and Insert Data
Initializing work completed within db_initialize_melissastonerogers.py file.
```
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

db_file = pathlib.Path("project.db")

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()    
```    

## Git Add / Commit / Push 

```
git add .
git commit -m "initial commit"
git push origin main
```
## Build SQL files
Include the following files: 
- create_tables.sql 
- insert_records.sql 
- update_records.sql 
- delete_records.sql 
- query_aggregation.sql 
- query_filter.sql 
- query_sorting.sql 
- query_group_by.sql 
- query_join.sql 

Add appropriate SQL statement and queries into each SQL file. 

## Python and SQL Integration
Use Python to interact with the SQL database and execute SQL commands.
Operations work completed within db_operations_melissastonerogers.py file.

Execute SQL statement or query using Python code. 
Example for function to insert data: 
```
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
```        
## Complete Your Project
Save your project and push back to your repository. 
```
git add .
git commit -m "final"                         
git push origin main
```

## Project Summary
This professional project is a valuable opportunity to become comfortable integrating Python and SQL. Engaging with ChatGPT was helpful in handling errors in SQL statements and Python code. 

![Final Project Screenshot](https://github.com/meldstonerogers/datafun-05-sql-project-/blob/main/Screen%20Shot%202024-06-02%20at%2010.59.03%20PM.png)

## Specification

This project was built to the following specification:
https://github.com/denisecase/datafun-05-spec