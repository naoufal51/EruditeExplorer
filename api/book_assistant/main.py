from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.book_assistant_v2 import BookAssistant
from src.book_indexer import BookIndexer
from fastapi.middleware.cors import CORSMiddleware
from src.utils import IgnoreNonSerializable
import logging
import os
import tempfile

logging.basicConfig(level=logging.INFO)

# Create FastAPI instance
app = FastAPI(json_encoder=IgnoreNonSerializable)

book_assistant = BookAssistant()
book_indexer = BookIndexer()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chatbot_endpoint")
async def chat_endpoint(request: Request):
    data = await request.json()
    message = data["message"]

    # Process the user message and generate a response
    response = book_assistant.ask_question(message)

    return {"reply": response}

@app.post("/index")
async def index_book(pdf_file: UploadFile = File(...)):
    logging.info(f"Received file {pdf_file.filename}")

    # Use a temp file
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(await pdf_file.read())
        temp_path = temp.name

    logging.info(f"File {temp_path} saved")

    # Now you can pass the temp file path to your function
    response = book_indexer.index_book(temp_path)

    logging.info(f"Response: {response}")

    # Clean up the temp file
    os.remove(temp_path)

    return {"response": "Uploaded"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001, log_level="info")
