from fastapi import FastAPI
from APP.analytics import (
    get_average_energy_usage,
    get_average_bill,
    get_total_customers,
    get_automation_rate
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to TragerInc Energy Chatbot API"}

@app.get("/summary")
def get_summary():
    return {
        "total_customers": get_total_customers(),
        "average_energy_usage_kwh": get_average_energy_usage(),
        "average_bill": get_average_bill(),
        "automation_rate_percent": get_automation_rate()
    }
from APP.schemas import ChatRequest
from APP.chatbot_engine import chatbot_response
@app.post("/chat")
def chat(request: ChatRequest):

    response = chatbot_response(request.query)

    return {
        "query": request.query,
        "response": response
    }
