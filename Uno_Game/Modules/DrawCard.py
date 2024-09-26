import numpy as np
from RandGenerator import genRandId
from GeneratePlayers import players_generated

# Variables
num_cards_drawn = 7

def drawCard(used_Id):
    """This function draws a card using a random ID generator."""
    num_attribute = range(1, 10)
    colour_attr = ['darkred', 'darkblue', 'darkorange', 'grey']
    action_attr = ['act_1', 'act_2', 'act_3']
    wild_cards = ['W_1', 'W_2', 'W_3']
    wild_colour = 'black'

    # Calculate probabilities and card pool sizes
    colourNum_size = len(colour_attr) * len(num_attribute)
    actColour_size = len(action_attr) * len(colour_attr)
    wild_size = len(wild_cards)
    Num_unique_cards = colourNum_size + actColour_size + wild_size
    
    Prob_wildCard = wild_size / Num_unique_cards
    Prob_actionColor = actColour_size / Num_unique_cards
    Prob_colourNum = colourNum_size / Num_unique_cards
    
    while True:
      rand_float = np.random.random()
      
      # Condition for wild cards
      if 0 <= rand_float < Prob_wildCard:
        indx = np.random.randint(low=0, high=wild_size)
        card = wild_cards[indx]
        card = [card, wild_colour]
        card_type_ID = 2  # Wild cards
        unique_Id = (card_type_ID, indx)
      
      # Condition for card with action & colour
      elif Prob_wildCard <= rand_float < (Prob_wildCard + Prob_actionColor):
        intra_Id, card = genRandId(action_attr, colour_attr, output_Id=True)
        card_type_ID = 1  # Action cards
        unique_Id = (card_type_ID, intra_Id)
      
      # Condition for card with number & colour
      else:
        intra_Id, card = genRandId(num_attribute, colour_attr, output_Id=True)
        card_type_ID = 0  # Colour & number cards
        unique_Id = (card_type_ID, intra_Id)
      
      # Ensure unique card is not repeated
      if unique_Id not in used_Id:
        used_Id.append(unique_Id)
        break
    
    return card, used_Id

def drawCards(num_cards_drawn, used_Id):
    """Draw multiple cards."""
    cards = [drawCard(used_Id) for _ in range(num_cards_drawn)]
    return cards

# Main function to draw cards for all players
players_cards = players_generated

def RunMain():
    """Main function to distribute cards to players."""
    used_Id = []  # Initialize used card ID list
    for player in players_cards.keys():
        players_cards[player] = drawCards(num_cards_drawn, used_Id)

RunMain()
