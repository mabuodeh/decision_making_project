from deckInit import Deck, Card, deal_cards
# create 4 player objects
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

p1 = Player('player 1')
p2 = Player('player 2')
p3 = Player('player 3')
p4 = Player('player 4')


deck = Deck()

deal_cards(deck, p1, p2, p3, p4)

print('player1\'s cards:')
print(len(p1.cards))
for c in p1.cards:
    print(c)
print('player2\'s cards:')
for c in p2.cards:
    print(c)
print('player3\'s cards:')
for c in p3.cards:
    print(c)
print('player4\'s cards:')
for c in p4.cards:
    print(c)
