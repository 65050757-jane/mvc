import csv

#class for loading FILE
class DataStorage:
    FILE_PATH = 'model/cow.csv'

    def load_file():
        data = []
        try:
            with open(DataStorage.FILE_PATH, newline='', encoding='utf-8') as csvfile:
                pass
        except FileNotFoundError:
            print("ไม่พบไฟล์ข้อมูล")
        except UnicodeDecodeError:
            print("เกิดข้อผิดพลาดในการอ่านไฟล์: การเข้ารหัสไม่ถูกต้อง")
        return data

# Test the loading function
if __name__ == '__main__':
    data_storage = DataStorage()
    data = data_storage.load_file()

