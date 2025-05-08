from datetime import datetime, timezone
from fsrs import Scheduler, Card, Rating

scheduler = Scheduler()

def process_review(card_data: dict, rating: int, review_datetime: datetime) -> dict:
    # Asegurar que 'due' y 'last_review' sean cadenas ISO 8601 válidas
    card_data["due"] = card_data["due"].replace("Z", "+00:00")
    if card_data.get("last_review"):
        card_data["last_review"] = card_data["last_review"].replace("Z", "+00:00")

    # Establecer valores predeterminados para 'stability' y 'difficulty' si son None
    if card_data.get("stability") is None:
        card_data["stability"] = 1.0  # Valor predeterminado sugerido
    if card_data.get("difficulty") is None:
        card_data["difficulty"] = 1.0  # Valor predeterminado sugerido

    review_datetime = datetime.now(timezone.utc)

    print("Card antes de: ", card_data)
    card = Card.from_dict(card_data)
    print("from_dict exitoso")
    
    print("Antes de review: ", card)
    reviewed_card, _ = scheduler.review_card(
        card=card,
        rating=Rating(rating),
        review_datetime=review_datetime
    )
    print("Despues de review: ", reviewed_card)
    return reviewed_card.to_dict()

def init_card(card_id: int) -> dict:
    new_card = Card(card_id = card_id, step=0, stability=1.0, difficulty=1.0)
    return new_card