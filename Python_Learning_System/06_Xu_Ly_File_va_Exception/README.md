# Module 6: Xử Lý File và Exception 📁

## 🎯 Mục Tiêu
- Đọc/ghi file text
- Làm việc với CSV, JSON
- Xử lý ngoại lệ (Exception)

## 1. Đọc/Ghi File Text

```python
# Ghi file
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Dòng 1\n")
    file.write("Dòng 2\n")

# Đọc toàn bộ
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Đọc từng dòng
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Đọc thành list
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Thêm vào file (append)
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Dòng 3\n")
```

## 2. Làm Việc Với CSV

```python
import csv

# Ghi CSV
data = [
    ["Tên", "Tuổi", "Thành phố"],
    ["An", 25, "Hà Nội"],
    ["Bình", 30, "TP.HCM"]
]

with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Đọc CSV
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# CSV với dictionary
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Tên"], row["Tuổi"])
```

## 3. Làm Việc Với JSON

```python
import json

# Dictionary -> JSON file
data = {
    "name": "An",
    "age": 25,
    "skills": ["Python", "Java", "C++"]
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

# JSON file -> Dictionary
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data["name"])

# Dictionary -> JSON string
json_string = json.dumps(data, ensure_ascii=False)
print(json_string)

# JSON string -> Dictionary
data = json.loads(json_string)
```

## 4. Exception Handling

```python
# Try-except cơ bản
try:
    number = int(input("Nhập số: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Vui lòng nhập số!")
except ZeroDivisionError:
    print("Không thể chia cho 0!")

# Try-except-else-finally
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File không tồn tại!")
else:
    print("Đọc file thành công!")
    print(content)
finally:
    print("Khối finally luôn chạy")
    # file.close()  # Đóng file

# Bắt tất cả exception
try:
    # Code có thể lỗi
    pass
except Exception as e:
    print(f"Lỗi: {e}")
```

## 5. Raise Exception

```python
# Raise exception tự định nghĩa
def chia(a, b):
    if b == 0:
        raise ValueError("Mẫu số không thể là 0")
    return a / b

try:
    result = chia(10, 0)
except ValueError as e:
    print(e)

# Custom exception
class AgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeError("Tuổi không thể âm!")
    if age < 18:
        raise AgeError("Chưa đủ 18 tuổi!")
    return True

try:
    check_age(15)
except AgeError as e:
    print(e)
```

## 6. Working with Paths

```python
import os

# Kiểm tra file/folder tồn tại
if os.path.exists("data.txt"):
    print("File tồn tại")

# Tạo folder
if not os.path.exists("data"):
    os.mkdir("data")

# List files trong folder
files = os.listdir(".")
print(files)

# Join path
path = os.path.join("data", "file.txt")

# Get file info
file_size = os.path.getsize("data.txt")
```

## 📝 Tóm Tắt
- **with open()**: Tự động đóng file
- **"r", "w", "a"**: Read, Write, Append
- **csv**: Xử lý file CSV
- **json**: Xử lý file JSON
- **try-except**: Bắt lỗi
- **raise**: Ném exception
