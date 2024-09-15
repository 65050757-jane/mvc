from model import DataStorage
from view.view import MainView, CowView, GoatView
import tkinter as tk
from tkinter import messagebox

class MainController:
    def __init__(self):
        self.root = tk.Tk()
        self.main_view = MainView(self.root, self)
        self.cow_view = CowView(self.root)
        self.goat_view = GoatView(self.root)
        self.main_view.create_window()
        self.data_storage = DataStorage()  # สร้างอินสแตนซ์ของ DataStorage สำหรับการโหลดข้อมูล
        self.root.mainloop()

    def check_cow_in_system(self, cow_id):
        """
        ตรวจสอบว่ามีวัวหรือแพะในระบบหรือไม่โดยใช้รหัส
        """
        data = self.data_storage.load_file()  # โหลดข้อมูลวัวจาก DataStorage
        animal = next((cow for cow in data if cow['ID'] == cow_id), None)  # ค้นหาวัวหรือแพะจากข้อมูล

        if not animal:
            messagebox.showerror("ข้อผิดพลาด", "ไม่พบวัวหรือแพะในระบบ")
        elif animal['Type'] == 'Cow':
            self.cow_view.show_milking_view(animal)
        elif animal['Type'] == 'Goat':
            self.goat_view.show_goat_view()

class GoatController:
    pass

class CowController:
    pass


if __name__ == '__main__':
    controller = MainController()
    