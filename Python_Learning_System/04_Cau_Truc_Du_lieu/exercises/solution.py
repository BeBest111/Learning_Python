"""SOLUTION MODULE 4"""

# Bài 1: Tìm số lớn nhất
numbers = [3, 7, 2, 9, 1]
print("Bài 1:", max(numbers))

# Bài 2: Xóa trùng lặp
lst = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(lst))
print("Bài 2:", unique)

# Bài 3: Đảo ngược list
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print("Bài 3:", reversed_list)

# Bài 4: Tạo dictionary
keys = ["name", "age", "city"]
values = ["An", 25, "HN"]
result = dict(zip(keys, values))
print("Bài 4:", result)

# Bài 5: List comprehension
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Bài 5:", evens)

# Bài 6: Giao 2 set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Bài 6:", set1 & set2)

# Bài 7: Đếm tần suất
text = "hello world"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print("Bài 7:", freq)

# Bài 8: Sắp xếp dictionary
scores = {"An": 85, "Binh": 92, "Chi": 78}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print("Bài 8:", sorted_scores)
