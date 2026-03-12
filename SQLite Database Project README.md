# SQLite Database Management using Python

## Project Overview
This project demonstrates how to create and manage a **SQLite database using Python and Pandas**.

The script reads instructor data from a CSV file, loads it into a SQLite database, performs SQL queries, and appends new data.

This project highlights how Python can be used for **database interaction and data analysis workflows**.

---

## Workflow

### Step 1: Connect to Database
Python establishes a connection to a SQLite database using the `sqlite3` library.

### Step 2: Load Data
Instructor data is read from a CSV file using Pandas and stored in a SQLite table.

### Step 3: Execute Queries
Several SQL queries are executed:

- Display all rows
- Display specific columns
- Count total records

### Step 4: Append New Data
New instructor data is added to the database table.

---

## Technologies Used

- Python
- Pandas
- SQLite3
- SQL

---

## Project Structure

Database_Project  
│  
├── database_script.py  
├── INSTRUCTOR.csv  
└── STAFF.db  

---

## Skills Demonstrated

- SQL database creation
- Data loading using Pandas
- Executing SQL queries in Python
- Appending records to database
- Database connectivity