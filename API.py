from fastapi import fastapi
from PoetryGPT import handle_message

app = FastAPI()


@app.post("/poetry")
async def poetry(text):
    return handle_message(text)
