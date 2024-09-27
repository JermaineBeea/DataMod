import tkinter
from GameModules.GeneratePlayers import centerWidget
from GameModules.DrawCard import players_cards
from Modules.DisplayCard import displayCards
from functools import partial

# region smaple players for testing
# players_cards = {
# 'dave': [(8, 'grey'), (5, 'darkred'), ['W_2', 'black'], (5, 'darkred'), (5, 'grey'), (8, 'grey'), (7, 'darkblue')], 
# 'susan': [(1, 'darkred'), (1, 'darkblue'), ['W_3', 'black'], (3, 'grey'), (4, 'grey'), ['W_1', 'black'], ('act_1', 'darkblue')], 
# 'mat': [(7, 'darkorange'), (4, 'darkblue'), ('act_1', 'darkorange'), ('act_1', 'grey'), (2, 'darkred'), (6, 'darkblue'), (6, 'grey')], 
# 'pat': [(1, 'darkred'), (7, 'darkblue'), (9, 'darkred'), (6, 'darkblue'), (9, 'darkred'), (2, 'grey'), (9, 'darkorange')], 
# 'pete': [['W_1', 'black'], (5, 'darkred'), (5, 'darkred'), (2, 'darkorange'), (5, 'darkblue'), (2, 'grey'), (9, 'grey')], 
# 'dude': [(6, 'darkorange'), (8, 'darkblue'), (4, 'darkorange'), (7, 'darkblue'), (8, 'darkorange'), (3, 'darkred'), (5, 'darkred')]
# }
# endregion

def RunPlayerTurn():
  # Player cards is fetched from DrawCard Module
  def sourceFunction(cards_):
      displayCards(cards_)

  button_width = 20  
  button_height = 4  
  button_colour = 'darkred'
  text_colour = 'white'

  root_height = 400
  root_width = 200
  x_shit = - 600
  y_shift = - 200

  root = tkinter.Tk()
  root.title('CHOOSE A PLAYER TO GO NEXT')
  root.config(bg = 'darkgrey')

  centerWidget(root, root_width, root_height, x_shit, y_shift)

  for player_name, cards_drawn in players_cards.items():
      func = partial(sourceFunction, cards_drawn)
      button = tkinter.Button(root, command=func, text=f'{player_name.upper()} \n Display \nCards', font = ('Consolas', 14), bg = button_colour, fg = text_colour)
      button.config(width=button_width, height=button_height)
      button.pack(fill= 'both',  expand= True) 

  root.mainloop()
