import random

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
                if card > temp:
                    temp = card
            print(self.name + '\'s highest non-' + suit + ':', temp)
            index = self.cards.index(temp)
            g_card = self.cards.pop(index)
            # print(index)
            for c in self.cards:
                print(c)
            return g_card

    def get_random_suit(self):
        suits = []
        for cs in self.cards:
            suits.append(cs.suit)
        return random.choice(suits)

    def calculate_score(self):
        # -15 / Round
        rounds_won = len(self.cards_taken)/4
        # -10 / Diamond
        # -25 / Queen
        # -75 / King of Hearts
        diamonds_won = 0
        queens_won = 0
        king_hearts_won = 0
        for c in self.cards_taken:
            if c.suit == 'Diamonds':
                diamonds_won += 1
            if c.rank == 'Q':
                queens_won += 1
            if c.rank == 'K' and c.suit == 'Hearts':
                king_hearts_won = 1
        return ((rounds_won * -15) + (diamonds_won * -10) + (queens_won * -25) + (king_hearts_won * -75))



    def __str__(self):
        return self.name
