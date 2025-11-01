# 📝 QUIZ MODULE 2: CẤU TRÚC ĐIỀU KHIỂN

## CÂU HỎI

### Câu 1: Kết quả của code sau là gì?
```python
x = 10
if x > 5:
    print("A")
elif x > 8:
    print("B")
else:
    print("C")
```
A. A  
B. B  
C. C  
D. A và B

---

### Câu 2: Range(1, 10, 2) tạo ra dãy số nào?
A. 1, 2, 3, 4, 5, 6, 7, 8, 9  
B. 1, 3, 5, 7, 9  
C. 2, 4, 6, 8, 10  
D. 1, 3, 5, 7, 9, 11

---

### Câu 3: Break dùng để làm gì?
A. Bỏ qua lần lặp hiện tại  
B. Thoát khỏi vòng lặp  
C. Tạm dừng chương trình  
D. Không làm gì

---

### Câu 4: Continue dùng để làm gì?
A. Tiếp tục chương trình  
B. Thoát vòng lặp  
C. Bỏ qua phần còn lại của lần lặp và tiếp tục lần lặp tiếp theo  
D. Dừng chương trình

---

### Câu 5: Đoạn code nào in số từ 5 đến 1?
A. `for i in range(5, 0, -1)`  
B. `for i in range(1, 5)`  
C. `for i in range(5, 1)`  
D. `for i in range(1, 6, -1)`

---

### Câu 6: Kết quả của 5 == 5.0 là gì?
A. True  
B. False  
C. Error  
D. None

---

### Câu 7: Toán tử nào kiểm tra một giá trị có trong list không?
A. is  
B. in  
C. has  
D. contains

---

### Câu 8: Pass dùng để làm gì?
A. Bỏ qua lỗi  
B. Placeholder không làm gì  
C. Thoát vòng lặp  
D. Tiếp tục vòng lặp

---

### Câu 9: Đoạn code nào ĐÚNG để kiểm tra x nằm trong khoảng 10-20?
A. `if 10 < x < 20:`  
B. `if x > 10 and x < 20:`  
C. `if x in range(10, 20):`  
D. Cả A và B

---

### Câu 10: Kết quả của code sau?
```python
for i in range(3):
    if i == 1:
        continue
    print(i)
```
A. 0 1 2  
B. 0 2  
C. 1 2  
D. 0 1

---

### Câu 11: While True: tạo ra điều gì?
A. Lỗi cú pháp  
B. Vòng lặp vô hạn  
C. Chạy 1 lần  
D. Không chạy

---

### Câu 12: Ternary operator trong Python có cú pháp nào?
A. `condition ? true : false`  
B. `true if condition else false`  
C. `if condition then true else false`  
D. `condition && true || false`

---

### Câu 13: Else có thể dùng với vòng lặp không?
A. Không  
B. Có, chạy khi vòng lặp kết thúc bình thường  
C. Có, chạy khi có break  
D. Chỉ với for, không với while

---

### Câu 14: Kết quả của not (True and False)?
A. True  
B. False  
C. Error  
D. None

---

### Câu 15: Enumerate() dùng để làm gì?
A. Đếm số phần tử  
B. Tạo ra index và giá trị khi duyệt  
C. Sắp xếp list  
D. Xóa phần tử

---

## ✅ ĐÁP ÁN

**Câu 1: A** - if đầu tiên đúng thì không kiểm tra elif

**Câu 2: B** - range(1, 10, 2): bắt đầu 1, kết thúc trước 10, bước 2

**Câu 3: B** - break thoát khỏi vòng lặp

**Câu 4: C** - continue bỏ qua phần còn lại và lặp tiếp

**Câu 5: A** - range(5, 0, -1) đếm ngược từ 5 đến 1

**Câu 6: A** - Python so sánh giá trị, không phân biệt int/float

**Câu 7: B** - toán tử in kiểm tra phần tử có trong container

**Câu 8: B** - pass là placeholder, không làm gì

**Câu 9: D** - Cả hai cách đều đúng

**Câu 10: B** - continue bỏ qua i=1

**Câu 11: B** - Tạo vòng lặp vô hạn (cần break để thoát)

**Câu 12: B** - `value_if_true if condition else value_if_false`

**Câu 13: B** - else chạy khi vòng lặp kết thúc không có break

**Câu 14: A** - not False = True

**Câu 15: B** - enumerate() trả về (index, value)

---

## 📊 ĐÁNH GIÁ

- **13-15**: Xuất sắc! 🌟
- **10-12**: Tốt! 👍
- **7-9**: Khá 📚
- **<7**: Ôn lại 💪
