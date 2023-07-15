from .utils import load_document, index_document

class BookIndexer:
    def __init__(self):
        pass

    def index_book(self, book_path: str):
        document = load_document(book_path)
        indexed_document = index_document(document)
        return indexed_document
