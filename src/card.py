class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def printCard(self):
        match self.suit:
            case "Hearts":
                print(self.heartsCard(self.value))
            case "Diamonds":
                print(self.diamondsCard(self.value))
            case "Clubs":
                print(self.clubsCard(self.value))
            case "Spades":
                print(self.spadesCard(self.value))
            case _:
                print("No card found for that suit")


    def clubsCard(self,value) -> str:
        return f'''    _______________
        | {value}           |
        |             |
        |             |
        |      O      |
        |     O O     |
        |      Ƴ      |
        |             |
        |           {value} |
        ---------------'''

    def heartsCard(self,value) -> str:
        return f'''    _______________
        | {value}           |
        |             |
        |     ∩ ∩     |
        |    | ˇ |    |
        |     \ /     |
        |      ∨      |
        |             |
        |           {value} |
        ---------------'''

    def diamondsCard(self,value) -> str:
        return f'''    _______________
        | {value}           |
        |             |
        |      ∧      |
        |     / \     |
        |     \ /     |
        |      ∨      |
        |             |
        |           {value} |
        ---------------'''

    def spadesCard(self,value) -> str:
        return f'''    _______________
        | {value}           |
        |             |
        |      ∧      |
        |     / \     |
        |    C   Ↄ    |
        |      Y      |
        |             |
        |           {value} |
        ---------------'''