import random
from player import Player
from deck import Deck
from card import Card

class Game:
    gameSuits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    gameValues = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.gameDeck = Deck(Game.gameSuits, Game.gameValues)
        self.gameDeck.shuffle()
        self.players = []
        self.addPlayer("Dealer", True, True)

    def printDeck(self):
        print(self.gameDeck)

    def printStatus(self):
        print(self.gameDeck)
        for player in self.players:
            player.printStatus();
        

    def dealCard(self, player):
        dealtCard = self.gameDeck.draw()
        if dealtCard.value == "K" or dealtCard.value == "Q" or dealtCard.value == "J":
            player.totalValue += 10
        elif dealtCard.value == "A" and player.totalValue <= 10:
            player.totalValue += 11
        elif dealtCard.value == "A" and player.totalValue > 10:
            player.totalValue += 1
        else:
            player.totalValue += int(dealtCard.value)
        player.heldCards.append(dealtCard)

    def addPlayer(self, *args, **kwargs):
        if len(args) == 0:
            self.players.append(Player())
        elif len(args) == 1:
            self.players.append(Player(args[0]))
        elif len(args) == 2:
            self.players.append(Player(args[0],args[1]))
        elif len(args) == 3:
            self.players.append(Player(args[0],args[1],args[2]))


    def dealCards(self):
        for player in self.players:
            self.dealCard(player)
        for player in self.players:
            self.dealCard(player)

    



    def takeTurn(self, player):

        if player.isRobot:
            print(f"PLAYER {player.name} IS ROBOT")
            if player.totalValue < 17:
                self.dealCard(player)

        else: #player is human
            humanChoice = None
            for card in player.heldCards:
                card.printCard()
            while humanChoice != "hit" and humanChoice != "hold":
                humanChoice = input(f"Player {player.name} your current score is {str(player.totalValue)}.\nDo you want to hit or hold?").lower()
            if humanChoice == "hit":
                self.dealCard(player)
                print(f"{player.name} you were dealt {str(player.heldCards[-1])}")
            else: 
                player.status = "holding"

            

    def shuffleCards(self):
        for player in self.players:
            self.gameDeck.cards += player.heldCards
            player.heldCards.clear()
        self.gameDeck.shuffle()
    
    def checkScores(self): #invalidate any players with scores over 21
        for player in self.players:
            if player.totalValue > 21:
                player.status = "bust"
            elif len(player.heldCards) == 2 and player.totalValue == 21:
                player.status = "natural"
            elif player.totalValue >= 17 and player.isRobot:
                player.status = "holding"

    def allPlayersDone(self) -> bool:
        for player in self.players:
            if player.status == "playing":
                return False
        return True
    
    def findWinners(self) -> bool: #returns True if at least one player has won. returns false if there were no winners
        dealerScore = self.players[0].totalValue
        for player in self.players:
            if player.totalValue <= 21 and player.totalValue > dealerScore:
                player.winner = True
            elif player.totalValue <= 21 and self.players[0].status=='bust':
                player.winner = True
        
        for i in range(1,len(self.players)):
            if self.players[i].winner:
                return True
        return False
            
        
        

    def playGame(self, numPlayersAdd):
        for i in range(numPlayersAdd):
            self.addPlayer()
        self.dealCards()
        while not self.allPlayersDone():
            self.printStatus()
            for player in self.players:
                if player.status == "playing":
                    self.takeTurn(player)
            self.checkScores();
        isWinner = self.findWinners()
        self.printStatus()
        print("DEALER STATS:")
        self.players[0].printStatus()
        if not isWinner:
            print("No players beat the dealer!!")
        else:
            print("The following players have won:")
            count = 0
            for player in self.players:
                if player.winner:
                    count += 1
                    player.printStatus()
            print(f"A total of {count} players have won.")