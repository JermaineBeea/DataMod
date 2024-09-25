from Input import *
from RandGenerator import randId 


# Variables for cards 
colour = ['red','blue','yellow','white']
card_num = list(range(10))

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

