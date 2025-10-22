# ==> unpacking arguments
def sayhi(name, age):
    print(f"hello friend! My name is {name}. I am {age} years old.")


# ==> Unpacking Positional Arguments
sayhi("aung kyaw", 24)  # hello friend! My name is aung kyaw. I am 24 years old.

args = ("Susan", 55)
sayhi(*args)  # hello friend! My name is Susan. I am 55 years old.


def adding_numbers(a, b, c):
    print(f"Adding Result: {a+b+c}")


adding_numbers(1, 2, 3)  # Adding Result: 6

tuple_numbers = (10, 20, 30)  # Unpack tuple into argument
adding_numbers(*tuple_numbers)  # Adding Result: 60

list_numbers = [100, 200, 300]  # Unpack list into argument
adding_numbers(*list_numbers)  # Adding Result: 600

keyword_arguments = {"name": "hla hla", "age": 33}  # Unpack keyword argument
sayhi(**keyword_arguments)  # hello friend! My name is hla hla. I am 33 years old.
