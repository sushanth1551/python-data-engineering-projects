# ETL Data Pipeline using Python

## Project Overview
This project demonstrates the implementation of a **basic ETL (Extract, Transform, Load) pipeline** using Python.

The objective of the project is to extract data from multiple file formats, transform the data into a standardized format, and load the cleaned data into a target dataset.

ETL pipelines are widely used in **data engineering and data warehousing** to process raw data before analysis.

---

## ETL Process

### 1. Extract
Data is extracted from multiple file formats:

- CSV files
- JSON files
- XML files

Python scripts read these files and combine them into a unified dataframe.

---

### 2. Transform
The transformation step standardizes the dataset by converting units:

- Height converted from **inches to meters**
- Weight converted from **pounds to kilograms**

This ensures the dataset is consistent and ready for analysis.

---

### 3. Load
The final transformed dataset is stored in a **CSV file** for further processing or analysis.

---

## Technologies Used

- Python
- Pandas
- XML ElementTree
- Glob module
- Datetime module

---

## Project Structure

ETL_Project  
│  
├── etl.py  
├── source1.csv  
├── source2.json  
├── source3.xml  
├── transformed_data.csv  
└── log_file.txt  

---

## How the Project Works

1. The script scans the folder for data files.
2. Data is extracted from CSV, JSON, and XML files.
3. All extracted data is combined into one dataframe.
4. Unit conversion transformations are applied.
5. The final dataset is exported to a CSV file.
6. Logging records each stage of the ETL pipeline.

---

## Skills Demonstrated

- ETL pipeline design
- Data transformation using Python
- Handling multiple file formats
- Data cleaning and preprocessing
- Automation of data workflows