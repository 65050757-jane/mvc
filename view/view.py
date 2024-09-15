import tkinter as tk
from tkinter import messagebox

class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("ค้นหาวัวในระบบ")
        self.root.geometry("600x400")

    def create_window(self):
        # ส่วนของการรับรหัสวัว
        self.label = tk.Label(self.root, text="กรุณากรอกรหัสวัว:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="ค้นหา", command=self.search_cow)
        self.submit_button.pack(pady=5)

    def search_cow(self):
        # ดึงค่ารหัสวัวจาก Entry และส่งไปยัง Controller
        cow_id = self.entry.get()  # ดึงค่าจากช่องอินพุต

        # ตรวจสอบเงื่อนไขตามที่กำหนด
        if not cow_id.isdigit():
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขเท่านั้น")
        elif len(cow_id) != 8:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลข 8 หลัก")
        elif cow_id[0] == '0':
            messagebox.showerror("ข้อผิดพลาด", "รหัสไม่สามารถขึ้นต้นด้วยเลข 0")
        else:
            self.controller.check_cow_in_system(cow_id)  # ส่งค่ารหัสวัวไปตรวจสอบใน Controller

class CowView:
    def __init__(self, root):
        self.root = root

    def show_milking_view(self, cow):
        # แสดงผลสำหรับการรีดนมวัว
        milking_window = tk.Toplevel(self.root)
        milking_window.title("รีดนมวัว")
        if cow['Number of Teats'] == 4:
            tk.Label(milking_window, text="วัวสามารถรีดนมได้").pack(pady=10)
        else:
            tk.Label(milking_window, text="วัวไม่สมบูรณ์ไม่สามารถรีดนมได้").pack(pady=10)
        tk.Button(milking_window, text="ปิด", command=milking_window.destroy).pack(pady=5)

class GoatView:
    def __init__(self, root):
        self.root = root

    def show_goat_view(self):
        # แสดงผลในกรณีที่เป็นแพะ พร้อมปุ่มสำหรับไล่แพะออกไป
        goat_window = tk.Toplevel(self.root)
        goat_window.title("ไล่แพะออกไป")
        tk.Label(goat_window, text="พบแพะในระบบ!").pack(pady=10)
        tk.Button(goat_window, text="ไล่แพะออกไป", command=goat_window.destroy).pack(pady=5)
