import tkinter
import numpy as np

player = {'dave': [(1, 'white'), (0, 'red'), (2, 'blue'), (9, 'white')], 'susan': [(3, 'blue'), (0, 'blue'), (6, 'red'), ('act_3', 'blue')], 'mike': [(7, 'yellow'), (0, 'red'), (0, 'white'), (3, 'blue')]}

def sourceFunction (name):
  cards = player[name]
  print(f'Card')
  