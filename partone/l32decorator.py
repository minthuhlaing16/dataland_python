#
# todo ==> Decorators


def div1(x, y):
    return x / y


print(div1(10, 2))  # ? 5.0
print(div1(2, 10))  # ? 0.2

# ! Number myr tae kaung ko ti pee top nae tat kaung nae sar chin tar


def div2(x, y):
    if y > x:
        return y / x
    else:
        return x / y


print(div2(2, 10))  # ? 5.0
print(div2(10, 2))  # ? 5.0


# todo Decorator


def check(fun):
    def inner(x, y):
        if y > x:
            return y / x
        return fun(x, y)

    return inner


# * Method 1


def div3(x, y):
    return x / y


div4 = check(div3)

print(div4(2, 10))  # ? 5.0
print(div4(10, 2))  # ? 5.0


# * Method 2


@check
def div5(x, y):
    return x / y


print(div5(2, 10))  # ? 5.0
print(div5(10, 2))  # ? 5.0

# todo exercise


def mydecorator(fun):
    def wrapper():
        print("Before the function run!")
        fun()
        print("After the function run!")

    return wrapper


@mydecorator
def sayhi():
    print("hello sir")


sayhi()

# * ==> Decorator with Arguments
# todo ==> using while


def say_name(fun):
    def inner(name):
        print("Before")
        fun(name)
        print("After")

    return inner


@say_name
def greet(name):
    print(f"Hello , {name} How are you?")


greet("John Doe")


# todo ==> Exercise 2


def sayname(count):
    def decorator(func):
        def wrapper(name):
            x = 0  # * init
            while x < count:
                func(name)
                x += 1  # * increment

        return wrapper

    return decorator


@sayname(5)
def greet(name):
    print(f"Hello , {name} How you doing...?")


greet("Yu Yu")


# * for in loop


def talk_my_name(count):
    def decorator(func):
        def wrapper(name):
            for _ in range(count):
                func(name)

        return wrapper

    return decorator


@talk_my_name(3)
def greeting(name):
    print(f"Hi {name}")


greeting("NI NI")


def sumnumbers(count):
    def decorator(func):
        def wrapper(*args):
            for _ in range(count):
                func(args)

        return wrapper

    return decorator


@sumnumbers(3)
def sumresults(numbers):
    total = sum(numbers)
    print(f"Sum result is = {total}")


sumresults(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# * Multiple Decorators


def setuppercase(func):
    def wrapper():
        return func().upper()

    return wrapper


def setexclamation(func):
    def wrapper():
        return func() + " !!!"

    return wrapper


@setuppercase
@setexclamation
def sayhello():
    return "hello"


print(sayhello())  # * HELLO !!!


# todo ==> Multiple Decorators with arguments


def setcounter(count):
    def decorator(func):
        def wrapper(name):
            for _ in range(count):
                func(name)

        return wrapper

    return decorator


def prefix(value):
    def decorator(func):
        def wrapper(name):
            print(value, end=" ")
            return func(name)

        return wrapper

    return decorator


@setcounter(3)
@prefix("Dear:")
def saygreet(name):
    print(f"Hello , {name}")


saygreet("Bo Gyote Aung San")
