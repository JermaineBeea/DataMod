import numpy as np

# Import based on execution context
if __name__ == '__main__':
  from GeneratePlayers import players_generated
else:
  from Modules.RandGenerator import modulos
  from GameModules.GeneratePlayers import players_generated

# Number of cards drawn for each player
num_cards_drawn = 7

def drawCard(used_Id):
  """
  Draws a card using a random ID and ensures it hasn't been drawn before.

  Args:
      used_Id (list): List of IDs for cards that have already been drawn.

  Returns:
      tuple: A card and the updated list of used IDs.
  """
  
  # Card attributes
  num_attribute = range(1, 10)
  colour_attr = ['darkred', 'darkblue', 'darkorange', 'grey']
  action_attr = ['act_1', 'act_2', 'act_3']
  wild_cards = ['W_1', 'W_2', 'W_3']
  wild_colour = 'black'

  # Calculate the size of each card pool
  colourNum_size = len(colour_attr) * len(num_attribute)  # Number-color cards
  actColour_size = len(action_attr) * len(colour_attr)    # Action-color cards
  wild_size = len(wild_cards)                             # Wild cards
  Num_unique_cards = colourNum_size + actColour_size + wild_size  # Total number of cards
  
  while True:
    # Generate a random unique ID for the card
    unique_Id = np.random.randint(low=0, high=Num_unique_cards, size=1)[0]  # Convert to scalar
    
    # Condition for drawing a wild card
    if 0 <= unique_Id < wild_size:
      indx = unique_Id
      card = wild_cards[indx]
      card = [card, wild_colour]  # Wild card is always paired with 'black'
    
    # Condition for drawing an action-color card
    elif wild_size <= unique_Id < (wild_size + actColour_size):
      indx_a, indx_b = modulos(len(colour_attr), unique_Id - wild_size)
      card = [action_attr[indx_a], colour_attr[indx_b]]
    
    # Condition for drawing a number-color card
    else:
      indx_a, indx_b = modulos(len(colour_attr), unique_Id - (wild_size + actColour_size))
      card = [num_attribute[indx_a], colour_attr[indx_b]]
    
    # Ensure the card hasn't already been drawn
    if unique_Id not in used_Id:
      used_Id.append(unique_Id)
      break
  
  return card, used_Id

def drawCards(num_cards_drawn, used_Id):
  """
  Draws multiple unique cards.

  Args:
      num_cards_drawn (int): Number of cards to draw.
      used_Id (list): List of used IDs to ensure uniqueness.

  Returns:
      list: List of drawn cards.
  """
  cards = [drawCard(used_Id)[0] for _ in range(num_cards_drawn)]
  return cards

# Main function to draw cards for all players
players_cards = players_generated

def RunDrawCards():
  """
  Main function to distribute cards to all players.
  Ensures each player receives a unique set of cards.
  """
  used_Id = []  # Track IDs of drawn cards to avoid duplicates
  for player in players_cards.keys():
    players_cards[player] = drawCards(num_cards_drawn, used_Id)


