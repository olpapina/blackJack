import sys

from modules.deck import Deck
from modules.game import Game
from modules.hand import Hand

players = []
players_dict = {}
players_bet = {}
dealer_hand = Hand(True)
game = Game(players_dict, dealer_hand)
deck = []
print("Welcome to BlackJack game")
while True:
    quantity = input("Select quantity of players from 1 to 7 > ")
    if not quantity.isdecimal():
        continue
    quantity = int(quantity)
    if 1 <= quantity <= 7:
        print("{} players in the game".format(quantity))
        for player in range(1, quantity + 1):
            players.append("player" + str(player))
        players_dict = dict.fromkeys(players, 0)
        players_bet = dict.fromkeys(players, 0)
        for key in players_dict:
            players_dict[key] = Hand(False)
        deck = game.cards
        deck.shuffle()
        break
    else:
        print("Try to enter allowed values")
        continue
while True:
    if deck.get_cards().__len__() > 25:
        players_round = players_dict.copy()
        completed_bet = game.start_game(players_dict, players_bet, deck)
        for key in completed_bet:
            if completed_bet[key] == 0:
                del players_round[key]
        if players_round.__len__() > 0:
            game.play_game_round(players_round, deck)
            game.play_dealer()
            game.count_result(players_round, players_bet, dealer_hand)
        else:
            print("Dealer is waiting for your bet")
            continue
    else:
        next_game = input("Would you like play with current players? Y/N > ").upper().strip()
        if next_game == 'Y':
            deck = Deck()
            deck.shuffle()
        else:
            print("Game is completed!")
            sys.exit()
