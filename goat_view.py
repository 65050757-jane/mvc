
import tkinter as tk
from tkinter import ttk

class GoatView:
    def __init__(self, root):
        self.root = root

    def show_goat_view(self):
        goat_window = tk.Toplevel(self.root)
        goat_window.title("ไล่แพะออกไป")
        self.center_window(goat_window, 350, 150)
        goat_window.configure(bg="#FFEBEE")

        frame = ttk.Frame(goat_window, padding=20, style="My.TFrame")
        frame.pack(fill='both', expand=True)

        tk.Label(frame, text="พบแพะในระบบ!", font=("Arial", 14), bg="#FFEBEE", fg="#C62828").pack(pady=10)
        ttk.Button(frame, text="ไล่แพะออกไป", command=goat_window.destroy, style="TButton").pack(pady=10)

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')
