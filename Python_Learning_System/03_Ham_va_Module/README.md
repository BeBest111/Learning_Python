# Module 3: Hàm và Module 🔧

## 🎯 Mục Tiêu
- Định nghĩa và sử dụng hàm
- Tham số và giá trị trả về
- Scope của biến
- Import và sử dụng module

## 1. Định Nghĩa Hàm

```python
# Hàm đơn giản
def chao():
    print("Xin chào!")

chao()  # Gọi hàm

# Hàm với tham số
def chao_ten(ten):
    print(f"Xin chào, {ten}!")

chao_ten("An")

# Hàm với giá trị trả về
def cong(a, b):
    return a + b

ket_qua = cong(5, 3)
print(ket_qua)  # 8
```

## 2. Tham Số

```python
# Tham số mặc định
def chao(ten="Bạn"):
    print(f"Xin chào, {ten}!")

chao()        # Xin chào, Bạn!
chao("An")    # Xin chào, An!

# Keyword arguments
def thong_tin(ten, tuoi, thanh_pho):
    print(f"{ten}, {tuoi} tuổi, sống ở {thanh_pho}")

thong_tin(tuoi=25, ten="An", thanh_pho="HN")

# *args - Số lượng tham số không xác định
def tong(*numbers):
    return sum(numbers)

print(tong(1, 2, 3, 4, 5))  # 15

# **kwargs - Từ điển tham số
def thong_tin(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

thong_tin(ten="An", tuoi=25, thanh_pho="HN")
```

## 3. Lambda Function

```python
# Lambda - Hàm ẩn danh
binh_phuong = lambda x: x ** 2
print(binh_phuong(5))  # 25

# Lambda với nhiều tham số
tong = lambda a, b: a + b
print(tong(3, 4))  # 7

# Dùng với map, filter
numbers = [1, 2, 3, 4, 5]
binh_phuong = list(map(lambda x: x ** 2, numbers))
print(binh_phuong)  # [1, 4, 9, 16, 25]
```

## 4. Scope

```python
# Global scope
x = 10

def ham():
    # Local scope
    y = 20
    print(x)  # Truy cập được biến global
    print(y)

ham()
# print(y)  # Lỗi! y không tồn tại ngoài hàm

# global keyword
count = 0

def tang_count():
    global count
    count += 1

tang_count()
print(count)  # 1
```

## 5. Module

```python
# Import toàn bộ module
import math
print(math.sqrt(16))  # 4.0

# Import một phần
from math import pi, sqrt
print(pi)  # 3.14159...
print(sqrt(25))  # 5.0

# Import với alias
import math as m
print(m.pow(2, 3))  # 8.0

# Tạo module riêng (file my_module.py)
# def xin_chao():
#     return "Xin chào!"
# 
# Sau đó import:
# from my_module import xin_chao
```

## 📝 Tóm Tắt
- **def**: Định nghĩa hàm
- **return**: Trả về giá trị
- **lambda**: Hàm ẩn danh
- **import**: Sử dụng module
