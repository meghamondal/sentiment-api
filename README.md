# sentiment-api
A FastAPI-based API for batch sentiment analysis.

## Live API

https://sentiment-api-wf5p.onrender.com/sentiment

## Features

- Batch sentiment classification
- Detects happy, sad, and neutral sentiments
- JSON request and response
- CORS enabled
- Publicly deployed on Render

## Example Request

POST /sentiment

```json
{
  "sentences": [
    "I love this!",
    "This is terrible.",
    "The meeting is at 3 PM."
  ]
}
```
## Example Response
```json
{
  "results": [
    {
      "sentence": "I love this!",
      "sentiment": "happy"
    },
    {
      "sentence": "This is terrible.",
      "sentiment": "sad"
    },
    {
      "sentence": "The meeting is at 3 PM.",
      "sentiment": "neutral"
    }
  ]
}
```
## Tech Stack
- Python
- FastAPI
- Uvicorn
- Render
