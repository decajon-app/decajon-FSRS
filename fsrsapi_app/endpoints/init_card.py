from fastapi import APIRouter, Path
from ..services.fsrs_service import init_card

router = APIRouter()

@router.get("/init_card/{card_id}")
async def init_card_endpoint(card_id: int = Path(...)):
    initialized_new_card = init_card(card_id)
    return initialized_new_card