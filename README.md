# Python OOP Assignments – Practice Series

This README contains a complete set of Python Object-Oriented Programming (OOP) assignments with examples and usage.

---

## 1. Using `self`

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
```

---

## 2. Using `cls`

```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")
```

---

## 3. Public Variables and Methods

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")
```

---

## 4. Class Variables and Class Methods

```python
class Bank:
    bank_name = "National Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
```

---

## 5. Static Variables and Static Methods

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```

---

## 6. Constructors and Destructors

```python
class Logger:
    def __init__(self):
        print("Logger created.")

    def __del__(self):
        print("Logger destroyed.")
```

---

## 7. Access Modifiers

```python
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
```

---

## 8. The `super()` Function

```python
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
```

---

## 9. Abstract Classes and Methods

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h
```

---

## 10. Instance Methods

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")
```

---

## 11. Class Methods

```python
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
```

---

## 12. Static Methods

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
```

---

## 13. Composition

```python
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()
```

---

## 14. Aggregation

```python
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee
```

---

## 15. MRO and Diamond Inheritance

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass
```

---

## 16. Function Decorators

```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")
```

---

## 17. Class Decorators

```python
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
```

---

## 18. Property Decorators

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price
```

---

## 19. callable() and **call**()

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number
```

---

## 20. Custom Exception

```python
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("Valid age.")
```

---

## 21. Make a Custom Class Iterable

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val
```

---

Happy practicing Python OOP! 🚀
