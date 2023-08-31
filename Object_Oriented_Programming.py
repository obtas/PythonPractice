"""Exercise One:
Create a class called Person with a constructor that takes in the person's name, age and occupation.
The class should have methods get_name(), get_age() and get_occupation() that return the respective
values. Create an instance of the class and call the methods to display the values."""

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_occupation(self):
        return self.occupation
    
person_1 = Person('Karina', 23, 'Singer')

print("Name: ", person_1.get_name())
print("Age: ", person_1.get_age())
print("Occupation: ", person_1.get_occupation())

"""Exercise Two:
Create a class called Student that inherits from Person. The class must have a constructor that takes in
the name, age, occupation, and a list of subjects. The class should have a method get_subjects() that
returns the list of subjects. Create an instance of the class and call the methods to display the values."""

class Student(Person):
    def __init__(self, name, age, occupation, subject_1, subject_2, subject_3):
        Person.__init__(self, name, age, occupation)
        self.subject_1 = subject_1
        self.subject_2 = subject_2
        self.subject_3 = subject_3

    def get_subjects(self):
        return self.subject_1, self.subject_2, self.subject_3
    
person_2 = Student('Winter', 26, 'Student', 'Science', 'English', 'Music')

print("Name: ", person_2.get_name())
print("Age: ", person_2.get_age())
print("Occupation: ", person_2.get_occupation())
print("Subjects: ", person_2.get_subjects())

"""Exercise Three:
Create a class called Rectangle with a constructor that takes in the width and height. The class should
have methods get_area() and get_perimeter() that return the area and perimeter of the rectangle
respectively. Create an instance of the class and call the methods to display the values."""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (self.height * 2) + (self.width * 2)
        return perimeter
    
rect = Rectangle(40, 200)

print("The area is: ", rect.get_area())
print("The perimeter is: ", rect.get_perimeter())

"""Exercise Four:
Create a class called BankAccount with a constructor that takes in the owner's name, balance and type
of account. The class should have methods get_balance(), deposit(amount) and withdraw(amount) that
return the balance, deposit an amount, and withdraw an amount respectively. Create an instance of
the class and call the methods to display the values."""

class BankAccount:
    def __init__(self, name, balance, type_of_account):
        self.name = name
        self.balance = balance
        self.type_of_account = type_of_account

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
bank_account_1 = BankAccount('Jane', 100, 'SAVINGS')
print("Balance: ", bank_account_1.get_balance())
print("Final Balance: ", bank_account_1.deposit(750))
print("Final Balance:", bank_account_1.withdraw(50))


"""Exercise Five:
Create a class called Vehicle with a constructor that takes in the make, model and year. The class
should have methods get_make(), get_model() and get_year() that return the respective values. Create
two classes, Car and Truck, that inherit from Vehicle. The Car class should have an additional method
get_type() that returns "Car" and the Truck class should have an additional method get_type() that
returns "Truck". Create instances of both classes and call the methods to display the values."""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
class Car(Vehicle):
    def __init__(self, make, model, year):
        Vehicle.__init__(self, make, model, year)

    def get_type(self):
        return "Car"
    
class Truck(Vehicle):
    def __init__(self, make, model, year):
        Vehicle.__init__(self, make, model, year)

    def get_type(self):
        return "Truck"
    
car_1 = Car("Vauxhall", "Corsa", 2005)
truck_1 = Truck("Ford", "Truck", 2006)

print("Make: ", car_1.get_make())
print("Model: ", car_1.get_model())
print("Year: ", car_1.get_year())
print("Type: ", car_1.get_type())
print("*" * 100)
print("Make: ", truck_1.get_make())
print("Model: ", truck_1.get_model())
print("Year: ", truck_1.get_year())
print("Type: ", truck_1.get_type())
