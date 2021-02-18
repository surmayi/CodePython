class Player:
    teamName = 'Liverpool'  # class variables - current team, same for all players

    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = []  # former team, which could be different for different players


p1 = Player('Mark')
p1.formerTeams.append('Barcelona')
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)