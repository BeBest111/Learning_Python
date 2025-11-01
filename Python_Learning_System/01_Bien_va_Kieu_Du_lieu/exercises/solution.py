"""
GIẢI ĐÁP CÁC BÀI TẬP MODULE 1: BIẾN VÀ KIỂU DỮ LIỆU
====================================================
"""

print("=" * 60)
print("BÀI 1: KHAI BÁO VÀ IN BIẾN")
print("=" * 60)

ho_ten = "Nguyen Van A"
tuoi = 25
chieu_cao = 1.75
can_nang = 70

print("=== THÔNG TIN CÁ NHÂN ===")
print(f"Họ tên: {ho_ten}")
print(f"Tuổi: {tuoi} tuổi")
print(f"Chiều cao: {chieu_cao} m")
print(f"Cân nặng: {can_nang} kg")

print("\n" + "=" * 60)
print("BÀI 2: TÍNH TOÁN CƠ BẢN")
print("=" * 60)

so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))

print(f"Tổng: {so_1 + so_2}")
print(f"Hiệu: {so_1 - so_2}")
print(f"Tích: {so_1 * so_2}")
print(f"Thương: {so_1 / so_2:.2f}")
print(f"Chia nguyên: {so_1 // so_2}")
print(f"Phần dư: {so_1 % so_2}")
print(f"Lũy thừa: {so_1 ** so_2}")

print("\n" + "=" * 60)
print("BÀI 3: CHUYỂN ĐỔI KIỂU DỮ LIỆU")
print("=" * 60)

# 1. Chuyển "123" thành số nguyên và cộng thêm 77
chuoi = "123"
ket_qua_1 = int(chuoi) + 77
print(f"1. '123' + 77 = {ket_qua_1}")

# 2. Chuyển 45.67 thành số nguyên
so_thuc = 45.67
ket_qua_2 = int(so_thuc)
print(f"2. int(45.67) = {ket_qua_2}")

# 3. Chuyển 100 thành chuỗi và nối với " điểm"
so = 100
ket_qua_3 = str(so) + " điểm"
print(f"3. 100 + ' điểm' = {ket_qua_3}")

# 4. Chuyển "3.14" thành số thực và nhân với 2
chuoi_so = "3.14"
ket_qua_4 = float(chuoi_so) * 2
print(f"4. '3.14' × 2 = {ket_qua_4}")

# 5. Kiểm tra xem 5 có phải là số nguyên không
kiem_tra = isinstance(5, int)
print(f"5. 5 có phải int? {kiem_tra}")

print("\n" + "=" * 60)
print("BÀI 4: XỬ LÝ CHUỖI")
print("=" * 60)

ho_ten = "Nguyen Van An"

print(f"1. Ký tự đầu: {ho_ten[0]}")
print(f"2. Ký tự cuối: {ho_ten[-1]}")
print(f"3. 3 ký tự đầu: {ho_ten[0:3]}")
print(f"4. Chữ hoa: {ho_ten.upper()}")
print(f"5. Chữ thường: {ho_ten.lower()}")
print(f"6. Số ký tự: {len(ho_ten)}")
print(f"7. Thay đổi: {ho_ten.replace('An', 'Binh')}")

print("\n" + "=" * 60)
print("BÀI 5: TÍNH BMI")
print("=" * 60)

can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

bmi = can_nang / (chieu_cao ** 2)
print(f"BMI của bạn là: {bmi:.2f}")

print("\n" + "=" * 60)
print("BÀI 6: HOÁN ĐỔI GIÁ TRỊ")
print("=" * 60)

a = 10
b = 20
print(f"Trước khi hoán đổi: a = {a}, b = {b}")

# Cách 1: Dùng tuple unpacking (Python style)
a, b = b, a

print(f"Sau khi hoán đổi: a = {a}, b = {b}")

# Cách 2: Dùng phép toán (không khuyến khích)
# a = a + b
# b = a - b
# a = a - b

print("\n" + "=" * 60)
print("BÀI 7: TÍNH DIỆN TÍCH HÌNH TRÒN")
print("=" * 60)

PI = 3.14159
ban_kinh = float(input("Nhập bán kính: "))

dien_tich = PI * (ban_kinh ** 2)
chu_vi = 2 * PI * ban_kinh

print(f"Diện tích: {dien_tich:.2f} cm²")
print(f"Chu vi: {chu_vi:.2f} cm")

print("\n" + "=" * 60)
print("BÀI 8: CHUYỂN ĐỔI NHIỆT ĐỘ")
print("=" * 60)

celsius = float(input("Nhập nhiệt độ (°C): "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit:.2f}°F")

print("\n" + "=" * 60)
print("BÀI 9: TÍNH TIỀN ĐIỆN")
print("=" * 60)

so_kwh = float(input("Nhập số kWh: "))
gia_dien = 2500
vat = 0.10

tien_dien = so_kwh * gia_dien
tien_vat = tien_dien * vat
tong_tien = tien_dien + tien_vat

print(f"Tiền điện (chưa VAT): {tien_dien:,.0f} đồng")
print(f"Thuế VAT (10%): {tien_vat:,.0f} đồng")
print(f"Tổng tiền: {tong_tien:,.0f} đồng")

print("\n" + "=" * 60)
print("BÀI 10: TÍNH THỜI GIAN")
print("=" * 60)

tong_giay = int(input("Nhập số giây: "))

gio = tong_giay // 3600
phut = (tong_giay % 3600) // 60
giay = tong_giay % 60

print(f"{tong_giay} giây = {gio} giờ {phut} phút {giay} giây")
print(f"Định dạng: {gio:02d}:{phut:02d}:{giay:02d}")

print("\n" + "=" * 60)
print("HOÀN THÀNH TẤT CẢ BÀI TẬP!")
print("=" * 60)
