from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.book_assistant import BookAssistant
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
book_assistant = BookAssistant()

# Add the following lines to enable CORS
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")
