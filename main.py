from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class SentencesInput(BaseModel):
    sentences: List[str]

happy_words = [
    "love", "great", "awesome", "happy", "good",
    "excellent", "amazing", "fantastic", "wonderful",
    "nice", "best", "enjoy", "liked"
]

sad_words = [
    "sad", "bad", "terrible", "awful", "hate",
    "worst", "angry", "upset", "disappointed",
    "horrible", "cry", "pain"
]

def detect_sentiment(text):

    lower = text.lower()

    happy_score = sum(word in lower for word in happy_words)
    sad_score = sum(word in lower for word in sad_words)

    if happy_score > sad_score:
        return "happy"

    elif sad_score > happy_score:
        return "sad"

    else:
        return "neutral"

@app.post("/sentiment")
def sentiment(data: SentencesInput):

    results = []

    for sentence in data.sentences:

        results.append({
            "sentence": sentence,
            "sentiment": detect_sentiment(sentence)
        })

    return {
        "results": results
    }