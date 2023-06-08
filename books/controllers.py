from flask import request, jsonify

from .. import db
from .models import Book

def list_all_books_controller():
    books = Book.query.all()
    response = []
    for book in books: response.append(format_book(book))
    return jsonify(response)

def create_book_controller():
    data = request.json

    new_book = Book(
        title = data['title'],
        author = data['author'],
        stars = data['stars']
    )
    db.session.add(new_book)
    db.session.commit()

    return jsonify(id=new_book.id, title=new_book.title, author=new_book.author, stars=new_book.stars)


def format_book(self):
    return {
        "title": self.title,
        "author": self.author,
        "stars": self.stars
    }
