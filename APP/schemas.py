from pydantic import BaseModel

class CustomerQuery(BaseModel):
    customer_id: str

class ChatRequest(BaseModel):
    query: str
    