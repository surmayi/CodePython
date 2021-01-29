class BodyInfo:
# Static methods do not know anything about the state of the class, i.e., they cannot modify class attributes.
# Static methods can be accessed using the class name or the object name.
# It does not use a reference to the object or class, so we do not have to use self or cls
    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))