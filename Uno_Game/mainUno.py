from Input import *
from RandGenerator import randId 


# Variables for cards 
colour = ['red','blue','yellow','white']
card_num = list(range(10))

num_drawn_cards = 7
used_Id = []

for player, cards in player_names.items():
		rand_choice = randId(colour, card_num, exclude = used_Id)
		# rand_choice returns unique Id as first returnn value
		used_Id.append(rand_choice[0]) 
		player_names[player] = [rand_choice[1] for _ in range(num_drawn_cards)]
		
print (player_names, used_Id)

