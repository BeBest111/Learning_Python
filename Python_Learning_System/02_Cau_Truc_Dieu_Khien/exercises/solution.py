"""GIẢI ĐÁP MODULE 2: CẤU TRÚC ĐIỀU KHIỂN"""

print("=" * 60)
print("BÀI 1: KIỂM TRA SỐ CHẴN LẺ")
print("=" * 60)
so = int(input("Nhập số: "))
if so % 2 == 0:
    print(f"{so} là số chẵn")
else:
    print(f"{so} là số lẻ")

print("\n" + "=" * 60)
print("BÀI 2: XẾP LOẠI HỌC LỰC")
print("=" * 60)
diem = float(input("Nhập điểm (0-10): "))
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

print("\n" + "=" * 60)
print("BÀI 3: TÍNH TỔNG TỪ 1 ĐẾN N")
print("=" * 60)
n = int(input("Nhập n: "))
tong = 0
for i in range(1, n + 1):
    tong += i
print(f"Tổng từ 1 đến {n} = {tong}")
# Hoặc dùng công thức: tong = n * (n + 1) // 2

print("\n" + "=" * 60)
print("BÀI 4: IN BẢNG CỬU CHƯƠNG")
print("=" * 60)
n = int(input("Nhập số: "))
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")

print("\n" + "=" * 60)
print("BÀI 5: KIỂM TRA SỐ NGUYÊN TỐ")
print("=" * 60)
num = int(input("Nhập số: "))
if num < 2:
    print(f"{num} không phải số nguyên tố")
else:
    la_nguyen_to = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to:
        print(f"{num} là số nguyên tố")
    else:
        print(f"{num} không phải số nguyên tố")

print("\n" + "=" * 60)
print("BÀI 6: IN CÁC SỐ CHIA HẾT CHO 3 HOẶC 5")
print("=" * 60)
print("Các số từ 1-100 chia hết cho 3 hoặc 5:")
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=" ")
print()

print("\n" + "=" * 60)
print("BÀI 7: TÍNH GIAI THỪA")
print("=" * 60)
n = int(input("Nhập n: "))
giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i
print(f"{n}! = {giai_thua}")

print("\n" + "=" * 60)
print("BÀI 8: VẼ TAM GIÁC SAO")
print("=" * 60)
n = int(input("Nhập chiều cao: "))
for i in range(1, n + 1):
    print("*" * i)

print("\n" + "=" * 60)
print("BÀI 9: ĐẾM SỐ CHỮ SỐ")
print("=" * 60)
so = abs(int(input("Nhập số: ")))
dem = 0
if so == 0:
    dem = 1
else:
    temp = so
    while temp > 0:
        dem += 1
        temp //= 10
print(f"{so} có {dem} chữ số")
# Hoặc: dem = len(str(so))

print("\n" + "=" * 60)
print("BÀI 10: MENU MÁY TÍNH")
print("=" * 60)
while True:
    print("\n=== MÁY TÍNH ===")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")
    
    chon = input("Chọn (1-5): ")
    
    if chon == "5":
        print("Tạm biệt!")
        break
    elif chon in ["1", "2", "3", "4"]:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        
        if chon == "1":
            print(f"Kết quả: {a + b}")
        elif chon == "2":
            print(f"Kết quả: {a - b}")
        elif chon == "3":
            print(f"Kết quả: {a * b}")
        elif chon == "4":
            if b != 0:
                print(f"Kết quả: {a / b}")
            else:
                print("Không thể chia cho 0!")
    else:
        print("Lựa chọn không hợp lệ!")

print("\n" + "=" * 60)
print("HOÀN THÀNH!")
print("=" * 60)
