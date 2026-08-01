from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from matching import match_books

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/match")
def match(input: str):
    results = match_books(input)
    return [
        {
            "title":             row[0],
            "author":            row[1],
            "ideology_keywords": row[2],
            "cover_image_url":   row[3],
            "author_message":    row[4],
            "genre":             row[5],
            "genre_color":       row[6],
            "score":             row[7],
            "preview_url":       row[8],
        }
        for row in results
        if row[7] > 0
    ]

handler = Mangum(app)
