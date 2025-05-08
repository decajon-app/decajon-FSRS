from fastapi import APIRouter, Path, Body
from datetime import datetime
from ..services.fsrs_service import process_review
from ..models.models import ReviewCardRequestDto

router = APIRouter()

@router.post("/review_card/{card_id}")
async def review_card_endpoint(card_id, request: ReviewCardRequestDto):
    print("Request crudo: ", request)
    updated_card = process_review(request.card_data.model_dump(mode="json"), request.rating, request.review_datetime)
    return updated_card
