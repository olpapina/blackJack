from game import Game
from hand import Hand

players = []
players_dict = {}
players_bet = {}
dealer_hand = Hand(True)
game = Game(players_dict, dealer_hand)
deck = []
while True:
    quantity = input("Select quantity of players from 1 to 7 > ")
    if not quantity.isdecimal():
        continue
    quantity = int(quantity)
    if 1 <= quantity <= 7:
        print("""{} players in the game
        """.format(quantity))
        for player in range(1, quantity + 1):
            players.append("player" + str(player))
        players_dict = dict.fromkeys(players, 0)
        players_bet = dict.fromkeys(players, 0)
        for key in players_dict:
            players_dict[key] = Hand(False)
        deck = game.cards
        deck.shuffle()
        completed_bet = game.start_game(players_dict, players_bet, deck)
        print("Completed", completed_bet)
        for key in players_dict:
            if completed_bet[key] == 0:
                completed_bet[key] = completed_bet.pop(key)
            # players_dict = players_dict.pop(key)
        break
    else:
        print("Enter quantity of players from 1 to 7 >")
        break
game.play_game_round(players_dict, deck)
game.play_dealer(dealer_hand, deck)
game.count_result(players_dict, players_bet, dealer_hand)
