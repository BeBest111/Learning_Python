# Module 4: Cấu Trúc Dữ Liệu 📊

## 🎯 Mục Tiêu
- List, Tuple, Dictionary, Set
- Các phương thức xử lý
- List comprehension

## 1. List (Danh Sách)

```python
# Tạo list
fruits = ["táo", "cam", "chuối"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hai", 3.0, True]

# Truy cập phần tử
print(fruits[0])      # táo
print(fruits[-1])     # chuối
print(fruits[0:2])    # ['táo', 'cam']

# Thêm phần tử
fruits.append("dâu")          # Thêm cuối
fruits.insert(1, "xoài")      # Thêm vị trí
fruits.extend(["nho", "dưa"]) # Thêm nhiều

# Xóa phần tử
fruits.remove("cam")  # Xóa theo giá trị
del fruits[0]         # Xóa theo index
last = fruits.pop()   # Xóa và trả về phần tử cuối

# Các phương thức khác
print(len(fruits))           # Độ dài
print(fruits.count("táo"))   # Đếm số lần xuất hiện
fruits.sort()                # Sắp xếp
fruits.reverse()             # Đảo ngược
```

## 2. Tuple (Bộ - Không Thay Đổi)

```python
# Tạo tuple
coordinates = (10, 20)
person = ("An", 25, "Hà Nội")

# Truy cập
print(coordinates[0])  # 10

# Unpack
x, y = coordinates
name, age, city = person

# Tuple 1 phần tử
single = (5,)  # Cần dấu phẩy
```

## 3. Dictionary (Từ Điển)

```python
# Tạo dictionary
person = {
    "name": "An",
    "age": 25,
    "city": "Hà Nội"
}

# Truy cập
print(person["name"])        # An
print(person.get("age"))     # 25
print(person.get("job", "Không có"))  # Giá trị mặc định

# Thêm/sửa
person["job"] = "Developer"
person["age"] = 26

# Xóa
del person["city"]
job = person.pop("job")

# Các phương thức
print(person.keys())    # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['An', 26])
print(person.items())   # dict_items([('name', 'An'), ('age', 26)])

# Duyệt dictionary
for key, value in person.items():
    print(f"{key}: {value}")
```

## 4. Set (Tập Hợp)

```python
# Tạo set
numbers = {1, 2, 3, 4, 5}
fruits = set(["táo", "cam", "táo"])  # Tự động xóa trùng

# Thêm/xóa
numbers.add(6)
numbers.remove(1)
numbers.discard(10)  # Không lỗi nếu không tồn tại

# Các phép toán tập hợp
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # Hợp: {1, 2, 3, 4, 5}
print(set1 & set2)  # Giao: {3}
print(set1 - set2)  # Hiệu: {1, 2}
print(set1 ^ set2)  # Đối xứng: {1, 2, 4, 5}
```

## 5. List Comprehension

```python
# Tạo list từ vòng lặp
squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# Với điều kiện
evens = [x for x in range(1, 11) if x % 2 == 0]
# [2, 4, 6, 8, 10]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set comprehension
unique_lengths = {len(word) for word in ["a", "ab", "abc", "ab"]}
# {1, 2, 3}
```

## 📝 Tóm Tắt
- **List**: Có thứ tự, thay đổi được, cho phép trùng lặp
- **Tuple**: Có thứ tự, KHÔNG thay đổi, cho phép trùng lặp
- **Dictionary**: Cặp key-value, không có thứ tự (Python 3.7+ có)
- **Set**: Không thứ tự, không trùng lặp
