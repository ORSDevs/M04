from sqlalchemy import create_engine, select, text

engine = create_engine('sqlite:///books.db')

conn = engine.connect()

metadata = text('SELECT title FROM books').columns
books_table = metadata['books']

select_query = select([books_table.c.title]).order_by(books_table.c.title)

results = conn.execute(select_query).fetchall()

for title in results:
    print(title[0])

conn.close()