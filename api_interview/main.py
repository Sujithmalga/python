from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json


class interview(BaseModel):
    question: str
    feedback: str
    qtypes: str
    user: str


app = FastAPI()


@app.get("/interview/")
async def get_data() -> List[interview]:
    product= []
    product.append(interview(question="how does jenkins works in cicd",feedback="very impacted",qtypes="hard",user="sujith"))
    return {product.json}

@app.post("/interview/")
async def create_data(pratice: interview):
    print(pratice.question, pratice.feedback, pratice.qtypes, pratice.user)
    return {"message" : "created" }


