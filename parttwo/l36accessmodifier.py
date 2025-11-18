#
# todo==> Modifier    Syntax      Access Inside Class     Access Inside Subclass    Access Outside Class
# todo==> Public      this.name   Yes                     Yes                       Yes
# todo==> Private     #name       Yes                     No                        No
# todo==> Protected   _name       Yes                     Yes                       Possible(Should not be use)


# ! Python mar pay tat nii ka
# todo==> Modifier    Syntax            Access Inside Class     Access Inside Subclass    Access Outside Class
# todo==> Public      self.name         Yes                     Yes                       Yes
# todo==> Private     self.__name       Yes                     No                        No
# todo==> Protected   self._name        Yes                     Yes                       Possible(Should not be use)


class Car:  # ? Defining the class
    def __init__(
        self, brand: str, wheels: int
    ) -> None:  # ? constructor method init ,type hint
        self.brand = brand  # ? public attribute
        self._wheels = wheels  # ? protected attribute
        self.__engine_status = False  # ? private attribute

    def engineon(self) -> None:
        self.__engine_status = True
        print(f"Engine on: {self.brand}")  # ? Instance Public Methods

    def engineoff(self) -> None:
        self.__engine_status = False
        print(f"Engine off: {self.brand}")

    def drive(self, km: float) -> None:
        if self.__engine_status:
            print(f"Driving: {self.brand} for {km}km/hr")
        else:
            print(f"Cannot Drive: {self.brand} engine is off !!!")

    def describe(self) -> None:
        print(f"{self.brand} is a car with {self._wheels} wheels")

    def __checkcomputerbox(self) -> None:  # ? Instance Private Methods
        print(f"Checking Computer Box of {self.brand}!")

    def _serviceengine(self) -> None:  # ? Instance Protected Methods
        print(f"Servicing the engine of {self.brand}!")

    def maintenance(self) -> None:  # ? Instance Public Method(as getter)
        print(f"Maintenance on {self.brand}!")
        self.__checkcomputerbox()
        self._serviceengine()


def main() -> None:
    toyota: Car = Car("Toyota", 4)
    toyota.engineon()
    toyota.drive(50)
    toyota.engineoff()
    toyota.describe()

    # print(f"This is protected attribute = {toyota._wheels}") # ! di lol ma tone tint buu

    # print(f"This is private attribute = {toyota.__engine_status}") # ! error

    # print(
    #     f"This is private attribute = {toyota._Car__engine_status}"
    # )  # ! khaw loa ya tal but ma tone tint buu

    # toyota._serviceengine() # ! not recommended

    # toyota.__checkcomputerbox()  # ! error

    # toyota._Car__checkcomputerbox() # ! khaw loa ya tal but not recommended

    toyota.maintenance()


# main()

# ? a paw ka def bay ka main mar s par twr yin error tat p
if __name__ == "__main__":
    main()
