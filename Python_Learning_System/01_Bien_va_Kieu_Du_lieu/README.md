# Module 1: Biến và Kiểu Dữ Liệu 📊

## 🎯 Mục Tiêu Học Tập

Sau khi hoàn thành module này, bạn sẽ:
- Hiểu khái niệm biến và cách sử dụng trong Python
- Nắm vững các kiểu dữ liệu cơ bản
- Biết cách chuyển đổi giữa các kiểu dữ liệu
- Sử dụng các toán tử cơ bản

---

## 1. Biến (Variables)

### 1.1. Biến là gì?

Biến là một "hộp" để lưu trữ dữ liệu. Trong Python, bạn không cần khai báo kiểu dữ liệu.

```python
# Khai báo biến
ten = "Nguyen Van A"
tuoi = 25
diem = 9.5

print(ten)   # Nguyen Van A
print(tuoi)  # 25
print(diem)  # 9.5
```

### 1.2. Quy Tắc Đặt Tên Biến

✅ **Đúng:**
```python
ten_sinh_vien = "An"
tuoi1 = 20
_private_var = 100
HANG_SO = 3.14
```

❌ **Sai:**
```python
# 1ten = "An"        # Không bắt đầu bằng số
# ten-sinh-vien = "" # Không dùng dấu gạch ngang
# class = "A1"       # Không dùng từ khóa
```

### 1.3. Gán Nhiều Giá Trị

```python
# Gán cùng lúc
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# Gán cùng giá trị
a = b = c = 0
print(a, b, c)  # 0 0 0
```

---

## 2. Kiểu Dữ Liệu Cơ Bản

### 2.1. Số Nguyên (Integer)

```python
so_nguyen = 100
so_am = -50
so_lon = 1_000_000  # Dùng _ để dễ đọc

print(type(so_nguyen))  # <class 'int'>
```

### 2.2. Số Thực (Float)

```python
so_thuc = 3.14
so_khoa_hoc = 2.5e3  # 2.5 * 10^3 = 2500.0

print(type(so_thuc))  # <class 'float'>
```

### 2.3. Chuỗi (String)

```python
# Tạo chuỗi
chuoi1 = 'Hello'
chuoi2 = "World"
chuoi3 = '''Chuỗi
nhiều dòng'''

# Nối chuỗi
hoan_chinh = chuoi1 + " " + chuoi2
print(hoan_chinh)  # Hello World

# Lặp chuỗi
print("Ha" * 3)  # HaHaHa

# Truy cập ký tự
ten = "Python"
print(ten[0])     # P
print(ten[-1])    # n
print(ten[0:3])   # Pyt
```

### 2.4. Boolean

```python
dung = True
sai = False

# Kết quả so sánh
ket_qua = 5 > 3
print(ket_qua)  # True
print(type(ket_qua))  # <class 'bool'>
```

---

## 3. Chuyển Đổi Kiểu Dữ Liệu

### 3.1. Ép Kiểu (Type Casting)

```python
# String -> Integer
chuoi = "100"
so = int(chuoi)
print(so + 50)  # 150

# Integer -> String
tuoi = 25
text = "Tôi " + str(tuoi) + " tuổi"
print(text)  # Tôi 25 tuổi

# String -> Float
gia = "19.99"
gia_float = float(gia)
print(gia_float * 2)  # 39.98

# Float -> Integer (làm tròn xuống)
pi = 3.14
so_nguyen = int(pi)
print(so_nguyen)  # 3
```

### 3.2. Kiểm Tra Kiểu Dữ Liệu

```python
x = 100
print(type(x))           # <class 'int'>
print(isinstance(x, int))  # True
```

---

## 4. Toán Tử Cơ Bản

### 4.1. Toán Tử Số Học

```python
a = 10
b = 3

print(a + b)   # 13  - Cộng
print(a - b)   # 7   - Trừ
print(a * b)   # 30  - Nhân
print(a / b)   # 3.333... - Chia
print(a // b)  # 3   - Chia lấy phần nguyên
print(a % b)   # 1   - Chia lấy phần dư
print(a ** b)  # 1000 - Lũy thừa
```

### 4.2. Toán Tử So Sánh

```python
x = 5
y = 10

print(x == y)  # False - Bằng
print(x != y)  # True  - Khác
print(x > y)   # False - Lớn hơn
print(x < y)   # True  - Nhỏ hơn
print(x >= y)  # False - Lớn hơn hoặc bằng
print(x <= y)  # True  - Nhỏ hơn hoặc bằng
```

### 4.3. Toán Tử Logic

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

---

## 5. Input/Output

### 5.1. In Ra Màn Hình

```python
print("Hello, World!")
print("Python", "is", "awesome", sep=" - ")  # Python - is - awesome
print("Dòng 1", end=" ")
print("Dòng 2")  # Dòng 1 Dòng 2
```

### 5.2. Nhập Từ Bàn Phím

```python
ten = input("Nhập tên của bạn: ")
print("Xin chào,", ten)

# Nhập số (phải ép kiểu)
tuoi_str = input("Nhập tuổi: ")
tuoi = int(tuoi_str)
print("Năm sau bạn", tuoi + 1, "tuổi")
```

---

## 6. Ví Dụ Tổng Hợp

```python
# Chương trình tính diện tích hình chữ nhật
print("=== TÍNH DIỆN TÍCH HÌNH CHỮ NHẬT ===")

# Nhập dữ liệu
chieu_dai = float(input("Nhập chiều dài: "))
chieu_rong = float(input("Nhập chiều rộng: "))

# Tính toán
dien_tich = chieu_dai * chieu_rong
chu_vi = (chieu_dai + chieu_rong) * 2

# In kết quả
print(f"Diện tích: {dien_tich} m²")
print(f"Chu vi: {chu_vi} m")
```

---

## 📝 Tóm Tắt

- **Biến** lưu trữ dữ liệu, không cần khai báo kiểu
- **Kiểu dữ liệu cơ bản**: int, float, string, boolean
- **Ép kiểu** để chuyển đổi giữa các kiểu dữ liệu
- **Toán tử** để thực hiện các phép tính và so sánh
- **input()** để nhập, **print()** để xuất

---

## 🎯 Tiếp Theo

Hãy vào thư mục `exercises/` để làm bài tập thực hành!
