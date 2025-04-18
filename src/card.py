class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def printCard(self):
        match self.suit:
            case "Hearts":
                print(heartsCard(self.value),end="")
            case "Diamonds":
                print(diamondsCard(self.value),end="")
            case "Clubs":
                print(clubsCard(self.value),end="")
            case "Spades":
                print(spadesCard(self.value),end="")
            case _:
                print("No card found for that suit")


    def clubsCard(value) -> str:
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

    def heartsCard(value) -> str:
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

    def diamondsCard(value) -> str:
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

    def spadesCard(value) -> str:
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