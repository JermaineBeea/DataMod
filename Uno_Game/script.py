import tkinter
import numpy as np
from Modules.GeneratePlayers import centerWidget
from functools import partial

player = {'dave': [(1, 'white'), (0, 'red'), (2, 'blue'), (9, 'white')], 'susan': [(3, 'blue'), (0, 'blue'), (6, 'red'), ('act_3', 'blue')], 'mike': [(7, 'yellow'), (0, 'red'), (0, 'white'), (3, 'blue')]}

def sourceFunction (name):
  cards = player[name]
  print(f'Cards for player {name} \nare {cards}')


# Root Main config variables
root_width = 300
root = tkinter.Tk()
root.title('Players')
root.config(bg = 'darkgrey')
centerWidget(root, )

for player_name, cards in player.items():

    func = partial(sourceFunction, name = player_name)
    button = tkinter.Button(root, command = func, text = f'Player {player_name} Cards', font = ('Consolas', 14), bg = 'darkred', fg = 'white')
    button.config(width = 15, height= 5)
    button.pack(pady = 30)

root.mainloop()
  