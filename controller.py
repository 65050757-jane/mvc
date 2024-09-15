# main_controller.py
from model import DataStorage  # ตรวจสอบให้แน่ใจว่า path นี้ถูกต้องตามโครงสร้างโฟลเดอร์
from view.view import MainView
import tkinter as tk


class MainController:
    def __init__(self):
        self.root = tk.Tk()
        self.main_view = MainView(self.root, self)
        self.main_view.create_window()
        self.data_storage = DataStorage()  # สร้างอินสแตนซ์ของ DataStorage สำหรับการโหลดข้อมูล
        self.root.mainloop()

    def check_cow_in_system(self, cow_id):
        """
        ตรวจสอบว่ามีวัวในระบบหรือไม่โดยใช้รหัสวัว
        """
        data = self.data_storage.load_file()  # โหลดข้อมูลวัวจาก DataStorage
        cow_exists = any(cow['ID'] == cow_id for cow in data)  # ตรวจสอบว่ารหัสวัวตรงกับข้อมูลใดในระบบหรือไม่

        if cow_exists:
            print("วัวที่มีรหัสนี้อยู่ในระบบ")
        else:
            print("ไม่พบวัวในระบบ")   
  
 
class GoatController:
    pass

class CowController:
    pass


if __name__ == '__main__':
    controller = MainController()
    