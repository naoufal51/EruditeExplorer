FROM python:3.8-slim

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

# Symlink g++ if necessary
RUN ln -s /usr/bin/g++ /usr/local/bin/g++
RUN pip install --upgrade certifi


# Install requirements
COPY requirements_ba.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY ./src /app/src
COPY ./api/book_assistant_api/main.py /app/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
