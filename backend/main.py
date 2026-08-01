from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from matching import match_books, add_book_request, get_pending_requests

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

@app.post("/requests")
def create_request(data: dict = Body(...)):
    title = str(data.get("title", ""))
    author = str(data.get("author", ""))
    genre = str(data.get("genre", "哲学"))
    reason_keywords = str(data.get("reason_keywords", ""))

    if not title.strip():
        raise HTTPException(status_code=400, detail="タイトルは必須です")

    created_item = add_book_request(
        title=title.strip(),
        author=author.strip(),
        genre=genre.strip(),
        reason_keywords=reason_keywords.strip()
    )
    return {"status": "success", "request": created_item}

@app.get("/requests")
def list_requests():
    return get_pending_requests()

handler = Mangum(app)
