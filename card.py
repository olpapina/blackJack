class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def display_card(self):
        print(self.get_rank(), self.get_suit())
