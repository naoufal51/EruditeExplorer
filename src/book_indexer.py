from .utils import load_document, index_document
import logging

class BookIndexer:
    def __init__(self):
        pass

    def index_book(self, book_path: str):
        logging.info(f"Loading document from {book_path}")
        document = load_document(book_path)
        logging.info(f"Indexing document")
        indexed_document = index_document(document)
        logging.info(f"Document indexed")
        # Remove Pinecone object from the response
        indexed_document.pop("pinecone", None)
        return {"message": "Document indexed successfully", "indexed_blocks": len(indexed_document)}
