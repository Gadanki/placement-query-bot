import csv
from datetime import datetime

def log_feedback(query, response, feedback):
    with open("feedback_log.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), query, response, feedback])
