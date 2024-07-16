from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from replit import db
import re

app = FastAPI()


class UserMessage(BaseModel):
    msg_id: str
    name: str
    email: str
    message: str


@app.get("/")
async def root():
    return {"message": "Nothing Here"}

@app.post("/message", status_code=201)
async def message(message: UserMessage):
    
    # Validate the message and email using regex \w+@\w+\.\w+
    if not re.match(r"\w+@\w+\.\w+", message.email):
        raise HTTPException(status_code=400, detail="Invalid email")

    if len(message.name) < 3 or len(message.message) < 10:
        raise HTTPException(status_code=400, detail="Invalid message")

    db[message.msg_id] = message
    return {"message": "Message Sent"}
