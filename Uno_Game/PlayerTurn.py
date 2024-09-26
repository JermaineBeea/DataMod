import tkinter
import numpy as np
from Modules.GeneratePlayers import centerWidget
from Modules.DrawCard import players_cards
from functools import partial

player_cards = {'dave': [(1, 'blue'), (9, 'blue'), (0, 'blue'), (7, 'blue'), (8, 'white'), (5, 'yellow'), ('act_2', 'white')], 
                'smith': [(0, 'blue'), (5, 'white'), (0, 'white'), ('act_2', 'red'), (0, 'red'), (8, 'blue'), ('act_2', 'blue')], 
                'peter': [(2, 'white'), ('act_2', 'blue'), (5, 'white'), (6, 'white'), (9, 'yellow'), ('act_3', 'white'), (1, 'blue')], 
                'david': [(2, 'blue'), (0, 'blue'), ('act_2', 'white'), ('act_1', 'yellow'), (2, 'blue'), ('act_3', 'white'), ('act_3', 'red')], 
                'peter%3': [['W_3', 'brown'], (9, 'white'), (4, 'white'), (4, 'blue'), ['W_1', 'brown'], (7, 'blue'), (1, 'blue')], 
                'king': [(5, 'blue'), (7, 'white'), (0, 'yellow'), (7, 'yellow'), (8, 'red'), (6, 'red'), ['W_1', 'brown']], 
                'kong': [('act_3', 'white'), (0, 'yellow'), ['W_1', 'brown'], (0, 'white'), ['W_2', 'brown'], ('act_1', 'yellow'), (1, 'red')], 'rad': [(3, 'red'), (0, 'white'), ['W_1', 'brown'], (8, 'red'), (8, 'red'), (0, 'red'), ('act_2', 'white')]}

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
x_shit = -200
y_shift = -100

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
