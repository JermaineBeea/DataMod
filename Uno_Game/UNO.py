import random
from RandGenerator import randId
import numpy as np
import inspect

from UserInput import validateInput , AppendInput
from ReadWrite import write_toArray
from RandGenerator import generateExclude 

# This will print just the function names
display_module = False
if display_module:
  functions_list = inspect.getmembers(randId, inspect.isfunction)
  for func in functions_list:
      print(func[0])  

# Variables to be used globally throughut program
global num_char, number, colour, action, wild_cards
global wild_size, numColour_size, actColour_size, TotalUnique_cards
global NUM_cardsDrawn

num_char = 10
number = list(range(num_char))
colour = ['red', 'blue', 'yellow', 'green']
action = ['act_1', 'act_2', 'act_3']
wild_cards = ['skip', 'draw', 'reverse']

wild_size = len(wild_cards)
numColour_size = len(colour) * num_char
actColour_size = len(action) * len(colour)
TotalUnique_cards = numColour_size + actColour_size + wild_size

# Number of cards to be issued to each player, variable to be passed to drawCards function as a DEFAULT value
NUM_cardsDrawn = 7

def draw (ID_used = []):
  # Product Mapping Pairs: (num, colour), (action, colour), wild_cards

  set_UniqueID = list(generateExclude(ID_used, 0, TotalUnique_cards))
  rand_Id = random.choice(list(set_UniqueID))

  # ID for Wild card
  if 0 <= rand_Id < wild_size:
    # Get the index of the mapped set from the random Id generated
    mapped_indx = rand_Id
    card = wild_cards[mapped_indx]

  # ID for Action-Colour card
  elif wild_size <= rand_Id < wild_size + actColour_size:
    # Get the index of the mapped set from the random Id generated
    mapped_indx = rand_Id - wild_size
    card = randId(action, colour, mapped_indx)
  
  # ID for Number-Colour card
  elif wild_size + actColour_size <= rand_Id < TotalUnique_cards:
    # Get the index of the mapped set from the random Id generated
    mapped_indx = rand_Id - (wild_size + actColour_size)
    card = randId(number, colour, mapped_indx)

  return mapped_indx, card

def drawCards (draw_num = NUM_cardsDrawn):
  used_Id = []
  cards_drawn = []

  for _ in range(draw_num):
    drawn_card = draw(used_Id)
    used_Id.append(drawn_card[0])
    cards_drawn.append(drawn_card[-1])
  
  return cards_drawn, used_Id

# Characteristics of cards
run_test = True
if __name__ == '__main__' and run_test:
  
  def generatePlayers_draw ():

    file_path = '/home/wtc/Documents/hello-friend/Uno_Game/Docs/swear.txt'
    profanities = write_toArray(file_path)
    count = 1
    exit_flag = 'exit'
    break_flag = 'done'

    key_inputs = {
      'break_flag' :break_flag,
      'exit_flage' :exit_flag,
      'data_type' : str,
      'invalid_input' : profanities
    }

    players = {}
    Net_ID_Used = []

    while True:
      message = f'Player {count} Please enter name, type {break_flag.upper()} to finish or {exit_flag.upper()} to quit game : '
      name_input = input(message)
      name_input = name_input.lower()
      name_input, is_valid = validateInput(name_input, **key_inputs)
      if name_input == break_flag: break
      if name_input == exit_flag: exit()
      if is_valid:
        if name_input not in players.keys():
          count = count + 1
          cards_drawn, Net_ID_Used = drawCards()
          players[name_input] = [cards_drawn]
          Net_ID_Used.extend(Net_ID_Used)
        else: 
          suggested_name = AppendInput(name_input)
          print(f'ERROR!, Name {name_input} already taken, try name {suggested_name}')
      
    return players, Net_ID_Used
         
  players, IDS_used = generatePlayers_draw()
  print(f'Players are {players} and ID generated is {IDS_used}')
  
  # endregion