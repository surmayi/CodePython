# all methods and properties in a class are publicly available by default.
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        #Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class.
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)

class Student:

    def __init__(self,name,result,id):
        self.name = name
        self.__result=result
        self._id=id

    def __printName(self,):
        print(self.name)

    def printResult(self):
        print(self.__result)

    def _printId(self):
        print(self._id)

student = Student('Surmayi',95,1001)

print(student.name)
student.printResult()

print(student._Student__printName())
print(student._printId())

Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error since we are trying to access private data type

Steve.displaySalary()
Steve.__displayID()  # this will generate an error

# If the user believes it is absolutely necessary to access a private property or a method,
# they can access it using the _<ClassName> prefix for the property or method
print(Steve._Employee__salary)  # accessing a private property