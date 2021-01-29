class Player:
    formerTeams = []  # class variables - incorrect usage
    teamName = 'Liverpool'

    def __init__(self, name):
        self.name = name  # creating instance variables


p1 = Player('Mark')
p2 = Player('Steve')

p1 = Player('Mark')
# BOth players could have different former team, however, each player's former team will get added to same variable
p1.formerTeams.append('Barcelona')
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)