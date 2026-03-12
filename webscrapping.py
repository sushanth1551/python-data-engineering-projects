import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"

db_name = "Movies.db"
table_name = "Top_50"

csv_path = r"C:\Users\SUSHANTH DUGGENI\Documents\VS CODE -codes\PROJECTS\ETL\top_50_films.csv"

df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
count = 0

html_page = requests.get(url).text
soup = BeautifulSoup(html_page, "html.parser")

tables = soup.find_all("tbody")
rows = tables[0].find_all("tr")

for row in rows:
    if count < 50:
        col = row.find_all("td")

        if len(col) != 0:
            data_dict = {
                "Average Rank": col[0].text.strip(),
                "Film": col[1].text.strip(),
                "Year": col[2].text.strip()
            }

            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)

            count += 1
    else:
        break

print(df)

# Save to CSV
df.to_csv(csv_path, index=False)

# Save to SQLite database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists="replace", index=False)
conn.close()

print("Data saved to CSV and SQLite database successfully.")