
from fastapi import APIRouter, Body, Path
from datetime import datetime, timezone
from typing import List
#from ..models.card import Card
from fsrs import Card  # Importa la clase Card desde tu módulo FSRS
router = APIRouter() 

@router.post("/screen_recomendations/{user_id}")
async def obtener_recomendaciones_fsrs(user_id: int = Path(...),
                                       cards_data: List[dict] = Body(...)
                                       ):
    now = datetime.now(timezone.utc)
    cards = [Card.from_dict(card_data) for card_data in cards_data]

    def calculate_urgency(card: Card) -> float:
        return -(card.due - now).total_seconds() - (1 - card.get_retrievability(now)) * 100

    sorted_cards = sorted(cards, key=calculate_urgency, reverse=True)
    top_n = 10 
    return [card.card_id for card in sorted_cards[:top_n]]