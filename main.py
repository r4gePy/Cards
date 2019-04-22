from random import choice
from Dialer import Dialer
from Player import Player


def counts_points_of_cards(cards):
    points_add = 0
    for point in range(2):
        if len(cards[point]) == 3 \
                or "К" in cards[point] \
                or "В" in cards[point] \
                or "Д" in cards[point]:
            points_add += 10
        elif 'Т' in cards[point]:
            if points_add <= 10:
                points_add += 11
            else:
                points_add += 1
        else:
            points_add += int(cards[point][0])
    return points_add


class Main:
    def __init__(self):
        self.list_types = ['2♥', '2♦', '2♣', '2♠', '3♥', '3♦', '3♣', '3♠',
                           '4♥', '4♦', '4♣', '4♠', '5♥', '5♦', '5♣', '5♠', '6♥',
                           '6♦', '6♣', '6♠', '7♥', '7♦', '7♣', '7♠', '8♥',
                           '8♦', '8♣', '8♠', '9♥', '9♦', '9♣', '9♠',
                           '10♥', '10♦', '10♣', '10♠', 'В♥', 'В♦', 'В♣', 'В♠',
                           'Д♥', 'Д♦', 'Д♣', 'Д♠', 'К♥', 'К♦', 'К♣',
                           'К♠', 'Т♥', 'Т♦', 'Т♣', 'Т♠']
        self.dictionary_cards = {
            '2♥': 2, '2♦': 2, '2♣': 2, '2♠': 2, '3♥': 3, '3♦': 3, '3♣': 3,
            '3♠': 3,
            '4♥': 4, '4♦': 4, '4♣': 4, '4♠': 4, '5♥': 5, '5♦': 5, '5♣': 5,
            '5♠': 5, '6♥': 6,
            '6♦': 6, '6♣': 6, '6♠': 6, '7♥': 7, '7♦': 7, '7♣': 7, '7♠': 7,
            '8♥': 8,
            '8♦': 8, '8♣': 8, '8♠': 8, '9♥': 9, '9♦': 9, '9♣': 9, '9♠': 9,
            '10♥': 10, '10♦': 10, '10♣': 10, '10♠': 10, 'В♥': 10, 'В♦': 10,
            'В♣': 10, 'В♠': 10,
            'Д♥': 10, 'Д♦': 10, 'Д♣': 10, 'Д♠': 10, 'К♥': 10, 'К♦': 10,
            'К♣': 10,
            'К♠': 10, }

    def give_cards_user(self, player):
        for _ in range(2):
            player.points.append(choice(self.list_types))
        print("Ваши карты:\n", player.cards)

    def give_cards_dialer(self):
        for _ in range(2):
            self.cards_dialer.append(choice(self.list_types))
        print("Противник получил карты:\n * *")
        self.points_dialer += counts_points_of_cards(self.cards_dialer)

    def take_card(self, exem):
        card_add = choice(self.list_types)
        if "Т" in card_add:
            points = self.dictionary_cards.get(card_add)


    def return_points(self):
        self.points_player += counts_points_of_cards(self.cards_player)
        print("Кол-во ваших очков следующее:\n", self.points_player)

    def do_rate(self):
        self.money_dialer -= 10
        self.money_player -= 10


mn = Main()
pl = Player()
dl = Dialer()
mn.give_cards_user(pl)
