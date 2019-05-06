from deckInit import Deck, Card, deal_cards
# create 4 player objects
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

def print_player_cards(pl):
    print(pl.name + '\'s cards:')
    for c in pl.cards:
        print(c)


p1 = Player('player 1')
p2 = Player('player 2')
p3 = Player('player 3')
p4 = Player('player 4')


deck = Deck()

deal_cards(deck, p1, p2, p3, p4)

print_player_cards(p1)
print_player_cards(p2)
print_player_cards(p3)
print_player_cards(p4)
