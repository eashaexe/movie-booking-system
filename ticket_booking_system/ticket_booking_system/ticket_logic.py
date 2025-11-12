import random
from datetime import datetime, timedelta
from utils import format_datetime

def create_ticket(name, movie, seats):
    showtime = datetime.now() + timedelta(minutes=1)  # 1 minute validity (for demo)
    ticket_id = f"T{random.randint(1000,9999)}"
    return {
        "ticket_id": ticket_id,
        "name": name,
        "movie": movie,
        "seats": seats,
        "showtime": format_datetime(showtime)
    }
