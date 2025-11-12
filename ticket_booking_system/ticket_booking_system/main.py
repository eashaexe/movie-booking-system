import tkinter as tk
from gui_menu import MenuPage
from data_manager import DataManager

if __name__ == "__main__":
    root = tk.Tk()
    root.title("🎟️ Ticket Booking System")
    root.geometry("500x400")
    data_manager = DataManager("tickets.json")
    MenuPage(root, data_manager)
    root.mainloop()
