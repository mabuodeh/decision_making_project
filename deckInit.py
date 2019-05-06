# code taken from:
# https://stackoverflow.com/questions/34006479/trying-to-implement-a-card-deck-sorting-algorithm-in-python

import random
# deck = ["2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC", "2D", "3D", "4D", "5D", "6D",
#        "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH",
#        "QH", "KH", "AH", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]
# deck = ['Ah', 'Jc', 'Qh', 'Kh', 'Kc', 'Jh', 'Ac', 'Qc']
from functools import total_ordering

graveyard = []



def num_rank(rank):
    if rank[0] == "J":
        return 11
    if rank[0] == "Q":
         return 12
    if rank[0] == "K":
         return 13
    if rank[0] == "A":
        return 14
    return int(rank)


@total_ordering
class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '%s of %s' % (self.rank,
                             self.suit)

    def __repr__(self): return str(self)

    def __lt__(self, other):
        t1 = self.suit, num_rank(self.rank)
        t2 = other.suit, num_rank(other.rank)
        return t1 < t2

    def __gt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 > t2

    def __eq__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 == t2

class Deck(object):
    def __init__(self):
        """
        Idea for this found here.
        https://stackoverflow.com/questions/8511745/sorting-a-hand-of-cards-accoring-to-rank-and-suit-in-python

        I could use this to ALWAYS have a shuffled deck at the beginning or to just start with a 'clean' deck as above...
        :return:
        """
        # self.rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        # self.suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.rank = ['2', '3', 'K', 'Q', 'J', '10', '9', '7']
        self.suit = ['Clubs', 'Hearts']
        self.deck = [Card(r, s) for r in self.rank for s in self.suit]
        random.shuffle(self.deck)

    def __getitem__(self, item):
        return self.deck[item]

    def deal(self):
        """
        Return a card from the deck.
        :return:
        """
        topCard = self.deck.pop(0)
        graveyard.append(topCard)
        # print(topCard)
        return topCard

    def shuffle(self):
        """
        Shuffle the deck
        :return:
        """
        self.deck.extend(graveyard)
        random.shuffle(self.deck)
        self.fan()

    def fan(self):
        """
        Print out the deck
        :return:
        """
        for card in self.deck:
            print(card)

    def order(self):
        return self.deck.sort()

    def printGraveyard(self):
        for dead in graveyard:
            print(dead)


def deal_cards(deck, p1, p2, p3, p4):
    while len(graveyard) <= 52 and len(deck.deck) > 0:
        # print('in while', len(deck.deck), len(graveyard))
        p1.cards.append(deck.deal())
        p2.cards.append(deck.deal())
        p3.cards.append(deck.deal())
        p4.cards.append(deck.deal())

# d.order()
# deck.fan()
