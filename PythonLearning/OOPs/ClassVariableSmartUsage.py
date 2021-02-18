class Player:
    teamName = 'Liverpool'      # class variables
    teamMembers = [] # to save all player names of current team Liverpool

    def __init__(self, name):
        self.name = name        # creating instance variables
        self.formerTeams = []
        # instance variable to store each new player to class variable teamMembers
        self.teamMembers.append(self.name)


p1 = Player('Mark')
p2 = Player('Steve')

print("Name:", p1.name)
print("Team Members:")
print(p1.teamMembers)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.teamMembers)