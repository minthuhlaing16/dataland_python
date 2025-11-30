#
# ? Must be implemented by concrete subclasses
# ? Cannot be instantiated directly

# todo => Create an Abstract Base Class (ABC)

from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @abstractmethod  # ? Decorator
    def showinfo(self) -> None:
        # pass #? no implementation here
        ...  # ? ellipsis --> more to come or use in special case

    @abstractmethod
    def getrole(self) -> None:
        # pass
        ...


class Student(Person):
    def __init__(self, name, age, studentid, major) -> None:
        super().__init__(name, age)
        self.studentid = studentid
        self.major = major

    # ? implement the abstract methods
    def showinfo(self):
        return f"Student: {self.name}, Age: {self.age} , ID: {self.studentid}, Major: {self.major}."

    def getrole(self):
        return "Student"


class Employee(Person):
    def __init__(self, name, age, employeeid, department):
        super().__init__(name, age)
        self.employeeid = employeeid
        self.department = department

    def showinfo(self):
        return f"Employee: {self.name} , Age: {self.age} , EmployeeID: {self.employeeid} , Department: {self.department}."

    def getrole(self):
        return "Employee"


class Teacher(Person):
    def __init__(self, name, age, teacherid, department, subject):
        super().__init__(name, age)
        self.teacherid = teacherid
        self.department = department
        self.subject = subject

    def showinfo(self):
        return f"I am teacher {self.name}. I am {self.age} years old.My teacher id is {self.teacherid}.I work in {self.department} Department. I teach {self.subject} subject.."

    def getrole(self):
        return "Teacher"


class Developer(Employee):
    def __init__(self, name, age, employeeid, department, role):
        super().__init__(name, age, employeeid, department)
        self.role = role

    def showinfo(self):
        return f"My name is {self.name}. I am {self.age} years old. I am a {self.role}. My id is {self.employeeid}. I work in {self.department} department.."

    # def getrole(self):
    #     return "Web Developer"


def main() -> None:
    student: Student = Student("Aung Aung", 23, "Std1001", "Computer Science")
    employee: Employee = Employee("John Doe", 23, "EMP1001", "Hr Department")
    teacher: Teacher = Teacher("Alice", 50, "TR1001", "Mathematic", "Math")
    developer: Developer = Developer("Bob", 33, "DEV1001", "MGW Tower", "Web Developer")

    print(student.showinfo())
    print(student.getrole())

    print(employee.showinfo())
    print(employee.getrole())

    print(teacher.showinfo())
    print(teacher.getrole())

    print(developer.showinfo())
    print(developer.getrole())


if __name__ == "__main__":
    main()


# todo Additional exercise


class RoleManager:
    def __init__(self):
        self.peoples = []

    def addperson(self, person):
        if not isinstance(person, Person):
            raise TypeError("Only Person subclass can be added.")
        self.peoples.append(person)

    def displayall(self):
        for people in self.peoples:
            print(people.showinfo())

    def countbyrole(self, role):
        return sum(1 for people in self.peoples if people.getrole() == role)


rolemanagerObj = RoleManager()
rolemanagerObj.addperson(Student("Aung Aung", 23, "Std1001", "Computer Science"))
rolemanagerObj.addperson(Employee("John Doe", 23, "EMP1001", "Hr Department"))
rolemanagerObj.addperson(Teacher("Alice", 50, "TR1001", "Mathematic", "Math"))
rolemanagerObj.addperson(Developer("Bob", 33, "DEV1001", "MGW Tower", "Web Developer"))

rolemanagerObj.displayall()

print(f"Number of students: {rolemanagerObj.countbyrole("Student")}")
print(f"Number of teachers: {rolemanagerObj.countbyrole("Teacher")}")
print(f"Number of employees: {rolemanagerObj.countbyrole("Employee")}")
