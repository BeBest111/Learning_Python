"""SOLUTION MODULE 6"""

import json
import csv

# Bài 1: Ghi và đọc file
names = ["An", "Bình", "Chi"]
with open("names.txt", "w", encoding="utf-8") as f:
    for name in names:
        f.write(name + "\n")

with open("names.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Bài 1:\n", content)

# Bài 2: Đếm số dòng
with open("names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"Bài 2: Số dòng: {len(lines)}")

# Bài 3: Tìm từ trong file
def count_word(filename, word):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().lower()
        return content.count(word.lower())

print(f"Bài 3: Số lần xuất hiện: {count_word('names.txt', 'An')}")

# Bài 4: Ghi JSON
person = {
    "name": "Nguyen Van An",
    "age": 25,
    "city": "Ha Noi",
    "skills": ["Python", "Java"]
}

with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=2)
print("Bài 4: Đã ghi JSON")

# Bài 5: CSV và tính tổng
scores = [
    ["Name", "Score"],
    ["An", 8.5],
    ["Binh", 9.0],
    ["Chi", 7.5]
]

with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(scores)

with open("scores.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    total = 0
    count = 0
    for row in reader:
        total += float(row["Score"])
        count += 1
    print(f"Bài 5: Điểm TB: {total/count:.2f}")

# Bài 6: Nhập số an toàn
def nhap_so(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Vui lòng nhập số!")

# Bài 7: Copy file
def copy_file(source, dest):
    try:
        with open(source, "r", encoding="utf-8") as f1:
            content = f1.read()
        with open(dest, "w", encoding="utf-8") as f2:
            f2.write(content)
        return True
    except FileNotFoundError:
        print("File không tồn tại!")
        return False
    except Exception as e:
        print(f"Lỗi: {e}")
        return False

copy_file("names.txt", "names_copy.txt")
print("Bài 7: Đã copy file")

# Bài 8: Custom exception
class ScoreError(Exception):
    pass

def validate_score(score):
    if not (0 <= score <= 10):
        raise ScoreError("Điểm phải từ 0-10!")
    return True

try:
    validate_score(15)
except ScoreError as e:
    print(f"Bài 8: {e}")

print("\nHOÀN THÀNH TẤT CẢ BÀI TẬP!")
