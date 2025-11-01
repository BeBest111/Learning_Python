"""SOLUTION MODULE 5: OOP"""

# Bài 1: Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 4)
print(f"Diện tích: {rect.area()}")
print(f"Chu vi: {rect.perimeter()}")

# Bài 2: Student
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)
    
    def average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0
    
    def grade(self):
        avg = self.average()
        if avg >= 9: return "A"
        elif avg >= 8: return "B"
        elif avg >= 6.5: return "C"
        elif avg >= 5: return "D"
        else: return "F"

student = Student("An")
student.add_score(8.5)
student.add_score(9.0)
print(f"TB: {student.average()}, Xếp loại: {student.grade()}")

# Bài 3: BankAccount
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

account = BankAccount("An", 1000)
account.deposit(500)
print(f"Số dư: {account.get_balance()}")

# Bài 4: Inheritance
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        return f"{self.brand} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    
    def info(self):
        return f"{super().info()}, {self.doors} cửa"

car = Car("Toyota", 2023, 4)
print(car.info())

# Bài 5: Calculator
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        return a / b if b != 0 else None

print(f"5 + 3 = {Calculator.add(5, 3)}")
print(f"5 * 3 = {Calculator.multiply(5, 3)}")
