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
        self.total_milk = 0  # Track total milk production
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
            self.handle_cow(animal, data)
        elif animal['Type'] == 'Goat':
            self.handle_goat()

    def handle_cow(self, cow, data):
        """
        ตรวจสอบและแสดงผลการรีดนมของวัว รวมถึงการจัดการเปลี่ยนแปลงเต้านมและการคำนวณปริมาณน้ำนมที่ผลิตได้
        """
        # เรียกหน้าจอรีดนมขึ้นมาก่อน
        can_milk = CowModel.can_be_milked(cow)
        self.cow_view.show_milking_view(cow, can_milk, lambda: self.perform_milking(cow, can_milk, data))

    def perform_milking(self, cow, can_milk, data):
        """
        ฟังก์ชันเพื่อดำเนินการรีดนมและคำนวณน้ำนมหลังจากผู้ใช้กดปุ่มรีดนม
        """
        if can_milk:
            # คำนวณปริมาณน้ำนมที่ผลิตได้ก่อนที่จะเปลี่ยนแปลงเต้านม
            milk_produced = CowModel.calculate_milk_production(cow)
            self.total_milk += milk_produced
            messagebox.showinfo("ผลิตน้ำนม", f"วัวผลิตน้ำนมได้ {milk_produced} ลิตรในรอบนี้")

        # จัดการการเปลี่ยนแปลงของเต้านมหลังจากการรีดนม
        CowStatusChanger.attempt_teat_change(cow, data)

        if not can_milk:
            messagebox.showinfo("ไม่สามารถรีดนมได้", "วัวไม่สมบูรณ์ไม่สามารถรีดนมได้")

        # แสดงผลรวมของน้ำนมที่ผลิตได้และรีเซ็ตหน้าจอเพื่อรับรหัสวัวใหม่
        messagebox.showinfo("ผลรวมการผลิตน้ำนม", f"น้ำนมทั้งหมดที่ผลิตได้: {self.total_milk} ลิตร")
        self.main_view.reset_view()  # รีเซ็ตหน้าจอให้พร้อมรับรหัสวัวใหม่



    def handle_goat(self):
        """
        แสดงผลในกรณีที่เป็นแพะ
        """
        GoatModel.handle_goat()
        self.goat_view.show_goat_view()

# Run the program
if __name__ == '__main__':
    controller = MainController()

    