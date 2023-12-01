#21
'''class Product:
    def __init__(self,price,name):
        self.price=price
        self.name=name
    def apply_discount(self, discount_percent=10):
        discounted_price = self.price - (self.price * discount_percent / 100)
        return discounted_price
product = Product(4500, 'book')
discounted_price = product.apply_discount()
print("new price:", discounted_price)  '''
#22
'''import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

triangle = Triangle(3, 4, 5)
cal_area = triangle.calculate_area()
print(cal_area)'''
#23

'''class Email:
    def __init__(self,subject,sender,recipient):
        self.subject=subject
        self.sender=sender
        self.recipient=recipient
    def send_email(self):
        message = f"emailga jiberiw\njiberiwshi: {self.sender}\nqabil qiliwshi: {self.recipient}\ntema: {self.subject}"
        return(message)
email=Email('wawka','shashka','my code')
send=email.send_email()
print(send)'''
#24
'''class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f"kitap '{book}' kitapxanaga qosiw '{self.name}'")
library = Library("qala kitapxanasi")
library.add_book("Cекретни домишко")'''
#25
'''class Rectangle:
    def __init__(self,length,width) :
        self.length=length
        self.width=width
    def is_square(self):
        s = self.length * self.width
        return(s)
        if self.length==self.width:
          return False
        else:
            return True
rectangle1 = Rectangle(5, 5)  
rectangle2 = Rectangle(4, 6)
print(rectangle1.is_square()) 
print(rectangle2.is_square()) '''
#26
'''class Person:
    def __init__(self,length,name) :
        self.length=length
        self.name=name
    def is_tall(self):
        if self.length >= 180:
            return True
        else:
            return False

person=Person(160,'wawka')
tall=person.is_tall()
print(tall)'''
#27
'''class BankAccount:
    def __init__(self,balance,ower):
        self.balance=balance
        self.ower=ower
    def check_balance(self):
        return self.balance
bank=BankAccount(20000,'men')
balance=bank.check_balance()
print(balance)'''
#28
'''import math
class Circle:
    def __init__(self,radius) :
        self.radius=radius
    def calculate_circumference(self):
       a= 2*math.pi*self.radius
       return(a)
       
circle=Circle(5)
circleference=circle.calculate_circumference()
print(circleference)'''
#29
'''class Car:
    def __init__(self,model,speed):
        self.model=model
        self.speed=speed
    def  accelerate(self,a):
       self.speed +=a
car=Car('BMW X7',250)
print(car.speed)
acc=car.accelerate(5)
print(car.speed)'''
#30
'''class Song:
    def __init__(self,title,artist) :
        self.title=title
        self.artist=artist#mugallim artist degen suwret salatin adam emespa actor degen aktyor bolmayma#
    def play(self):
        return(f'Играет:{self.title} исполнителя:{self.artist}')
song=Song('S-class','stary kids')
play=song.play()
print(play)'''
#31
'''class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_perimeter(self):
        return 2*(self.length+self.width)
rectangle=Rectangle(10,5)
perm=rectangle.calculate_perimeter()
print(perm)'''
#32
'''class Student:
    def __init__(self, name):
        self.name = name
        self.courses = ['Najmatdinova Oralxan']
    def add_course(self, course):
        self.courses.append(course)
student = Student('')
print(student.name) 
student.add_course("py dev")
print(student.courses)  '''
#33
class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.transactions = []

    def generate_statement(self):
        statement = f"Bank Statement for Account Number: {self.account_number}\n"
        statement += "Date\t\tDescription\tAmount\n"
        for transaction in self.transactions:
            date = transaction["date"]
            description = transaction["description"]
            amount = transaction["amount"]
            statement += f"{date}\t{description}\t{amount}\n"
        return statement
    def add_transaction(self, date, description, amount):
        transaction = {"date": date, "description": description, "amount": amount}
        self.transactions.append(transaction)
account = BankAccount("1234567890")

account.add_transaction("2023-11-01", "Refill",  1000)
account.add_transaction("2023-11-05", "Shopping", -500)
account.add_transaction("2023-11-10", "Money transfer", -200)
statement = account.generate_statement()
print(statement)
#34
''''class Book:
    def __init__(self,title,author) :
        self.title=title
        self.author=author
    def is_popular(self,sale=5000):
        if sale>1000:
            return True
        else:
            return False
book=Book('naruto','Masashi Kishimoto')
pop=book.is_popular()
print(pop)'''
#35
'''class Triangle:
    def __init__(self,base,height) :
        self.base=base
        self.height=height
    def calculate_perimeter(self):
        side = ((self.base / 2) ** 2 + self.height ** 2) ** 0.5
        perimeter = 2 * side + self.base
        return perimeter
trianle=Triangle(10,20)
per=trianle.calculate_perimeter()
print(per)'''
#36
'''class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def promote(self, new_position='teacher'):
        self.position = new_position
employee = Employee('Najmatdinov Oralxan','programmist')
print(employee.position)  
employee.promote()
print(employee.position) '''
#37
'''class Dog:
    def __init__(self,name,breed) :
        self.name=name
        self.breed=breed
    def bark(self):
        return 'gave-gave!'
dog=Dog('diamina','Giant Teddy')
bark=dog.bark()
print(bark)'''
#38
'''class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def translate(self, b, a):
        self.x += b
        self.y += a
point = Point(2, 3)
print("Исходные координаты:", point.x, point.y)  
point.translate(5, -2)
print("Новые координаты:", point.x, point.y)  '''
#39
'''class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
bank = Bank("Мой Банк")
account1 = 12345
account2 = 56474
bank.add_account(account1)
bank.add_account(account2)
print(bank.accounts)'''
#40
'''class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
    def add_friend(self, friend):
        self.friends.append(friend)
person = Person('dog')
friend1 = 'cat'
person.add_friend(friend1)

print(person.friends)'''

