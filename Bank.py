class Bank:
    def __init__(self):
        self.money_player = 100
        self.money_dialer = 100

    def do_bet(self):
        self.money_player -= 10
        self.money_dialer -= 10

    def win(self, winner):
        if winner == "player":
            self.money_player += 10
        elif winner == "dialer":
            self.money_dialer += 10
        else:
            pass
