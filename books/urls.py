from flask import request

from ..app import app
from .controllers import list_all_books_controller, create_book_controller

@app.route("/books", methods=['GET', 'POST'])
def list_books():
    if request.method == 'GET': return list_all_books_controller()
    if request.method == 'POST': return create_book_controller()
