import csv
import random

class DataStorage:
    FILE_PATH = 'model/cow.csv'

    @staticmethod
    def load_file():
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


class CowModel:
    @staticmethod
    def can_be_milked(cow):
        """
        ตรวจสอบว่าจำนวนเต้านมของวัวมี 4 เต้าหรือไม่
        """
        return cow['Number of Teats'] == 4


class GoatModel:
    @staticmethod
    def handle_goat():
        """
        การดำเนินการเมื่อพบแพะในระบบ
        """
        print("พบแพะในระบบ ให้เตรียมส่งกลับไปที่ภูเขา")


class CowStatusChanger:
    @staticmethod
    def attempt_teat_change(cow):
        """
        พิจารณาการเปลี่ยนแปลงจำนวนเต้านมของวัวตามเงื่อนไข:
        - ถ้าวัวมี 4 เต้าและถูกรีดนม มีโอกาส 5% ที่จะลดลง 1 เต้า
        - ถ้าวัวมี 3 เต้า มีโอกาส 20% ที่จะเพิ่มกลับมาเป็น 4 เต้า
        """
        if cow['Number of Teats'] == 4:
            # โอกาส 5% ที่เต้านมจะลดลง 1 เต้า
            if random.random() < 0.05:
                cow['Number of Teats'] -= 1
                print("เต้านมของวัวลดลงเหลือ 3 เต้าเนื่องจากการรีดนม")
        elif cow['Number of Teats'] == 3:
            # โอกาส 20% ที่เต้านมจะเพิ่มกลับมาเป็น 4 เต้า
            if random.random() < 0.20:
                cow['Number of Teats'] += 1
                print("วัวกลับมามี 4 เต้าเนื่องจากการฟื้นตัว")
