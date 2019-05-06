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

    def get_round_player(self, cur_suit):
        player_list = [(self.first_player, self.first_card),
        (self.second_player, self.second_card),
        (self.third_player, self.third_card),
        (self.fourth_player, self.fourth_card)]

        for idx, pl in enumerate(player_list):
            if pl[1].suit == cur_suit:
                start_index = idx
                break
        player_list[0], player_list[idx] = player_list[idx], player_list[0]


        # print(player_list[start_index][0].name)
        ret_player = player_list[0]
        iter_player_list = iter(player_list)
        next(iter_player_list)
        for pl in iter_player_list:
            if pl[1].suit == ret_player[1].suit and pl[1] > ret_player[1]:
                ret_player = pl
        return ret_player







    def __str__(self):
        return "{}, {}\n{}, {}\n{}, {}\n{}, {}\n".format(self.first_player,
        self.first_card, self.second_player, self.second_card,
        self.third_player, self.third_card, self.fourth_player, self.fourth_card)
