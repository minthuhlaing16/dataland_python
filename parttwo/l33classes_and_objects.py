# defining the class


# constructor
class Car:
    def __init__(self, brand: str, wheels: int) -> None:
        self.brand = brand
        self.wheels = wheels

    def engineon(self) -> None:
        print(f"Engine on: {self.brand}")

    def engineoff(self) -> None:
        print(f"Engine off: {self.brand}")

    def drive(self, km: float) -> None:
        print(f"Driving: {self.brand} for {km}km/hr")

    def describe(self) -> None:
        print(f"{self.brand} is a car with {self.wheels} wheels")


def main() -> None:
    toyota: Car = Car("Toyota", 4)
    toyota.engineon()
    toyota.drive(50)
    toyota.engineoff()
    toyota.describe()

    honda: Car = Car("Honda", 8)
    honda.engineon()
    honda.drive(50)
    honda.engineoff()
    honda.describe()


# main()

# ? a paw ka def bay ka main mar s par twr yin error tat p
if __name__ == "__main__":
    main()


class Staff:
    def __init__(self, name: str, age: int, hascar: bool) -> None:
        # ? bind ma lote khin mar lae htoke loa ya tal
        print(f"My name is {name}, I am {age} years old.")
        self.name = name
        self.age = age
        self.hascar = hascar

    def getinfo(self) -> None:
        print(f"Name is {self.name}, Age is {self.age}, car status {self.hascar}")


def main() -> None:
    staffObj1: Staff = Staff("Nu NU", 27, True)
    staffObj2: Staff = Staff("Aung Kyaw", 30, False)

    staffObj1.getinfo()
    staffObj2.getinfo()

    print(staffObj1.name)
    print(staffObj1.age)
    print(staffObj1.hascar)

    print(staffObj2.name)
    print(staffObj2.age)
    print(staffObj2.hascar)


# main()

if __name__ == "__main__":
    main()
