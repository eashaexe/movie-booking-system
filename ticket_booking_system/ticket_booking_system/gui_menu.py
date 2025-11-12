import tkinter as tk
from tkinter import ttk
from gui_booking import BookingPage
from gui_ticket_view import TicketViewer

class MenuPage:
    def __init__(self, root, data_manager):
        self.root = root
        self.data_manager = data_manager
        self.create_menu()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_menu(self):
        self.clear()
        tk.Label(self.root, text="🎬 Ticket Booking System", font=("Arial", 18, "bold")).pack(pady=20)

        ttk.Button(self.root, text="Book Ticket", command=self.open_booking).pack(pady=10)
        ttk.Button(self.root, text="View/Delete Ticket", command=self.open_viewer).pack(pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def open_booking(self):
        BookingPage(self.root, self.data_manager, self.create_menu)

    def open_viewer(self):
        TicketViewer(self.root, self.data_manager, self.create_menu)
