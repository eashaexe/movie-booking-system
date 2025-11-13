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
        self.selected_time = tk.StringVar()
        self.show_movie_options()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_movie_options(self):
        self.clear()
        tk.Label(self.root, text="🎬 Choose a Movie", font=("Arial", 16, "bold")).pack(pady=10)
        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        self.movies = random.sample(MOVIES, 5)
        self.selected_movie = tk.StringVar(value=self.movies[0])

        for m in self.movies:
            movie_frame = tk.Frame(frame, borderwidth=1, relief="solid", padx=8, pady=5)
            movie_frame.pack(pady=3, fill="x", padx=10)
            tk.Radiobutton(movie_frame, text=m, variable=self.selected_movie, value=m).pack(anchor="w")
            # Fake movie info section
            tk.Label(movie_frame, text=f"Genre: {random.choice(['Action', 'Comedy', 'Drama', 'Sci-Fi'])} | "
                                       f"Duration: {random.choice([100, 120, 140])} min | "
                                       f"Rating: ⭐ {random.uniform(3, 5):.1f}/5", fg="gray").pack(anchor="w")

        ttk.Button(self.root, text="Next →", command=self.show_time_options).pack(pady=15)
        ttk.Button(self.root, text="⬅ Back", command=self.go_back).pack()

    def show_time_options(self):
        self.clear()
        tk.Label(self.root, text=f"🕒 Select Showtime for '{self.selected_movie.get()}'", font=("Arial", 14, "bold")).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        time_slots = ["10:00 AM", "1:30 PM", "4:00 PM", "7:00 PM", "10:00 PM"]
        for t in time_slots:
            ttk.Radiobutton(frame, text=t, variable=self.selected_time, value=t).pack(anchor="w")

        ttk.Button(self.root, text="Next →", command=self.show_seats).pack(pady=15)
        ttk.Button(self.root, text="⬅ Back", command=self.show_movie_options).pack()

    def show_seats(self):
        if not self.selected_time.get():
            messagebox.showwarning("No Time Selected", "Please choose a showtime first.")
            return

        self.clear()
        movie = self.selected_movie.get()
        tk.Label(self.root, text=f"🎟️ Select Seats for {movie}\nShowtime: {self.selected_time.get()}",
                 font=("Arial", 14, "bold")).pack(pady=10)
        frame = tk.Frame(self.root)
        frame.pack()

        self.selected_seats = []
        self.booked_seats = self.data_manager.get_booked_seats(movie)

        # Seat grid
        for i in range(5):
            for j in range(5):
                seat = f"{chr(65+i)}{j+1}"
                btn = tk.Button(frame, text=seat, width=4, height=1,
                                command=lambda s=seat: self.select_seat(s))
                btn.grid(row=i, column=j, padx=5, pady=5)
                if seat in self.booked_seats:
                    btn.config(state="disabled", bg="red")
                else:
                    btn.config(bg="lightgreen")

        # Selected seats label
        self.selection_label = tk.Label(self.root, text="Selected Seats: None", font=("Arial", 12))
        self.selection_label.pack(pady=5)

        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        ttk.Button(control_frame, text="Confirm Booking ✅", command=self.confirm_booking).grid(row=0, column=0, padx=5)
        ttk.Button(control_frame, text="Reset Selection 🔄", command=self.reset_selection).grid(row=0, column=1, padx=5)
        ttk.Button(self.root, text="⬅ Back", command=self.show_time_options).pack()

    def select_seat(self, seat):
        if seat in self.selected_seats:
            self.selected_seats.remove(seat)
        else:
            self.selected_seats.append(seat)
        self.selection_label.config(
            text=f"Selected Seats: {', '.join(self.selected_seats) if self.selected_seats else 'None'}"
        )

    def reset_selection(self):
        self.selected_seats = []
        self.show_seats()

    def confirm_booking(self):
        if not self.selected_seats:
            messagebox.showwarning("No Seat Selected", "Please select at least one seat.")
            return

        name = simpledialog.askstring("Name", "Enter your name:")
        if not name:
            return

        movie = self.selected_movie.get()
        ticket_info = create_ticket(name, movie, self.selected_seats)
        self.data_manager.add_ticket(movie, ticket_info)

        self.show_ticket_summary(ticket_info)

    def show_ticket_summary(self, ticket_info):
        self.clear()
        tk.Label(self.root, text="🎫 Booking Confirmed!", font=("Arial", 16, "bold"), fg="green").pack(pady=10)
        tk.Label(self.root, text=f"Ticket ID: {ticket_info['ticket_id']}", font=("Arial", 12)).pack()
        tk.Label(self.root, text=f"Movie: {ticket_info['movie']}", font=("Arial", 12)).pack()
        tk.Label(self.root, text=f"Seats: {', '.join(ticket_info['seats'])}", font=("Arial", 12)).pack()
        tk.Label(self.root, text=f"Showtime: {self.selected_time.get()}", font=("Arial", 12)).pack(pady=5)

        ttk.Button(self.root, text="🏠 Back to Main Menu", command=self.go_back).pack(pady=15)

