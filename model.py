import csv
import random
from tkinter import messagebox

class DataStorage:
    FILE_PATH = 'model/cow.csv'  # Updated file path for saving changes

    @staticmethod
    def load_file():
        """
        Load animal data from the CSV file.
        Returns a list of dictionaries representing each animal.
        """
        data = []
        try:
            with open(DataStorage.FILE_PATH, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    row['Age (Years)'] = int(float(row['Age (Years)'])) if row['Age (Years)'] else None
                    row['Age (Months)'] = int(float(row['Age (Months)'])) if row['Age (Months)'] else None
                    row['Number of Teats'] = int(float(row['Number of Teats'])) if row['Number of Teats'] else None
                    data.append(row)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("ไม่พบไฟล์ข้อมูล")
        except UnicodeDecodeError:
            print("เกิดข้อผิดพลาดในการอ่านไฟล์: การเข้ารหัสไม่ถูกต้อง")
        except Exception as e:
            print(f"An error occurred: {e}")
        return data

    @staticmethod
    def save_file(data):
        """
        Save the updated data back to the CSV file.
        """
        headers = ['ID', 'Type', 'Age (Years)', 'Age (Months)', 'Date of Birth', 'Number of Teats']
        try:
            with open(DataStorage.FILE_PATH, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
            print("Data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

class CowModel:
    @staticmethod
    def can_be_milked(cow):
        """
        ตรวจสอบว่าจำนวนเต้านมของวัวมี 4 เต้าหรือไม่
        """
        return cow['Number of Teats'] == 4

    @staticmethod
    def calculate_milk_production(cow):
        """
        คำนวณจำนวนน้ำนมที่ผลิตได้ในรอบนั้น โดยจำนวนน้ำนมวัวจะเท่ากับจำนวนปีในอายุของวัว
        บวกด้วยจำนวนเดือนในอายุของวัว หน่วยเป็นลิตร
        """
        age_years = cow.get('Age (Years)', 0)
        age_months = cow.get('Age (Months)', 0)
        return age_years + age_months


class GoatModel:
    @staticmethod
    def handle_goat():
        """
        การดำเนินการเมื่อพบแพะในระบบ
        """
        print("พบแพะในระบบ ให้เตรียมส่งกลับไปที่ภูเขา")

class CowStatusChanger:
    @staticmethod
    def attempt_teat_change(cow, data, show_recovery_popup=False):
        """
        Attempt to change the number of teats based on specific conditions and save changes to CSV:
        - If the cow has 4 teats and is milked, there is a 5% chance to reduce teats to 3.
        - If the cow has 3 teats, there is a 20% chance to recover to 4 teats.
        """
        updated = False
        if cow['Number of Teats'] == 4:
            # 5% chance that teats reduce to 3
            if random.random() < 0.05:
                cow['Number of Teats'] -= 1
                updated = True
                messagebox.showinfo("รีดนม", "เต้านมของวัวลดลงเหลือ 3 เต้าเนื่องจากการรีดนม")
        elif cow['Number of Teats'] == 3:
            # 20% chance that teats increase to 4
            if random.random() < 0.20:
                cow['Number of Teats'] += 1
                updated = True
                if show_recovery_popup:
                    messagebox.showinfo("การฟื้นตัว", "วัวกลับมามี 4 เต้าเนื่องจากการฟื้นตัว")

        # Update the data in the CSV if changes occurred
        if updated:
            # Save the updated data back to the CSV file by ensuring the cow object is correctly referenced in the data list
            for index, animal in enumerate(data):
                if animal['ID'] == cow['ID']:
                    data[index] = cow  # Update the exact cow in the data list
                    break
            DataStorage.save_file(data)


# Example of calling CowStatusChanger with the correct data parameter
data = DataStorage.load_file()
if data:
    cow = data[0]  # Example: Using the first cow in the data
    CowStatusChanger.attempt_teat_change(cow, data)  # Passing the data list correctly
