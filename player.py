class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.cards_taken = []

    def print_cards(self):
        print(self.name + '\'s cards:')
        for c in self.cards:
            print(c)

    def get_greedy_card(self, suit):
        # cards for the current round (same suit)
        round_cards = []
        diff_cards = []
        for card in self.cards:
            if card.suit == suit:
                round_cards.append(card)
            else:
                diff_cards.append(card)

        if round_cards:
            temp = round_cards[0]
            for card in round_cards:
                if card < temp:
                    temp = card
            print(self.name + '\'s lowest ' + suit + ':', temp)
            index = self.cards.index(temp)
            g_card = self.cards.pop(index)
            # print(index)
            for c in self.cards:
                print(c)
            return g_card
        else:
            temp = diff_cards[0]
            for card in diff_cards:
                if card < temp:
                    temp = card
            print(self.name + '\'s lowest non-' + suit + ':', temp)
            index = self.cards.index(temp)
            g_card = self.cards.pop(index)
            # print(index)
            for c in self.cards:
                print(c)
            return g_card


    def __str__(self):
        print(self.name)
