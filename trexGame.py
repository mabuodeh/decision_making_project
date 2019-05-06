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
# while len(p1.cards) > 0:
    # starting player plays greedy card of random suit
rand_suit = random.choice(deck_suits)

# first player, get suit of greedy card
table.first_card = cur_player.get_greedy_card(rand_suit)
table.first_player = cur_player

# check if next player has card of same suit to play
#   cur_player_index = (cur_player_index + 1)%4)
cur_player_index = (cur_player_index + 1) % 4
cur_player = player_list[cur_player_index]

# second player
table.second_card = cur_player.get_greedy_card(rand_suit)
table.second_player = cur_player
cur_player_index = (cur_player_index + 1) % 4
cur_player = player_list[cur_player_index]

# third player
table.third_card = cur_player.get_greedy_card(rand_suit)
table.third_player = cur_player
cur_player_index = (cur_player_index + 1) % 4
cur_player = player_list[cur_player_index]

# fourth player
table.fourth_card = cur_player.get_greedy_card(rand_suit)
table.fourth_player = cur_player

# if not, plays greedy card of some other suit
# when all 4 players play, check which card is greatest
# give cards to that player

# g_card = p1.get_greedy_card('Clubs')
# print('greedy card:', g_card)
