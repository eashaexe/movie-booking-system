import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
from movie_data import MOVIES
from ticket_logic import create_ticket

class BookingPage:
    def __init__(self, root, data_manager, go_back):
        self.root = root
        self.data_manager = data_manager
        self.go_back = go_back
        self.booked_seats = []
        self.selected_movie = None
        self.selected_seats = []
        self.show_movie_options()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_movie_options(self):
        self.clear()
        tk.Label(self.root, text="🎥 Choose a Movie", font=("Arial", 14)).pack(pady=10)
        self.movies = random.sample(MOVIES, 5)
        self.selected_movie = tk.StringVar(value=self.movies[0])

        for m in self.movies:
            tk.Radiobutton(self.root, text=m, variable=self.selected_movie, value=m).pack(anchor="w")

        ttk.Button(self.root, text="Next", command=self.show_seats).pack(pady=15)
        ttk.Button(self.root, text="Back", command=self.go_back).pack()

    def show_seats(self):
        self.clear()
        movie = self.selected_movie.get()
        tk.Label(self.root, text=f"🎟️ Select Seats for {movie}", font=("Arial", 14)).pack(pady=10)
        frame = tk.Frame(self.root)
        frame.pack()

        self.selected_seats = []
        self.booked_seats = self.data_manager.get_booked_seats(movie)

        for i in range(5):
            for j in range(5):
                seat = f"{chr(65+i)}{j+1}"
                btn = tk.Button(frame, text=seat, width=4,
                                command=lambda s=seat: self.select_seat(s))
                btn.grid(row=i, column=j, padx=5, pady=5)
                if seat in self.booked_seats:
                    btn.config(state="disabled", bg="red")
                else:
                    btn.config(bg="lightgreen")

        ttk.Button(self.root, text="Confirm Booking", command=self.confirm_booking).pack(pady=10)
        ttk.Button(self.root, text="Back", command=self.show_movie_options).pack()

    def select_seat(self, seat):
        if seat in self.selected_seats:
            self.selected_seats.remove(seat)
        else:
            self.selected_seats.append(seat)

    def confirm_booking(self):
        if not self.selected_seats:
            messagebox.showwarning("No seat", "Please select at least one seat.")
            return
        name = simpledialog.askstring("Name", "Enter your name:")
        if not name:
            return

        movie = self.selected_movie.get()
        ticket_info = create_ticket(name, movie, self.selected_seats)
        self.data_manager.add_ticket(movie, ticket_info)

        messagebox.showinfo("Booking Successful",
                            f"🎟️ Ticket ID: {ticket_info['ticket_id']}\nMovie: {movie}\nSeats: {', '.join(self.selected_seats)}")
        self.go_back()
