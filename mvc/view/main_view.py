import tkinter as tk
from tkinter import messagebox

class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("ค้นหาวัวในระบบ")
        self.root.geometry("600x400")
        self.center_window(self.root, 600, 400)

    def create_window(self):
        # ส่วนของการรับรหัสวัว
        self.label = tk.Label(self.root, text="กรุณากรอกรหัสวัว:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.root, justify='center')
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

    def reset_view(self):
        """
        Reset the input field to allow new input.
        """
        self.entry.delete(0, 'end')  # เคลียร์ข้อมูลในช่องอินพุต

    def center_window(self, window, width, height):
        """
        Center the window on the screen.
        """
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

class CowView:
    def __init__(self, root):
        self.root = root

    def show_milking_view(self, cow, can_milk, on_milk_button_click):
        # แสดงหน้าจอให้ผู้ใช้กดปุ่มรีดนมก่อน
        milking_window = tk.Toplevel(self.root)
        milking_window.title("รีดนมวัว")
        self.center_window(milking_window, 300, 200)

        tk.Label(milking_window, text="กดปุ่มเพื่อเริ่มการรีดนม", anchor='center').pack(pady=10)
        milk_button = tk.Button(milking_window, text="รีดนม", command=lambda: on_milk_button_click())
        milk_button.pack(pady=5)

    def center_window(self, window, width, height):
        """
        Center the window on the screen.
        """
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

class GoatView:
    def __init__(self, root):
        self.root = root

    def show_goat_view(self):
        # แสดงผลในกรณีที่เป็นแพะ พร้อมปุ่มสำหรับไล่แพะออกไป
        goat_window = tk.Toplevel(self.root)
        goat_window.title("ไล่แพะออกไป")
        self.center_window(goat_window, 300, 150)

        tk.Label(goat_window, text="พบแพะในระบบ!", anchor='center').pack(pady=10)
        tk.Button(goat_window, text="ไล่แพะออกไป", command=goat_window.destroy).pack(pady=5)

    def center_window(self, window, width, height):
        """
        Center the window on the screen.
        """
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')
