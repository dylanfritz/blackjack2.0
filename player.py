import copy
from card import Card


class Player:
    playerCount = 0
    def __init__(self, name="DEFAULT", isRobot=True, isDealer=False):
        Player.playerCount += 1
        self.playerID = Player.playerCount
        self.heldCards = []
        self.totalValue = 0
        self.status = "playing"
        self.winner = False

        if name == "DEFAULT":
            self.name = "Player"+str(Player.playerCount)
        else:
            self.name = name
        
        self.isRobot = isRobot
        self.isDealer = isDealer

    def __str__(self):
        return self.name

    def printStatus(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.playerID}")
        print(f"Cards: {[str(x) for x in self.heldCards]}")
        print(f"Total Score: {str(self.totalValue)}")
        print(f"Status: {self.status}")
        print(f"Winner: {self.winner}")