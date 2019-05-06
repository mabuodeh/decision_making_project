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
        player_list = [{"p": self.first_player, "c": self.first_card},
        {"p": self.second_player, "c": self.second_card},
        {"p": self.third_player, "c": self.third_card},
        {"p": self.fourth_player, "c": self.fourth_card}]

        for idx, pl in enumerate(player_list):
            if pl["c"].suit == cur_suit:
                start_index = idx
                break
        player_list[0], player_list[idx] = player_list[idx], player_list[0]


        # print(player_list[start_index][0].name)
        ret_player = player_list[0]
        iter_player_list = iter(player_list)
        next(iter_player_list)
        for pl in iter_player_list:
            if pl["c"].suit == ret_player["c"].suit and pl["c"] > ret_player["c"]:
                ret_player = pl

        # print("swap procedure, current card:")
        # print(ret_player["c"])
        # print("cards in hand:")
        # for cr in ret_player["p"].cards:
        #     print(cr)
        #     if cr.suit == ret_player["c"].suit and cr > ret_player["c"]:
        #         print("swapping")
        #         print(cr)
        #         print(ret_player["c"])
        #         cr, ret_player["c"] = ret_player["c"], cr

        ret_player["p"].cards_taken.extend([player_list[0]["c"],
        player_list[1]["c"], player_list[2]["c"], player_list[3]["c"]])
        return ret_player







    def __str__(self):
        return "{}, {}\n{}, {}\n{}, {}\n{}, {}\n".format(self.first_player,
        self.first_card, self.second_player, self.second_card,
        self.third_player, self.third_card, self.fourth_player, self.fourth_card)
