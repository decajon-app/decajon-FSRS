from fastapi import FastAPI

from .endpoints import review_card
from .endpoints import screen_recomendations
from .endpoints import init_card
app = FastAPI()

app.include_router(review_card.router, prefix="/fsrs")
app.include_router(screen_recomendations.router, prefix="/fsrs")
app.include_router(init_card.router, prefix="/fsrs")