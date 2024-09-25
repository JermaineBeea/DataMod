#from Input import *
import numpy as np
from Modules.RandGenerator import genRandId, generateExclude


def drawCard ():
  # Variables for cards 
  colour = ['red','blue','yellow','white']
  card_num = list(range(10))
  action_attr = ['act_1', 'act_2', 'act_3']
  wild_cards = ['W_1', 'W_2', 'W_3']

  #TYPES OF CARDS
  # colour & num
  # Action card & colour
  # Wild card isnt mapped with any other variable
  colourNum_size = len(colour)*len(card_num)
  actColour_size = len(action_attr)*len(colour)
  wild_size = len(wild_cards)

  used_Id = []
  Num_unique_cards = colourNum_size + actColour_size + wild_size
  valid_range = list(generateExclude(used_Id, start = 0, end = Num_unique_cards))
  rand_Id = np.random.choice(valid_range)

  # Condition for wild card
  # Colour for wild card is constant
  if 0 <= rand_Id < wild_size:
    indx = wild_size - rand_Id
    wild_colour = 'brown'
    card = wild_cards[indx]
    card = [card, wild_colour]

  # Condition for card with attribute Act & colour
  max = wild_size + actColour_size
  if wild_size <= rand_Id < max:
    indx = max - rand_Id
    card = genRandId(action_attr, colour, unique_Id = indx)

  # Condition for card with attribute number & colour
  max = Num_unique_cards
  if wild_size + actColour_size <= rand_Id < max:
    indx = max - rand_Id
    card = genRandId(card_num, colour, unique_Id = indx )
    
  return card