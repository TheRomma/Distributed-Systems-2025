from fastapi import FastAPI
from app.producer import produce_add_message, produce_remove_message

app = FastAPI()

@app.post("/add")
async def add_message(link: str, title: str):
    produce_add_message(link, title)
    return {"status": "Message sent to 'add' topic"}

@app.post("/remove")
async def remove_message(filename: str):
    produce_remove_message(filename)
    return {"status": "Message sent to 'remove' topic"}
