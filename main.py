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
    "nice", "best", "enjoy", "liked", "like",
    "brilliant", "perfect", "cool", "fun",
    "excited", "beautiful", "positive", "success",
    "smile", "joy", "pleased", "delight",
    "super", "outstanding", "favorite", "fantabulous",
    "win", "winning", "laugh", "loved", "yay",
    "sweet", "glad", "cheerful", "satisfied"
]

sad_words = [
    "sad", "bad", "terrible", "awful", "hate",
    "worst", "angry", "upset", "disappointed",
    "horrible", "cry", "pain", "annoying",
    "depressed", "negative", "poor", "failure",
    "boring", "disaster", "ugly", "sucks",
    "problem", "broken", "mad", "unhappy",
    "frustrated", "tired", "stress", "hurt",
    "loser", "losing", "fail", "failed",
    "depressing", "miserable", "tragic",
    "pathetic", "hate", "crying"
]

def detect_sentiment(text):

    lower = text.lower()

    happy_score = 0
    sad_score = 0

    for word in happy_words:
        if word in lower:
            happy_score += 1

    for word in sad_words:
        if word in lower:
            sad_score += 1

    if happy_score > sad_score:
        return "happy"

    if sad_score > happy_score:
        return "sad"

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
