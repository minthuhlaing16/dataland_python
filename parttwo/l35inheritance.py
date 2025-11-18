# Parent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand  # ? instance variable

    def power(self):
        return "Petrol"


# * Subclass (inherit from Vehicle)


class EV(Vehicle):
    def power(self):  # ? Overriding parent method
        return "Battery"


carObj = EV("Tesla")
print(carObj.brand)  # ? Tesla
print(carObj.power())  # ? Battery


# ? ==> Using super() . Muu la shi nay tat kaung ko pyan khaw chin tal so super nae khaw tal


# todo exe 1


class Employee:
    def task(self):
        return "Frontend Development"


class Employer(Employee):
    def task(self):
        return super().task() + " and specialized frameworks..."


jobObj = Employer()

print(jobObj.task())

# todo exe 2


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail_info(self):
        return f"Person Name = {self.name}, Age = {self.age}"


class Student(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def detail_info(self):
        original_info = super().detail_info()
        return f"{original_info}, Subject = {self.subject}."


sudentObj = Student("Mya Mya", 23, "Computer Science")

print(sudentObj)
print(sudentObj.detail_info())
