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
