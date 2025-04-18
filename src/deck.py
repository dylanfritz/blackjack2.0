import random
from card import Card

class Deck:
    def __init__(self, suits, values):
        self.cards = []
        self.discard = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

        self.cardNum = len(suits)*len(values)
        self.totalNum = len(suits)*len(values)

    def __str__(self):
        prettyDeck = [str(x) for x in self.cards]
        return str(prettyDeck) + f"NUM OF CARDS ({self.cardNum})({self.totalNum})"
    
    #"top of deck" is end of list

    def draw(self) -> Card:
        drawnCard = self.cards.pop()
        self.cardNum -= 1
        return drawnCard

    def shuffle(self):
        self.cards += self.discard
        self.discard.clear()
        
        random.shuffle(self.cards)
        self.cardNum = self.totalNum
