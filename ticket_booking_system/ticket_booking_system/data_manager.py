import json
import os

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                return json.load(f)
        return {}

    def save_data(self):
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4)

    def get_booked_seats(self, movie):
        return self.data.get(movie, {}).get("booked_seats", [])

    def add_ticket(self, movie, ticket_info):
        self.data.setdefault(movie, {"booked_seats": [], "tickets": []})
        self.data[movie]["booked_seats"].extend(ticket_info["seats"])
        self.data[movie]["tickets"].append(ticket_info)
        self.save_data()

    def delete_ticket(self, movie, ticket_id):
        movie_info = self.data.get(movie)
        if not movie_info:
            return False

        for t in movie_info["tickets"]:
            if t["ticket_id"] == ticket_id:
                for seat in t["seats"]:
                    if seat in movie_info["booked_seats"]:
                        movie_info["booked_seats"].remove(seat)
                movie_info["tickets"].remove(t)
                self.save_data()
                return True
        return False
