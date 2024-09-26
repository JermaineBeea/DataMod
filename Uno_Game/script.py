import tkinter
import numpy as np
#from Modules.GeneratePlayers import centerWidget
from functools import partial

players = {'dave': [(1, 'white'), (0, 'red'), (2, 'blue'), (9, 'white')], 'susan': [(3, 'blue'), (0, 'blue'), (6, 'red'), ('act_3', 'blue')], 'mike': [(7, 'yellow'), (0, 'red'), (0, 'white'), (3, 'blue')]}

def sourceFunction (name):
  cards = players[name]
  print(f'Cards for player {name} \nare {cards}')

num_players = len(players)

# Global Button configuration variables
button_width = 15
button_height = 5

# Root Main config variables
root_height = (button_height + 20)*num_players
root_width = 2*button_width
x_shift = 0
y_shift = -100

root = tkinter.Tk()
root.title('Players')
root.config(bg = 'darkgrey')
#centerWidget(root, root_width, root_height, x_shift, y_shift )

for player_name, cards in players.items():

    func = partial(sourceFunction, name = player_name)
    button = tkinter.Button(root, command = func, text = f'Player {player_name} Cards', font = ('Consolas', 14), bg = 'darkred', fg = 'white')
    # button.config(width = button_width, height= button_height)
    button.pack(pady = 30)

root.mainloop()
  