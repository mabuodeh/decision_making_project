# from deckInit import Card
# from player import Player

class Table:
    def __init__(self):
        # self.first = Card('Hearts', '7')
        # self.first_player = Player
        # self.second = Card('Hearts', '7')
        # self.third = Card('Hearts', '7')
        # self.fourth = Card('Hearts', '7')
        self.first_card = None
        self.first_player = None
        self.second_card = None
        self.second_player = None
        self.third_card = None
        self.third_player = None
        self.fourth_card = None
        self.fourth_player = None

    def __str__(self):
        return "{}, {}\n{}, {}\n{}, {}\n{}, {}\n".format(self.first_player,
        self.first_card, self.second_player, self.second_card,
        self.third_player, self.third_card, self.fourth_player, self.fourth_card)
