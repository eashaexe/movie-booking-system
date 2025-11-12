import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class TicketViewer:
    def __init__(self, root, data_manager, go_back):
        self.root = root
        self.data_manager = data_manager
        self.go_back = go_back
        self.show_tickets()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_tickets(self):
        self.clear()
        tk.Label(self.root, text="🎫 View / Delete Tickets", font=("Arial", 14)).pack(pady=10)
        tree = ttk.Treeview(self.root, columns=("ID", "Name", "Movie", "Seats", "Showtime", "Status"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(pady=10, fill="both", expand=True)

        now = datetime.now()
        for movie, info in self.data_manager.data.items():
            for t in info.get("tickets", []):
                showtime = datetime.strptime(t["showtime"], "%Y-%m-%d %H:%M:%S")
                status = "Valid" if showtime > now else "Expired"
                tree.insert("", "end", values=(t["ticket_id"], t["name"], t["movie"], ", ".join(t["seats"]), t["showtime"], status))

        ttk.Button(self.root, text="Delete Ticket", command=lambda: self.delete_ticket(tree)).pack(pady=5)
        ttk.Button(self.root, text="Back", command=self.go_back).pack()

    def delete_ticket(self, tree):
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Select", "Please select a ticket to delete.")
            return

        values = tree.item(selected[0], "values")
        ticket_id = values[0]
        movie = values[2]
        success = self.data_manager.delete_ticket(movie, ticket_id)

        if success:
            messagebox.showinfo("Deleted", "Ticket deleted successfully.")
            self.show_tickets()
        else:
            messagebox.showwarning("Error", "Ticket not found.")
