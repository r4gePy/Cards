from random import choice
from Card import Card
from Player import Player


class Deck:
    def __init__(self):
        self.cards_values = {
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
        self.types_exem = Card()

    def give_one_card(self, human):
        card = choice(self.types_exem.types)
        if "Т" in card:
            if human.points <= 10:
                points = 11
            else:
                points = 1
        else:
            points = self.cards_values.get(card)
        human.points += points
        human.cards.append(card)

    def give_cards(self, human):
        for _ in range(2):
            card = choice(self.types_exem.types)
            human.cards.append(card)
            if "Т" in card:
                if human.points <= 10:
                    points = 11
                else:
                    points = 1
                human.points += points
            else:
                human.points += self.cards_values.get(card)


pl = Player()
