# Book Assistant Chatbot

A chatbot application that allows users to ask questions about a book, and it provides answers based on the book's content. The chatbot is built using FastAPI for the backend, Chatscope for the chat UI, and React for the frontend.

## Features

* Natural language processing capabilities
* Book indexing and searching for relevant information
* Interactive chat UI with Chatscope

## Getting Started

### Prerequisites
* Python 3.7 or higher
* Node.js and npm
* FastAPI
* Uvicorn
* Pinecone
* OpenAI
* Chatscope
* Langchain
* Torch

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/naoufal51/book-assistant-chatbot.git
   cd book-assistant-chatbot
    ```
2. Create a virtual environment and install the required Python dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
     ```
3. Set the necessary environment variables:
    ```sh
    export PINECONE_API_KEY=<your Pinecone API key>
    export OPENAI_API_KEY=<your OpenAI API key>
    ```
4. Navigate to the frontend directory and install the required npm packages:
    ```sh
    cd frontend
    npm install
    ```

### Usage
1. Start the backend server:
    ```sh
    cd path/to/book-assistant-chatbot
    uvicorn main:app --host 0.0.0.0 --port 8001 --reload
    ```
2. Start the book_indexer_api server:
    ```sh
        cd path/to/book-assistant-chatbot/book_indexer_api
        uvicorn main:app --host 0.0.0.0 --port 8002 --reload
    ```
3. Index a book by sending a PDF file to the /index endpoint of the book_indexer_api server using a REST client or curl, for example:
    ```sh
    curl -X POST -H "Content-Type: multipart/form-data" -F "pdf_file=@path/to/your/book.pdf" http://localhost:8002/index
    ```
    The server will respond with a message indicating that the document has been indexed successfully.

4. Start the frontend server:
    ```sh
    cd path/to/book-assistant-chatbot/frontend
    npm start
    ```
Open http://localhost:3000 in your browser to view the chat UI.


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

 

