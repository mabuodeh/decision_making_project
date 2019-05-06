from deckInit import Deck, Card, deal_cards
from player import Player
# create 4 player objects


p1 = Player('player 1')
p2 = Player('player 2')
p3 = Player('player 3')
p4 = Player('player 4')


deck = Deck()

deal_cards(deck, p1, p2, p3, p4)

p1.print_cards()
p2.print_cards()
p3.print_cards()
p4.print_cards()
