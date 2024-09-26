
import numpy as np

if __name__ == '__main__':
  from RandGenerator import genRandId
  from GeneratePlayers import players_generated
else: 
  from Modules.RandGenerator import genRandId
  from Modules.GeneratePlayers import players_generated

# Variables
# Used Id is to keep track of cards already drawn from deck
global used_Id
num_cards_drawn = 7
used_Id = []

def drawCard ():
  """"This function draws a card using a reandom ID generator"""

  # Variables for cards 
  #num_attribute = np.arange(10).astype(str)
  num_attribute = range(1, 10)
  colour_atrr = ['darkred','darkblue','darkorange','grey']
  action_attr = ['act_1', 'act_2', 'act_3']
  wild_cards = ['W_1', 'W_2', 'W_3']
  wild_colour = 'black'

  #TYPES OF CARDS
  # colour & num with card_type_Id 0
  # Action card & colour with card_type_ID 1
  # Wild card isnt mapped with any other variable with card_type_ID 2
  
  colourNum_size = len(colour_atrr)*len(num_attribute)
  actColour_size = len(action_attr)*len(colour_atrr)
  wild_size = len(wild_cards)
  Num_unique_cards = colourNum_size + actColour_size + wild_size
  
  # Probaility of drawing a Wild cards
  Prob_wildCard = wild_size/Num_unique_cards 
  # Probaility of drawing a card with Action and Colour characteristics
  Prob_actionColor = actColour_size/Num_unique_cards
  # Probaility of drawing a card with Colour and Number characteristics
  Prob_colourNum = colourNum_size/Num_unique_cards
  
  # Rand float is to detrmine whic card of the charateristics is drawn
  # For the cards besided Wild cards, genRandId functions generated random Id to choose randomly betwen the given two chateristics that make up the card of the corresponding type.
  rand_float = np.random.random()

  # Condition for wild cards
  if 0 <= rand_float < Prob_wildCard:
    indx = np.random.randint(low = 0, high = wild_size)
    card = wild_cards[indx]
    card = [card, wild_colour]
    card_type_ID = 0
    unique_Id = card_type_ID, indx
    used_Id.append(unique_Id)

  # Condition for card with attribute Act & colour
  max = Prob_wildCard + Prob_actionColor
  if Prob_wildCard <= rand_float < max:
    intra_Id, card = genRandId(action_attr, colour_atrr, output_Id = True)
    card_type_ID = 1
    unique_Id = card_type_ID, intra_Id
    used_Id.append(unique_Id)

  # Condition for card with attribute number & colour
  max = Prob_wildCard + Prob_actionColor + Prob_colourNum
  if Prob_wildCard + Prob_actionColor <= rand_float < max:
    intra_Id, card = genRandId(num_attribute, colour_atrr, output_Id = True)
    card_type_ID = 2
    unique_Id = card_type_ID, intra_Id
    used_Id.append(unique_Id)
    
  return card

def drawCards(num_cards_drawn):
  cards = [drawCard() for _ in range(num_cards_drawn)]
  return cards

# Main return is players_cards. Players_generated is fetched from GeneratePlayers
# player_cards is to be passed to DrawCrads module
players_cards = players_generated

def RunMain ():
  """" 
  Main return is players_cards:
  players_generated is fetched from GeneratePlayers
  """
  for player in players_cards.keys():
    players_cards[player] = drawCards(num_cards_drawn)

RunMain()
