from marshmallow import Schema, fields, EXCLUDE


class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()
    description = fields.Str()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


incoming_book_data = {
    "title": "Clean Code",
    "author": "Bob Martin",
}

book_schema = BookSchema()
book = book_schema.load(incoming_book_data)
book_obj = Book(**book)

print(book_obj)
