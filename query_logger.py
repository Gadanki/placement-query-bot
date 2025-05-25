import csv
from datetime import datetime

def log_query(query, category, response_type):
    with open("query_log.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), query, category, response_type])
