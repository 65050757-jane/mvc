import tkinter as tk

class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("")
        self.root.geometry("600x400")

    def create_window(self):
        # ส่วนของการรับรหัสวัว
        self.label = tk.Label(self.root, text="กรุณากรอกรหัสวัว:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

class CowView:
    pass
class GoatView:
    pass

