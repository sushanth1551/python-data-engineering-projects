# Web Scraping Top 50 Ranked Films

## Project Overview
This project demonstrates how to perform **web scraping using Python**.

The script extracts information about the **Top 50 highly ranked films** from a webpage and stores the results in both a CSV file and a SQLite database.

Web scraping is commonly used in data engineering to collect publicly available data from websites.

---

## Data Source

Archived webpage:

https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films

Data extracted:

- Average Rank
- Film Name
- Year

---

## Workflow

### Step 1: Download Webpage
The `requests` library fetches the HTML content of the webpage.

### Step 2: Parse HTML
BeautifulSoup parses the HTML document and identifies the film ranking table.

### Step 3: Extract Data
The script loops through table rows and extracts the required fields.

### Step 4: Store Data
The extracted data is saved into:

- CSV file
- SQLite database

---

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- SQLite3

---

## Project Structure

WebScraping_Project  
│  
├── web_scraper.py  
├── top_50_films.csv  
└── Movies.db  

---

## Skills Demonstrated

- Web scraping
- HTML parsing
- Data extraction
- Data storage using SQLite
- Python automation