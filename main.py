from fastapi import FastAPI, Form
from analyzer import analyze_input
from telegram_bot import send_to_telegram

app = FastAPI()

@app.post("/submit/")
async def process_input(user_input: str = Form(...)):
    analysis = analyze_input(user_input)
    send_to_telegram(analysis)
    return {"status": "success", "data": analysis}
