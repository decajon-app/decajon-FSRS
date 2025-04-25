from fastapi import APIRouter, Path, Body
from datetime import datetime
from ..services.fsrs_service import process_review

router = APIRouter()

@router.post("/review_card/{card_id}")
async def review_card_endpoint(card_id: int = Path(...),
                            rating: int = Body(..., embed=True, description="Rating given by the user (1-4)"),
                            review_datetime: datetime = Body(embed=True, description="Date and time of the review (ISO format)"),
                            card_data: dict = Body(..., description="Current Card data from Spring Boot")
                        ):
    updated_card = process_review(card_data, rating, review_datetime)
    return updated_card