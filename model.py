import csv

class DataStorage:
    FILE_PATH = 'model/cow.csv'  # ตรวจสอบให้แน่ใจว่าเส้นทางนี้ถูกต้อง

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
        # การดำเนินการเมื่อพบแพะสามารถเพิ่มได้ตามต้องการ เช่น การส่งกลับไปที่ภูเขา
        print("พบแพะในระบบ ให้เตรียมส่งกลับไปที่ภูเขา")



# Test the loading function
if __name__ == '__main__':
    data = DataStorage.load_file()  # Correctly calling the static method directly from the class
    print(data)


