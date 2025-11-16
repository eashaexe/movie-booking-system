 import random
from datetime import datetime, timedelta
from utils import format_datetime

# --- Constants for Calculation (Add these to the top of your file) ---
# NOTE: In a real system, these would ideally be loaded from a configuration or database.
TICKET_PRICE = 12.50  # Base price per ticket
MEAL_PLAN_PRICES = {
    "None": 0.00,
    "Small Popcorn & Drink": 7.50,
    "Large Combo": 15.00
}
# ---------------------------------------------------------------------

def create_ticket(name, movie, seats, duration_minutes, meal_plan_name="None"):
    """
    Creates a ticket dictionary including movie duration, meal plan, and calculated total amount.
    """
    
    # --- 1. Calculate Total Amount ---
    
    # Calculate base price based on number of seats
    base_amount = len(seats) * TICKET_PRICE
    
    # Get meal plan cost, defaulting to 0.00 if the plan name is not found
    meal_plan_cost = MEAL_PLAN_PRICES.get(meal_plan_name, 0.00)
    
    # Calculate final total amount
    total_amount = base_amount + meal_plan_cost

    # --- 2. Generate Ticket Details ---
    
    showtime = datetime.now() + timedelta(minutes=1) # 1 minute validity (for demo)
    ticket_id = f"T{random.randint(1000,9999)}"
    
    return {
        "ticket_id": ticket_id,
        "name": name,
        "movie": movie,
        "seats": seats,
        "showtime": format_datetime(showtime),
        
        # --- New Fields Added ---
        "duration_minutes": duration_minutes,
        "meal_plan": meal_plan_name,
        "total_amount": round(total_amount, 2)  # Round to 2 decimal places for currency
    }

# --- REMEMBER TO SAVE THIS FILE! ---