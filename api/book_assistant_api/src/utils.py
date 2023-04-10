import os
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone, Chroma
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import pinecone

PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_ENV = os.environ.get("PINECONE_ENV", "northamerica-northeast1-gcp")
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
INDEX_NAME = os.environ.get("INDEX_NAME", "book-assistant")


pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

def load_document(book_path: str):
    loader = UnstructuredPDFLoader(book_path)
    document = loader.load()
    return document

def index_document(document):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    text_blocks = splitter.split_documents(document)
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    search = Pinecone.from_texts([text_block.page_content for text_block in text_blocks], index_name=INDEX_NAME, embedding=embeddings)
    return search

def search_similar_text_blocks(query: str):
    index = pinecone.Index(INDEX_NAME)
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    # search = Pinecone(index, embedding=embeddings)
    search = Pinecone(index, embeddings.embed_query, "text")
    docs = search.similarity_search(query, include_metadata=True)
    return docs

def generate_answer(search_results, question: str):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
    chain = load_qa_chain(llm, chain_type="stuff")
    answer = chain.run(input_documents=search_results, question=question)
    return answer
