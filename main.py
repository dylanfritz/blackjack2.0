from game import Game
game = Game()
numHumans = int(input("How many human players do you want to add? "))
for _ in range(numHumans):
    playerName = input("Enter the player's name: ")
    game.addPlayer(playerName, False, False)

numRobots = int(input("How many robot players do you want to add? "))
game.printStatus()
game.playGame(numRobots)


