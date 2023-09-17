import csv

data = [
    {"title": "The Weirdstone of Brisingamen", "author": "Alan Garner", "year": 1960},
    {"title": "Perdido Street Station", "author": "China Miéville", "year": 2000},
    {"title": "Thud!", "author": "Terry Pratchett", "year": 2005},
    {"title": "The Spellman Files", "author": "Lisa Lutz", "year": 2007},
    {"title": "Small Gods", "author": "Terry Pratchett", "year": 1992},
]

csv_file = "books2.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "author", "year"])

    writer.writeheader()

    writer.writerows(data)

print(f'Data has been saved to {csv_file}')
