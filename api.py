from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = flask(__name__)



app.cnfig['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = sqlAlchemy(app)


class Book(db.model):
    id = db.Column(db.integer, primary_key=true)
    name = db.Column(db.string(80), unique=true, nullable=false)
    description = db.Column(db.string(120))

    def__repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'hello!'


@app.route('/books')
def get_books():
    books = Books.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'description': book.description}

        output.append(book_data)

    return {"books": output}

@app.route('/books/<id>')
def get_books(id):
    book = book.queary.get_or_404(id)
    return {"name" : book.name, "description": book.description}


@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json['name'],
                description=request.json[description])
    db.session.add(book)
    db.session.commit()
    return {'id': books.id}


@app.route('/books/<id>', methods=['DELETE'])
def delete_books(none=None):
    book = Book.queary.get(id)
    if book is none:
        return {"error": "404"}
    db.session.delete(book)
    db.session.commit()
    retrun ["message": "yeet!lol@"]