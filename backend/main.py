from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from pydantic import BaseModel
from matching import match_books, add_book_request, get_pending_requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

class RequestCreate(BaseModel):
    title: str
    author: str = ""
    genre: str = "哲学"
    reason_keywords: str = ""

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
def create_request(req: RequestCreate):
    if not req.title.strip():
        raise HTTPException(status_code=400, detail="タイトルは必須です")
    
    created_item = add_book_request(
        title=req.title.strip(),
        author=req.author.strip(),
        genre=req.genre.strip(),
        reason_keywords=req.reason_keywords.strip()
    )
    return {"status": "success", "request": created_item}

@app.get("/requests")
def list_requests():
    return get_pending_requests()

handler = Mangum(app)
