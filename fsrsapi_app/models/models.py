# models.py

from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class CardData(BaseModel):
    card_id: int
    state: int
    step: int
    stability: Optional[float]
    difficulty: Optional[float]
    due: datetime
    last_review: Optional[datetime]

    model_config = ConfigDict(alias_generator=lambda s: ''.join(['_' + c.lower() if c.isupper() else c for c in s]).lstrip('_'), populate_by_name=True)

class ReviewCardRequestDto(BaseModel):
    rating: int
    review_datetime: datetime
    card_data: CardData
