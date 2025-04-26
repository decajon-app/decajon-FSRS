from fastapi import FastAPI

from .endpoints import review_card
from .endpoints import screen_recomendations
app = FastAPI()

app.include_router(review_card.router, prefix="/fsrs")
app.include_router(screen_recomendations.router, prefix="/fsrs")