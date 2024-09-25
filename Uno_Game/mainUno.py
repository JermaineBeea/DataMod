from Input import *
from Modules.RandGenerator import randId, generateExclude


# Variables for cards 

colour = ['red','blue','yellow','white']
card_num = list(range(10))
wild_card = ['W_1', 'W_2', 'W_3']
action_cards = ['act_1', 'act_2', 'act_3']
wild_cards = ['W_1', 'W_2', 'W_3']

#TYPES OF CARDS
# colour & num
# Action card & colour
# Wild card isnt mapped with any other variable
colourNum_size = len(colour)*len(card_num)
actColour_size = len(action_cards)*len(colour)
wild_size = len(wild_card)

used_Id = []
Num_unique_cards = colourNum_size + actColour_size + wild_size
valid_range = generateExclude(used_Id, start = 0, end = Num_unique_cards)
rand_Id = np.random.choice(valid_range)

# Condition for wild card
# Colour for wild card is constant
if 0 <= rand_Id < wild_size:
  indx = wild_size - rand_Id
  wild_colour = 'brown'
  drawn_card = wild_card[indx]
  drawn_card = [drawn_card, wild_colour]

# Condition for card Act and olour
max = wild_size + actColour_size
if wild_size <= rand_Id < max:
  indx = max - rand_Id


# Condition for Colour and Num card
max = Num_unique_cards
if wild_size + actColour_size <= rand_Id < max:
  indx = max - rand_Id
  card = rand_Id()
  used_Id = []

for player, cards in player_names.items():
# rand_choice returns unique Id as first returnn value
for _ in range(num_drawn_cards):
  rand_choice = randId(card_num, colour, exclude = used_Id)
  used_Id.append(rand_choice[0]) 
  cards.append(rand_choice[1])

  print (f'{player_names}\n')
  print(used_Id)

