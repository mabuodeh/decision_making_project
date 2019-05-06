from deckInit import Deck, Card, deal_cards
from player import Player

p1 = Player('player 1')
p2 = Player('player 2')
p3 = Player('player 3')
p4 = Player('player 4')

# def show_lowest_card(pl):
#     temp = ''
#     for c in pl.cards:
#         temp = c
#         if

deck = Deck()

deal_cards(deck, p1, p2, p3, p4)

p1.print_cards()
# p2.print_cards()
# p3.print_cards()
# p4.print_cards()

# show_lowest_card(p1)
# p1.cards.sort()
# p1.print_cards()

# cards for the current round (same suit)
round_cards = []
for card in p1.cards:
    if card.suit == 'Clubs':
        round_cards.append(card)

if round_cards:
    temp = p1.cards[0]
    for card in p1.cards:
        if card < temp:
            temp = card
print('lowest club:', temp)
