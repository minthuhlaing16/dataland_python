# Static Property (class variable)


# todo Exercise One


class BankAccount:
    # ? Static Property
    totalaccounts = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.totalaccounts += 1


accObj1 = BankAccount("John Doe", 500)
accObj2 = BankAccount("Min Min", 200)

print("Total bank accounts = ", BankAccount.totalaccounts)


# todo Exercise 2
class Car:
    totalcars = 0  # ? Static property / class property / class variable

    def __init__(self, brand):
        self.brand = brand
        Car.totalcars += 1


carObj1 = Car("Toyota")
carObj2 = Car("Honda")
carObj3 = Car("Suzuki")

print("Total Cars Models: ", Car.totalcars)


# todo Exercise 3


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @staticmethod
    def getcount():
        return Counter.count


counterObj1 = Counter()
counterObj2 = Counter()
counterObj3 = Counter()
counterObj4 = Counter()
counterObj5 = Counter()

print("Total object instance = ", Counter.getcount())


# todo ==> Custom Static Property


class customstcproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls=None):
        return self.func()


class Greet:
    @customstcproperty
    def sayhi():
        return "Hello Mandalay!"


print(Greet.sayhi)


# todo ==> Custom Static Property (with param)


class stcproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls=None):
        return self.func(cls)


class NumCounter:
    idx = 100

    @stcproperty
    def getidx(cls):
        return cls.idx


print(NumCounter.getidx)
