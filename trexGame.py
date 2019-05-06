from deckInit import Deck, Card, deal_cards
from player import Player
from table import Table
import random

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
deck_suits = deck.suit
table = Table()

deal_cards(deck, p1, p2, p3, p4)

# p1.print_cards()
# p2.print_cards()
# p3.print_cards()
# p4.print_cards()

# show_lowest_card(p1)
# p1.cards.sort()
# p1.print_cards()

# add players to list of players
player_list = [p1, p2, p3, p4]
# check who starts (the player with 7 of hearts)
# get that player's index to keep track of who starts each round
if Card('7', 'Hearts') in p1.cards:
    cur_player_index = player_list.index(p1)
elif Card('7', 'Hearts') in p2.cards:
    cur_player_index = player_list.index(p2)
elif Card('7', 'Hearts') in p3.cards:
    cur_player_index = player_list.index(p3)
elif Card('7', 'Hearts') in p4.cards:
    cur_player_index = player_list.index(p4)

cur_player = player_list[cur_player_index]
# enter loop of game (while player 1 still has cards)
while len(p1.cards) > 0:
    rand_suit = cur_player.get_random_suit()

    # first player, get suit of greedy card
    table.first_card = cur_player.get_greedy_card(rand_suit)
    table.first_player = cur_player

    # second player
    cur_player_index = (cur_player_index + 1) % 4
    cur_player = player_list[cur_player_index]
    table.second_card = cur_player.get_greedy_card(rand_suit)
    table.second_player = cur_player

    # third player
    cur_player_index = (cur_player_index + 1) % 4
    cur_player = player_list[cur_player_index]
    table.third_card = cur_player.get_greedy_card(rand_suit)
    table.third_player = cur_player

    # fourth player
    cur_player_index = (cur_player_index + 1) % 4
    cur_player = player_list[cur_player_index]
    table.fourth_card = cur_player.get_greedy_card(rand_suit)
    table.fourth_player = cur_player

    # when all 4 players play, check which card is greatest
    # give cards to that player
    winner_tuple = table.get_round_player(rand_suit)
    print('cards taken by ' + winner_tuple["p"].name + ' :')
    for ctaken in winner_tuple["p"].cards_taken:
        print(ctaken)
    print('\n')


print(p1.calculate_score())
print(p2.calculate_score())
print(p3.calculate_score())
print(p4.calculate_score())
