from modules.chip import Chip


class Hand:
    def __init__(self, dealer):
        self.dealer = dealer
        self.cards = []
        self.chip = Chip(100)

    def add_cards(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_ace = 0
        for card in self.cards:
            rank = card.get_rank()
            if rank == 'A':
                num_ace += 1
            elif rank in ('J', 'Q', 'K'):
                value += 10
            else:
                value += int(rank)

        if num_ace == 4 and value <= 7:
            value += 14
        elif num_ace == 3 and value <= 8:
            value += 13
        elif num_ace == 2 and value <= 9:
            value += 12
        elif num_ace == 1 and value <= 10:
            value += 11
        elif num_ace == 1 and value > 10:
            value += 1
        return value

    def get_cards(self):
        return self.cards

    def get_chip(self):
        return self.chip

    def set_clean_cards(self):
        self.cards = []
