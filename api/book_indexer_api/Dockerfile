FROM python:3.8-slim

<<<<<<< HEAD
WORKDIR /app

=======
# Set environment variables
ENV PINECONE_API_KEY=""
ENV OPENAI_API_KEY=""
ENV INDEX_NAME="book-assistant"

WORKDIR /app

# Update package list, install necessary dependencies and clean up
RUN apt-get update && \
    apt-get install -y git g++ build-essential ca-certificates openssl poppler-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install torch 
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

>>>>>>> main
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src
COPY ./api/book_indexer_api/main.py /app/main.py

<<<<<<< HEAD
ENV PINECONE_API_KEY ""
ENV OPENAI_API_KEY ""
ENV INDEX_NAME ""

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
=======

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


>>>>>>> main
