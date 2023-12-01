'''class Person:
    def __init__(self, name):
        self.name = name
    def say_name(self):
        print("my name is _", self.name)
person = Person("wawka")
person.say_name()'''
#2

'''class Person:
    def say_name(self,name):
        self.name=name
        return name

person=Person()
name= person.say_name('wawka')
print(name)'''
#3
'''class Person:
    def __init__(self, name):
        self.name = name
    def say(self):
        print("hello world", self.name)
person = Person('hi')
person.say()'''
#4
'''class Person:
    def __init__(self):
        print("Hello")

    def say(self):
        print("World")
person = Person()
person.say()'''
#5


'''class Person:
    def __init__(self, name,age):
        self.name = name
        self.age=age
    def write_info(self):
        print( self.name,self.age)
person = Person("wawka",'14')
person.write_info()'''
#6
'''class Person:
    def __init__(self, name=0, age=0):
        self.name = name
        self.age = age

    def write_info(self):
        print("name:", self.name)
        print("age:", self.age)
person1 = Person("wawka", 14)
person1.write_info()'''
#7
'''class Person:
    def __init__(self, name=0, age=0):
        self.name = name
        self.age = age

    def write_info(self):
        print("name:", self.name)
        print("age:", self.age)
    def write_info_2(self):
        print("name:", self.name)
        print("age:", self.age)

person1 = Person("wawka", 14)
person2= Person('cat',2)
person1.write_info()
person2.write_info()'''
#8
'''class Rectangle:
    def __init__(self,wigth,hight):
        self.wight=wigth
        self.hight=hight
    def calculate_area(self):
        return self.wight*self.hight
rectangle=Rectangle(5,4)
calculate_area_1=rectangle.calculate_area()
print(calculate_area_1)'''
#9
'''import math

class Circle:
    def __init__(self,r):
        self.r=r
    def calculate_area(self):
        return math.pi*self.r**2
circle=Circle(5)
circle_1=circle.calculate_area()
print(circle_1)'''
#10
'''class Student:
    def __init__(self,oralxan,grade):
        self.name=oralxan
        self.grade=grade
    def is_passing(self):
        if  self.grade>=3:
            return('true')
        else:
            return('false')
        

student = Student("John", 2)
passing_status = student.is_passing()
print(passing_status)'''
#11
'''class Car:
    def __init__(self,fast,name):
        self.fast=fast
        self.name=name
        
    def is_fast(self):
        if self.fast>100:
            return('true')
        else:
            return('false')
car=Car(500,'bmw m5 f90')
fast_1=car.is_fast()
print(fast_1)'''
#12
'''class Person:
    def __init__(self,age,name) :
        self.age=age
        self.name=name
    def birthday(self):
        self.age +=1 
person= Person(14,'wawka')
birth= person.birthday()
print(person.age)'''
#13
'''a=int(input('a='))
class BankAccount:
    def __init__(self,balance,owner):
        self.balance=balance
        self.ower=owner
    def deposit(self):
        self.balance+=a
bank=BankAccount(10,'men')
deposit_1=bank.deposit()
print(bank.balance)'''
#14
'''a=int(input('a='))
class BankAccount:
    def __init__(self,balance,owner):
        self.balance=balance
        self.ower=owner
    def withdraw(self):
        self.balance-=a
bank=BankAccount(10,'men')
deposit_1=bank.withdraw()
print(bank.balance)'''
#15
'''class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def get_info(self):
        print(f"ati: {self.title}, avtor: {self.author}")
book=Book('meaw','cat')
info=book.get_info()'''
#16

'''class Employee:
    def __init__(self,name,salary) :
        self.name=name
        self.salary=salary
    def raise_salary(self):
        self.salary *= 1.1

employee=Employee('dog',50)
employee.raise_salary()
print(f"Новая зарплата: {employee.salary}")'''

#17
'''class Dog:
    def __init__(self,age,name):
        self.name=name
        self.age=age
    def convert_age_to_human_years(self):
        human_age = self.age * 7
        return human_age
dog=Dog(5,'mimika')
human=dog.convert_age_to_human_years()
print(dog.age)
print(dog.name)'''
#18
'''import math
class Point:
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def distance_to_origin(self):
        distance = math.sqrt(self.x ** 2 + self.y ** 2)
        return distance
point = Point(3, 4)
distance = point.distance_to_origin()
print(f"Расстояние от точки до начала координат: {distance}")'''
#20
'''class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def cal_grades(self):
        if len(self.grades) > 0:
            average_grade = sum(self.grades) / len(self.grades)
            return average_grade
        else:
            return 0
student = Student("wawka", [80, 90, 75, 85, 95])
average_grade = student.cal_grades()
print(f"ortasha ball( {student.name}: {average_grade})")'''

#19
'''class BankAccount:
    def __init__(self,balance1,balance2,summ):
        self.balance1=balance1
        self.balance2=balance2
        self.summ=summ
    def transfer(self):
        if self.balance1>=self.summ:
            self.balance1-=self.balance2
            self.balance2+=self.balance1
            return(f'{self.balance1}{self.balance2}')
        else:
            return False
    
app=BankAccount(200,5000,20)
print(app.transfer())'''
    




