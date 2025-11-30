#
# ? Note : Declared using the @classmethod decorator
# ? Take cls as first argument.
# ? use for Alternative Constructors: create different ways to instantiate objects


# class Greeting:
#     @classmethod
#     def sayhello(cls):
#         print(f"Hello Myanmar")


# Greeting.sayhello()  # ? Hello Myanmar


class Greeting:
    @classmethod
    def sayhello(cls):
        print(f"Hello from {cls.__name__}")


Greeting.sayhello()  # ? Hello from Greeting


class Mobile:
    network = "5G"

    @classmethod
    def getconnection(cls):
        return cls.network


print(Mobile.getconnection())  # * 5G

mobileObj: Mobile = Mobile()
print(mobileObj.getconnection())  # * 5G


# todo static property + classmethod
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def getcount(cls):  # ? cls refers to the class itself
        return cls.count


print(Counter.getcount())  # ? before instantiation

counterObj1 = Counter()
counterObj2 = Counter()
counterObj3 = Counter()

print(
    Counter.getcount()
)  # ? after instantiation, also valid but less common (for static methods, class methods you don't need to create an object.)


class Book:
    BOOKTYPES = ("HardCover", "PaperBack", "Ebook")

    @classmethod
    def getbooktype(cls):
        return cls.BOOKTYPES

    @classmethod
    def booktypevalid(cls, formatname):
        return formatname in cls.BOOKTYPES


print(Book.getbooktype())
print(Book.booktypevalid("PDF"))
print(Book.booktypevalid("Paperback"))
print(Book.booktypevalid("Ebook"))

# todo ==> Alternative constructor


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculateage(cls, name, birthyear):
        currentyear = 2025
        age = currentyear - birthyear
        return cls(name, age)

    @classmethod
    def currentage(cls, name, birthyear):
        from datetime import date

        currentyear = date.today().year
        age = currentyear - birthyear
        return cls(name, age)


# ? Normal instant
personObj1 = Person("John Doe", 25)
print(personObj1.name, personObj1.age)  # * John Doe 25

# ? Using class method as alternative constructor
personObj2 = Person.calculateage("Hla Hla", 1997)
print(personObj2.name, personObj2.age)

personObj3 = Person.currentage("Alice", 1996)
print(personObj3.name, personObj3.age)


# todo ==> Class Method with Inheritance


class Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def describe(cls, level):
        return f"A {cls.__name__} studies at {level}."


class GraduateStudent(Student):
    pass


print(Student.describe("undergraduate"))
print(GraduateStudent.describe("graduate"))


# todo ==> Define Read-Only Property (@property)


class Employee:
    def __init__(self, name, monthlysalary):
        self.name = name
        self._monthlysalary = monthlysalary

    @property
    def annualsalary(self):
        return self._monthlysalary * 12


employeeObj = Employee("Zaw Zaw", 500)
print(employeeObj.annualsalary)
