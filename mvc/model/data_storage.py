
import csv

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

    @staticmethod
    def save_file(data):
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
