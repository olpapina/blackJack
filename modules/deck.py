import random
from modules.card import Card


class Deck:
    def __init__(self):
        self.cards = []
        suits = (chr(9829), chr(9830), chr(9824), chr(9827))
        rank_digits = tuple(range(2, 11))
        rank_letters = ('J', 'Q', 'K', 'A')
        ranks = rank_digits + rank_letters
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, str(rank)))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            deal_cart = self.cards.pop(-1)
            return deal_cart

    def get_cards(self):
        return self.cards
