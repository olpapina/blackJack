from modules.deck import Deck


class Game:
    def __init__(self, players, dealer):
        self.players = players
        self.dealer = dealer
        self.cards = Deck()

    def start_game(self, players_dict, players_bet, deck):
        self.dealer.cards = []
        for key in players_dict:
            player_hand = players_dict[key]
            player_hand.cards = []
        print("")
        print("New round start!")
        for i in range(2):
            self.dealer.add_cards(deck.deal_card())
            for key in players_dict:
                player_hand = players_dict[key]
                player_hand.add_cards(deck.deal_card())
                if i == 0:
                    chip = player_hand.get_chip()
                    print("{},".format(key))
                    players_bet[key] = chip.get_bet(100)
        card = self.dealer.cards[0]
        print("Dealer's opened card: ")
        card.display_card()
        return players_bet

    @staticmethod
    def play_game_round(players_dict, deck):
        for key in players_dict:
            player_hand = players_dict[key]
            while True:
                if player_hand.get_value() < 21:
                    print("")
                    print("{}, You should to Hit: ".format(key))
                    cards = player_hand.get_cards()
                    print("You have: ", player_hand.get_value())
                    for card in cards:
                        card.display_card()
                    hit = input("Would you like to Hit again? Enter Y/N> ").upper().strip()
                    if hit == 'Y':
                        next_card = deck.deal_card()
                        next_card.display_card()
                        player_hand.add_cards(next_card)
                    elif hit == 'N':
                        break
                    else:
                        continue
                else:
                    print("You have: ", player_hand.get_value())
                    break

    def play_dealer(self):
        print("Dealer opens second card:")
        cards = self.dealer.get_cards()
        card = cards[1]
        card.display_card()
        while True:
            if self.dealer.get_value() < 17:
                print("Dealer is Hit")
                self.dealer.add_cards(self.cards.deal_card())
            else:
                print("Dealer has: ", self.dealer.get_value())
                for card in cards:
                    card.display_card()
                print("Round is completed!")
                break

    @staticmethod
    def count_result(players_dict, players_bet, dealer):
        for key in players_dict:
            player_hand = players_dict[key]
            player_value = player_hand.get_value()
            dealer_value = dealer.get_value()
            chip = player_hand.get_chip()
            if dealer_value > 21 or dealer_value < player_value < 22:
                print("{}, You are a winner, congrats! ".format(key))
                chip.add_chips(players_bet[key])
            else:
                print("{}, You are a loser :( ".format(key))
                chip.sub_chips(players_bet[key])
