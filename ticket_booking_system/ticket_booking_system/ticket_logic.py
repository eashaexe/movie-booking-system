import random
from datetime import datetime, timedelta
from utils import format_datetime

TICKET_VALIDITY_MINUTES = 15   # You can change validity time here

def create_ticket(name, movie, seats):
    """
    Creates a new ticket with a unique ID and calculates expiry based on showtime.
    """

    showtime = datetime.now() + timedelta(minutes=TICKET_VALIDITY_MINUTES)

    ticket_id = f"T{random.randint(1000, 9999)}"

    return {
        "ticket_id": ticket_id,
        "name": name,
        "movie": movie,
        "seats": seats,
        "showtime": format_datetime(showtime),
        "expires_in_minutes": TICKET_VALIDITY_MINUTES
    }
