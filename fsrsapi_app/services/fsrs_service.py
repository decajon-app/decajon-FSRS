import datetime
from fsrs import Scheduler, Card, Rating

scheduler = Scheduler()

def process_review(card_data: dict, rating: int, review_datetime: datetime) -> dict:
    card = Card.from_dict(card_data)
    reviewed_card, _ = scheduler.review_card(card=card, rating=Rating(rating), review_datetime=review_datetime)
    return reviewed_card.to_dict()

def init_card(card_id: int) -> dict:
    new_card = Card(card_id = card_id)
    return new_card