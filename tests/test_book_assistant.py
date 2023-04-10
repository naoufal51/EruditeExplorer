import pytest
from src.book_assistant import BookAssistant
from src.book_indexer import BookIndexer
from src.utils import load_document, index_document, search_similar_text_blocks, generate_answer

# Update this path to a valid PDF file for testing purposes
TEST_BOOK_PATH = "data/raw/SuttonBartoIPRLBook2ndEd.pdf"

def test_load_document():
    document = load_document(TEST_BOOK_PATH)
    assert document is not None

def test_index_document():
    document = load_document(TEST_BOOK_PATH)
    indexed_document = index_document(document)
    assert indexed_document is not None

def test_search_similar_text_blocks():
    query = "test query"
    search_results = search_similar_text_blocks(query)
    assert search_results is not None

def test_generate_answer():
    query = "test query"
    search_results = search_similar_text_blocks(query)
    answer = generate_answer(search_results, query)
    assert answer is not None

def test_book_assistant():
    book_assistant = BookAssistant()
    query = "test query"
    answer = book_assistant.ask_question(query)
    assert answer is not None

def test_book_indexer():
    book_indexer = BookIndexer()
    indexed_document = book_indexer.index_book(TEST_BOOK_PATH)
    assert indexed_document is not None
