# Module 2: Cấu Trúc Điều Khiển 🔀

## 🎯 Mục Tiêu Học Tập

Sau khi hoàn thành module này, bạn sẽ:
- Hiểu và sử dụng câu lệnh điều kiện if-elif-else
- Làm chủ vòng lặp for và while
- Biết cách sử dụng break, continue, pass
- Áp dụng vòng lặp lồng nhau

---

## 1. Câu Lệnh Điều Kiện

### 1.1. If - Elif - Else

```python
# If đơn giản
tuoi = 18
if tuoi >= 18:
    print("Bạn đã trưởng thành")

# If-else
diem = 7.5
if diem >= 5:
    print("Đạt")
else:
    print("Không đạt")

# If-elif-else
diem = 8.5
if diem >= 9:
    print("Xuất sắc")
elif diem >= 8:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5:
    print("Trung bình")
else:
    print("Yếu")
```

### 1.2. Toán Tử Logic

```python
# AND - Cả hai điều kiện đều đúng
tuoi = 20
co_bang_lai = True

if tuoi >= 18 and co_bang_lai:
    print("Được phép lái xe")

# OR - Ít nhất một điều kiện đúng
la_hoc_sinh = True
la_sinh_vien = False

if la_hoc_sinh or la_sinh_vien:
    print("Được giảm giá vé")

# NOT - Đảo ngược điều kiện
da_dang_ky = False

if not da_dang_ky:
    print("Vui lòng đăng ký")
```

### 1.3. Toán Tử So Sánh Nâng Cao

```python
# So sánh chuỗi
name = "Python"
if name == "Python":
    print("Đúng rồi!")

# In - Kiểm tra phần tử trong chuỗi/list
text = "Hello World"
if "World" in text:
    print("Có chứa World")

# Is - So sánh địa chỉ bộ nhớ
x = None
if x is None:
    print("x là None")

# So sánh chuỗi (chain comparison)
x = 10
if 5 < x < 15:
    print("x nằm trong khoảng 5 đến 15")
```

### 1.4. Conditional Expression (Ternary Operator)

```python
# Cú pháp: value_if_true if condition else value_if_false
tuoi = 20
trang_thai = "Trưởng thành" if tuoi >= 18 else "Vị thành niên"
print(trang_thai)

# Ví dụ khác
a, b = 10, 20
max_value = a if a > b else b
print(f"Số lớn nhất: {max_value}")
```

---

## 2. Vòng Lặp For

### 2.1. For với Range

```python
# In số từ 0 đến 4
for i in range(5):
    print(i)

# In số từ 1 đến 5
for i in range(1, 6):
    print(i)

# In số chẵn từ 0 đến 10
for i in range(0, 11, 2):
    print(i)

# Đếm ngược
for i in range(10, 0, -1):
    print(i)
```

### 2.2. For với Chuỗi và List

```python
# Duyệt chuỗi
name = "Python"
for char in name:
    print(char)

# Duyệt list
fruits = ["Táo", "Cam", "Chuối"]
for fruit in fruits:
    print(fruit)

# Duyệt với index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

### 2.3. For Lồng Nhau

```python
# Bảng cửu chương
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# Vẽ tam giác sao
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

---

## 3. Vòng Lặp While

### 3.1. While Cơ Bản

```python
# Đếm từ 1 đến 5
count = 1
while count <= 5:
    print(count)
    count += 1

# Nhập cho đến khi đúng
password = ""
while password != "123456":
    password = input("Nhập mật khẩu: ")
print("Đúng rồi!")
```

### 3.2. While với Điều Kiện Phức Tạp

```python
# Tìm số chia hết cho 7
num = 1
while num <= 100:
    if num % 7 == 0:
        print(num)
    num += 1

# Vòng lặp vô hạn (cẩn thận!)
# while True:
#     user_input = input("Nhập 'quit' để thoát: ")
#     if user_input == "quit":
#         break
```

---

## 4. Break, Continue, Pass

### 4.1. Break - Thoát Vòng Lặp

```python
# Tìm số đầu tiên chia hết cho 7
for i in range(1, 100):
    if i % 7 == 0:
        print(f"Số đầu tiên: {i}")
        break

# Dừng khi gặp điều kiện
numbers = [1, 2, 3, -1, 5, 6]
for num in numbers:
    if num < 0:
        print("Gặp số âm, dừng!")
        break
    print(num)
```

### 4.2. Continue - Bỏ Qua Lần Lặp

```python
# In số lẻ
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# Bỏ qua giá trị âm
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue
    print(num)
```

### 4.3. Pass - Placeholder

```python
# Placeholder cho code sẽ viết sau
for i in range(5):
    if i == 3:
        pass  # TODO: Xử lý sau
    else:
        print(i)

# Function placeholder
def my_function():
    pass  # Sẽ implement sau
```

---

## 5. Else với Vòng Lặp

```python
# Else với for - chạy khi vòng lặp kết thúc bình thường
for i in range(5):
    print(i)
else:
    print("Vòng lặp hoàn thành!")

# Không chạy else nếu có break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Không in được vì có break")
```

---

## 6. Ví Dụ Tổng Hợp

### 6.1. Kiểm Tra Số Nguyên Tố

```python
num = int(input("Nhập số: "))

if num < 2:
    print(f"{num} không phải số nguyên tố")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} là số nguyên tố")
    else:
        print(f"{num} không phải số nguyên tố")
```

### 6.2. Menu Chương Trình

```python
while True:
    print("\n=== MENU ===")
    print("1. Xem thông tin")
    print("2. Thêm dữ liệu")
    print("3. Thoát")
    
    choice = input("Chọn (1-3): ")
    
    if choice == "1":
        print("Hiển thị thông tin...")
    elif choice == "2":
        print("Thêm dữ liệu...")
    elif choice == "3":
        print("Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ!")
```

### 6.3. Đoán Số

```python
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Tôi đã nghĩ ra một số từ 1-100. Bạn có thể đoán được không?")

while attempts < max_attempts:
    guess = int(input(f"Lần đoán {attempts + 1}/{max_attempts}: "))
    attempts += 1
    
    if guess == secret:
        print(f"Chúc mừng! Bạn đoán đúng sau {attempts} lần!")
        break
    elif guess < secret:
        print("Số của bạn nhỏ hơn!")
    else:
        print("Số của bạn lớn hơn!")
else:
    print(f"Hết lượt! Số đúng là {secret}")
```

---

## 📝 Tóm Tắt

- **if-elif-else**: Điều kiện phân nhánh
- **for**: Lặp với số lần xác định
- **while**: Lặp với điều kiện
- **break**: Thoát vòng lặp
- **continue**: Bỏ qua lần lặp hiện tại
- **pass**: Placeholder không làm gì

---

## 🎯 Tiếp Theo

Hãy vào thư mục `exercises/` để làm bài tập thực hành!
