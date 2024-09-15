
import tkinter as tk
from tkinter import ttk

class CowView:
    def __init__(self, root):
        self.root = root

    def show_milking_view(self, cow, can_milk, on_milk_button_click):
        milking_window = tk.Toplevel(self.root)
        milking_window.title("รีดนมวัว")
        self.center_window(milking_window, 350, 200)
        milking_window.configure(bg="#E0F7FA")

        frame = ttk.Frame(milking_window, padding=20, style="My.TFrame")
        frame.pack(fill='both', expand=True)

        tk.Label(frame, text="กดปุ่มเพื่อเริ่มการรีดนม", font=("Arial", 14), bg="#E0F7FA", fg="#004D40").pack(pady=10)
        milk_button = ttk.Button(frame, text="รีดนม", command=lambda: on_milk_button_click(), style="TButton")
        milk_button.pack(pady=10)

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')
