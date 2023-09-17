import csv
import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

with open('books2.csv', 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        title, author, year = row
        cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, int(year)))

conn.commit()
conn.close()