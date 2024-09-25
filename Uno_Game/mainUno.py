from Input import *
from Modules.RandGenerator import randId 


# Variables for cards 
wild_card = ['W_1', 'W_2', 'W_3']
colour = ['red','blue','yellow','white']
card_num = list(range(10))
action_cards = ['act_1', 'act_2', 'act_3']
wild_card = ['W_1', 'W_2', 'W_3']

num_drawn_cards = 4
used_Id = []

for player, cards in player_names.items():
  # rand_choice returns unique Id as first returnn value
  for _ in range(num_drawn_cards):
    rand_choice = randId(card_num, colour, exclude = used_Id)
    used_Id.append(rand_choice[0]) 
    cards.append(rand_choice[1])
		
print (f'{player_names}\n')
print(used_Id)

