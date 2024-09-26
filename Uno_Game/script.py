import tkinter
import numpy as np

from functools import partial

player = {'dave': [(1, 'white'), (0, 'red'), (2, 'blue'), (9, 'white')], 'susan': [(3, 'blue'), (0, 'blue'), (6, 'red'), ('act_3', 'blue')], 'mike': [(7, 'yellow'), (0, 'red'), (0, 'white'), (3, 'blue')]}

def sourceFunction (name):
  cards = player[name]
  print(f'Cards for player {name} \nare {cards}')


root = tkinter.Tk()
root.title('Players')

for player_name, cards in player.items():

    func = partial(sourceFunction, name = player_name)
    button = tkinter.Button(root, command = func, text = f'Player {player_name}', font = ('Consolas', 14))
    button.geomet
    button.pack(pady = 10)

root.mainloop()
  