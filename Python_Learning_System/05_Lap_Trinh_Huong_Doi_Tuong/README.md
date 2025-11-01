# Module 5: Lập Trình Hướng Đối Tượng (OOP) 🎭

## 🎯 Mục Tiêu
- Hiểu Class và Object
- Constructor và Destructor
- Inheritance, Encapsulation, Polymorphism

## 1. Class và Object

```python
# Định nghĩa class
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method
    def gioi_thieu(self):
        print(f"Tôi là {self.name}, {self.age} tuổi")

# Tạo object
person1 = Person("An", 25)
person1.gioi_thieu()  # Tôi là An, 25 tuổi

# Truy cập thuộc tính
print(person1.name)   # An
person1.age = 26      # Sửa thuộc tính
```

## 2. Thuộc Tính và Phương Thức

```python
class BankAccount:
    # Class variable (thuộc tính lớp)
    bank_name = "ABC Bank"
    
    def __init__(self, owner, balance=0):
        # Instance variable (thuộc tính đối tượng)
        self.owner = owner
        self.balance = balance
    
    # Instance method
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    # Class method
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    
    # Static method
    @staticmethod
    def validate_amount(amount):
        return amount > 0

# Sử dụng
account = BankAccount("An", 1000)
account.deposit(500)
print(account.balance)  # 1500
```

## 3. Encapsulation (Đóng Gói)

```python
class Student:
    def __init__(self, name, age):
        self.name = name        # Public
        self._grade = None      # Protected (quy ước)
        self.__password = "123" # Private
    
    # Getter
    def get_password(self):
        return self.__password
    
    # Setter
    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            return True
        return False

student = Student("An", 20)
print(student.name)              # OK
# print(student.__password)      # Lỗi!
print(student.get_password())    # OK - dùng getter
```

## 4. Inheritance (Kế Thừa)

```python
# Lớp cha (base class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

# Lớp con (derived class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} nói: Gâu gâu!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} nói: Meo meo!"

# Sử dụng
dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.speak())  # Buddy nói: Gâu gâu!
print(cat.speak())  # Kitty nói: Meo meo!

# Super() - gọi method của lớp cha
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
```

## 5. Polymorphism (Đa Hình)

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Polymorphism in action
shapes = [Rectangle(5, 4), Circle(3)]
for shape in shapes:
    print(shape.area())
```

## 6. Magic Methods

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    # Đại diện chuỗi
    def __str__(self):
        return f"{self.title} ({self.pages} trang)"
    
    # So sánh
    def __eq__(self, other):
        return self.pages == other.pages
    
    # Cộng
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book("Python", 300)
book2 = Book("Java", 400)
print(book1)           # Python (300 trang)
print(book1 == book2)  # False
print(book1 + book2)   # 700
```

## 📝 Tóm Tắt
- **Class**: Khuôn mẫu, Object: Thực thể
- **__init__**: Constructor
- **self**: Tham chiếu đến object
- **Encapsulation**: Ẩn dữ liệu
- **Inheritance**: Kế thừa
- **Polymorphism**: Đa hình
