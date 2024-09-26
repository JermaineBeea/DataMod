import tkinter
import numpy as np
from Modules.GeneratePlayers import centerWidget  # Ensure this module is correctly imported
from functools import partial

# Player data
players = {
    'dave': [(1, 'white'), (0, 'red'), (2, 'blue'), (9, 'white')],
    'susan': [(3, 'blue'), (0, 'blue'), (6, 'red'), ('act_3', 'blue')],
    'mike': [(7, 'yellow'), (0, 'red'), (0, 'white'), (3, 'blue')]
}

def sourceFunction(name):
    cards = players[name]
    print(f'Cards for player {name} \nare {cards}')

num_players = len(players)

# Global Button configuration variables
button_width = 5
button_height = 5

# Root dimensions based on the number of players and button dimensions
root_height = (button_height + 1) * num_players  # Adjust height for spacing
root_width = button_width * 100   # Add extra space for aesthetics

# Centering offsets
x_shift = 0
y_shift = -100

# Initialize the root window
root = tkinter.Tk()
root.title('Players')
root.config(bg ='darkgrey')
centerWidget(root, root_width, root_height, x_shift, y_shift)


for player_name in players.keys():
    func = partial(sourceFunction, name=player_name)
    button = tkinter.Button(root, command=func, text=f'{player_name} \nCards', font =( 'Consolas', 14), bg = 'darkred', fg = 'white')
    button.config(width=button_width, height=button_height)
    button.pack(pady=10)  

root.mainloop()
