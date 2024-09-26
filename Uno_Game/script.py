import tkinter
import numpy as np
from Modules.GeneratePlayers import centerWidget  # Ensure this module is correctly imported
from functools import partial

# Player data
players = {
    'dave': [(1, 'white'), (0, 'red'), (2, 'blue'), (9, 'white')],
    'susan': [(3, 'blue'), (0, 'blue'), (6, 'red'), ('act_3', 'blue')],
    'mike': [(7, 'yellow'), (0, 'red'), (0, 'white'), (3, 'blue')],
    'kyle': [(7, 'yellow'), (0, 'red'), (0, 'white'), (3, 'blue')],
    'Danielle': [(7, 'yellow'), (0, 'red'), (0, 'white'), (3, 'blue')]
}

def sourceFunction(name):
    cards = players[name]
    print(f'Cards for player {name} \nare {cards}')

num_players = len(players)

# Global Button configuration variables
button_width = 20  
button_height = 2  

# Root dimensions based on the number of players and button dimensions
metric = ...
root_height = metric*num_players*button_height  
root_width = button_width * 10  

# Initialize the root window
root = tkinter.Tk()
root.title('Players')
root.config(bg='darkgrey')

# Center the window
centerWidget(root, root_width, root_height)

# Create and pack buttons for each player
for player_name in players.keys():
    func = partial(sourceFunction, name=player_name)
    button = tkinter.Button(root, command=func, text=f'{player_name} \nCards', font = ('Consolas', 14), bg = 'darkred', fg='white')
    button.config(width=button_width, height=button_height)
    button.pack(pady = 0) 

# Start the main loop
root.mainloop()
