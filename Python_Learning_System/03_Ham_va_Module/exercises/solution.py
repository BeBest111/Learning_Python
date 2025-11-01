"""SOLUTION MODULE 3"""

# Bài 1
def tong(a, b):
    return a + b
print("Bài 1:", tong(5, 3))

# Bài 2
def la_so_chan(n):
    return n % 2 == 0
print("Bài 2:", la_so_chan(4))

# Bài 3
def giai_thua(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Bài 3:", giai_thua(5))

# Bài 4
def tim_max(a, b, c):
    return max(a, b, c)
print("Bài 4:", tim_max(3, 7, 5))

# Bài 5
def dao_chuoi(s):
    return s[::-1]
print("Bài 5:", dao_chuoi("Python"))
