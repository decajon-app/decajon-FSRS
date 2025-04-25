from fastapi import FastAPI

from .endpoints import review_card

app = FastAPI()

app.include_router(review_card.router, prefix="/fsrs")