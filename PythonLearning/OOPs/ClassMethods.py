class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    # Class methods work with class variables and are accessible using the class name rather than its object.
    # Since all the class objects share the class variables, the class methods are used to access and modify class variables.
    # Just like instance methods, all class methods have at least one argument, cls
    @classmethod
    def getTeamName(cls):
        return cls.teamName


print(Player.getTeamName())