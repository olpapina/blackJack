

class Chip:
    def __init__(self, amount):
        self.amount = amount

    def add_chips(self, amount):
        self.amount += amount
        print("Your chips = {}".format(self.amount))

    def sub_chips(self, amount):
        self.amount -= amount
        print("Your chips = {}".format(self.amount))

    def get_bet(self, max_bet):
        while True:
            print("How much would you like to bet? (1-{}) or QUIT".format(max_bet))
            bet = input('> ').upper().strip()
            if bet == 'QUIT':
                print("Thanks for playing!")
                return 0
            if not bet.isdecimal():
                continue
            bet = int(bet)
            if 1 <= bet <= max_bet:
                if bet <= self.amount:
                    print("Your bet is ", bet)
                    print("")
                    break
                else:
                    print("Your bet should be <= {} (available chips)".format(self.amount))
            else:
                print("Please, select chips <= {}".format(max_bet))
        return bet
