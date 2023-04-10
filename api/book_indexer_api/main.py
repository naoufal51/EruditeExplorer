from fastapi import FastAPI, File, UploadFile
from src.book_indexer import BookIndexer
import logging
from fastapi import FastAPI
from custom_json_encoder import IgnoreNonSerializable

logging.basicConfig(level=logging.INFO)

app = FastAPI(json_encoder=IgnoreNonSerializable)



# app = FastAPI()
book_indexer = BookIndexer()

@app.post("/index")
async def index_book(pdf_file: UploadFile = File(...)):
    logging.info(f"Received file {pdf_file.filename}")
    with open(pdf_file.filename, "wb") as buffer:
        buffer.write(await pdf_file.read())
    logging.info(f"File {pdf_file.filename} saved")
    response = book_indexer.index_book(pdf_file.filename)
    logging.info(f"Response: {response}")
    return {"response": "Uploaded"}

