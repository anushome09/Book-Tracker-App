from fastapi import APIRouter, Query
from typing import List, Optional

from backend.services.google_books import search_books

router = APIRouter()

@router.get("/search-books")
def google_book_search(q: str = Query(...), max_result: int=5):
    return search_books(q, max_result)