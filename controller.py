from model import DataStorage, CowModel, GoatModel, CowStatusChanger
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
            self.handle_cow(animal)
        elif animal['Type'] == 'Goat':
            self.handle_goat()

    def handle_cow(self, cow):
        """
        ตรวจสอบและแสดงผลการรีดนมของวัว รวมถึงการจัดการเปลี่ยนแปลงเต้านม
        """
        if CowModel.can_be_milked(cow):
            self.cow_view.show_milking_view(cow, can_milk=True)
            CowStatusChanger.attempt_teat_change(cow)  # เรียกใช้การเปลี่ยนแปลงจำนวนเต้านมหลังการรีดนม
        else:
            self.cow_view.show_milking_view(cow, can_milk=False)
            CowStatusChanger.attempt_teat_change(cow)  # เรียกใช้การเปลี่ยนแปลงในกรณีที่วัวมี 3 เต้า

    def handle_goat(self):
        """
        แสดงผลในกรณีที่เป็นแพะ
        """
        GoatModel.handle_goat()
        self.goat_view.show_goat_view()




if __name__ == '__main__':
    controller = MainController()
    