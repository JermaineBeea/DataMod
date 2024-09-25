import numpy as np
import random

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
Num_unique_cards = colourNum_size + actColour_size + wild_size

def Prob_a (): return wild_size/Num_unique_cards
def Prob_b (): return actColour_size/Num_unique_cards
def Prob_c (): return colourNum_size/Num_unique_cards

prob_functions = [Prob_a, Prob_b, Prob_c]
prob_val = [func() for func in prob_functions ]
prob_val.sort()

for n, func_val in enumerate(prob_val):
  rand_float = np.random.random()
  
