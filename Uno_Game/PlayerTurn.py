import tkinter
import numpy as np
from Modules.GeneratePlayers import centerWidget
# from Modules.DrawCard import players_cards
from functools import partial

players_cards = {'david': [('act_2', 'grey'), ('act_2', 'darkblue'), (6, 'grey'), ('act_1', 'darkred'), ('act_3', 'darkorange'), ('act_2', 'grey'), (5, 'grey')], 
 'susan': [('act_3', 'darkred'), (4, 'darkblue'), ('act_1', 'darkblue'), ('act_3', 'darkorange'), ('act_2', 'darkorange'), (2, 'darkblue'), (7, 'grey')]} 


# Player cards is fetched from DrawCard Module
def sourceFunction(name):
    cards = players_cards[name]
    print(f'Cards for player {name} \nare {cards}')

# Global Button configuration variables
button_width = 20  
button_height = 2  
button_colour = 'darkred'
text_colour = 'white'

# Root dimensions based on the number of players and button dimensions
root_height = 400
root_width = 200
x_shit = - 600
y_shift = - 200

# Initialize the root window
root = tkinter.Tk()
root.title('CHOOSE A PLAYER TO GO NEXT')
root.config(bg='darkgrey')

# Center the window
centerWidget(root, root_width, root_height, x_shit, y_shift)

# Create and pack buttons for each player
for player_name in players_cards.keys():
    func = partial(sourceFunction, name=player_name)
    button = tkinter.Button(root, command=func, text=f'{player_name.upper()} \n Display Cards', font = ('Consolas', 14), bg = button_colour, fg = text_colour)
    button.config(width=button_width, height=button_height)
    button.pack(fill= 'both',  expand= True) 

# Start the main loop
root.mainloop()
