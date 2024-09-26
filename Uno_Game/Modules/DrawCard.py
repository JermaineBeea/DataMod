#from Input import *
import numpy as np
from RandGenerator import genRandId

def drawCard ():
  """"This function draws a card using a reandom ID generator"""

  # Variables for cards 
  num_attribute = list(np.arange(10).astype(str))
  colour_atrr = ['red','blue','yellow','white']
  action_attr = ['act_1', 'act_2', 'act_3']
  wild_cards = ['W_1', 'W_2', 'W_3']

  #TYPES OF CARDS
  # colour & num
  # Action card & colour
  # Wild card isnt mapped with any other variable
  colourNum_size = len(colour_atrr)*len(num_attribute)
  actColour_size = len(action_attr)*len(colour_atrr)
  wild_size = len(wild_cards)
  Num_unique_cards = colourNum_size + actColour_size + wild_size

  Prob_a = wild_size/Num_unique_cards
  Prob_b = actColour_size/Num_unique_cards
  Prob_c = colourNum_size/Num_unique_cards

  rand_float = np.random.random()

  # Condition for wild card
  # Colour for wild card is constant
  # Random index serves as Intra ID

  # Condition for wild cards
  if 0 <= rand_float < Prob_a:
    indx = np.random.randint(low = 0, high = wild_size)
    wild_colour = 'brown'
    card = wild_cards[indx]
    card = [card, wild_colour]
    card_type_ID = 0
    unique_Id = card_type_ID, indx

  # Condition for card with attribute Act & colour
  max = Prob_a + Prob_b
  if Prob_a <= rand_float < max:
    intra_Id, card = genRandId(action_attr, colour_atrr, output_Id = True)
    card_type_ID = 1
    unique_Id = card_type_ID, intra_Id

  # Condition for card with attribute number & colour
  max = Prob_a + Prob_b + Prob_c
  if Prob_a + Prob_b <= rand_float < max:
    intra_Id, card = genRandId(num_attribute, colour_atrr, output_Id = True)
    card_type_ID = 2
    unique_Id = card_type_ID, intra_Id

  return [(unique_Id), card]

if __name__ == '__main__':
  
  num_card = 4
  cards = [drawCard()[1] for _ in range(num_card)]
  print(cards)