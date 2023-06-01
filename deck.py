import random
from card import Card


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
        # for card in self.cards:
        #     print("card ", card.get_suit(), card.get_rank(), "\n")
        # print("__________")
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        # for card in self.cards:
        #     print("card ", card.get_suit(),card.get_rank(), "\n")
        # print(self.cards.__len__())

    def deal_card(self):
        if len(self.cards) > 0:
            deal_cart = self.cards.pop(-1)
            return deal_cart
