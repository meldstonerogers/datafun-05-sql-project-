# datafun-05-sql-project-
# Module 5 Project
Melissa Stone Rogers, May 20, 2024

## Introduction
Professional project integrating Python and SQL, focusing on database interactions using SQLite.
Commands were used on a Mac machine running zsh.  

## How to Install and Run the Project
Create project repository in Github and clone to your machine.

```shell
git clone project.url
```

```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Freeze Requirements

```shell
python3 -m pip freeze > requirements.txt
```

## Import Dependencies and Create Database

```shell
import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def main():
    create_database()

if __name__ == "__main__":
    main()
```    

## Git Add / Commit / Push 

```shell
git add .
git commit -m "initial commit"
git push origin main
```

## Specification

This project was built to the following specification:
https://github.com/denisecase/datafun-05-spec