
import tkinter as tk
from tkinter import messagebox
from view.main_view import MainView
from view.cow_view import CowView
from view.goat_view import GoatView
from model.data_storage import DataStorage
from model.cow_model import CowModel
from model.goat_model import GoatModel
from model.cow_status_changer import CowStatusChanger

class MainController:
    def __init__(self):
        self.root = tk.Tk()
        self.main_view = MainView(self.root, self)
        self.cow_view = CowView(self.root)
        self.goat_view = GoatView(self.root)
        self.main_view.create_window()
        self.data_storage = DataStorage()
        self.total_milk = 0
        self.root.mainloop()

    def check_cow_in_system(self, cow_id):
        data = self.data_storage.load_file()
        animal = next((cow for cow in data if cow['ID'] == cow_id), None)

        if not animal:
            messagebox.showerror("ข้อผิดพลาด", "ไม่พบวัวหรือแพะในระบบ")
        elif animal['Type'] == 'Cow':
            self.handle_cow(animal, data)
        elif animal['Type'] == 'Goat':
            self.handle_goat()

    def handle_cow(self, cow, data):
        can_milk = CowModel.can_be_milked(cow)
        self.cow_view.show_milking_view(cow, can_milk, lambda: self.perform_milking(cow, can_milk, data))

    def perform_milking(self, cow, can_milk, data):
        CowStatusChanger.attempt_teat_change(cow, data)

        if can_milk:
            milk_produced = CowModel.calculate_milk_production(cow)
            self.total_milk += milk_produced
            messagebox.showinfo("ผลิตน้ำนม", f"วัวผลิตน้ำนมได้ {milk_produced} ลิตรในรอบนี้")
        else:
            messagebox.showinfo("ไม่สามารถรีดนมได้", "วัวไม่สมบูรณ์ไม่สามารถรีดนมได้")

        messagebox.showinfo("ผลรวมการผลิตน้ำนม", f"น้ำนมทั้งหมดที่ผลิตได้: {self.total_milk} ลิตร")
        self.main_view.reset_view()

    def handle_goat(self):
        GoatModel.handle_goat()
        self.goat_view.show_goat_view()
