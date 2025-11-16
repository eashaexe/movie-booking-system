from datetime import datetime

def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def format_currency(amount):
    return f"rupees {amount:.2f}"
