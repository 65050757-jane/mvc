
import random
from tkinter import messagebox
from model.data_storage import DataStorage

class CowStatusChanger:
    @staticmethod
    def attempt_teat_change(cow, data):
        updated = False
        if cow['Number of Teats'] == 4:
            if random.random() < 0.05:
                cow['Number of Teats'] -= 1
                updated = True
                messagebox.showinfo("รีดนม", "เต้านมของวัวลดลงเหลือ 3 เต้าเนื่องจากการรีดนม")
        elif cow['Number of Teats'] == 3:
            if random.random() < 0.20:
                cow['Number of Teats'] += 1
                updated = True
                messagebox.showinfo("การฟื้นตัว", "วัวกลับมามี 4 เต้าเนื่องจากการฟื้นตัว")

        if updated:
            for index, animal in enumerate(data):
                if animal['ID'] == cow['ID']:
                    data[index] = cow
                    break
            DataStorage.save_file(data)
