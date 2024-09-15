import csv

#class for loading FILE
class cowModel:
    pass

class changeCow:
    pass

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
            # Open the file in read mode and load the data
            with open(DataStorage.FILE_PATH, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Convert relevant fields to appropriate data types
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


# Test the loading function
# Test the loading function
if __name__ == '__main__':
    data = DataStorage.load_file()  # Correctly calling the static method directly from the class
    print(data)


