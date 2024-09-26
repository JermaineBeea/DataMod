import tkinter
from Modules.GeneratePlayers import centerWidget

# Initialize current_root globally to track the current window
current_root = None

def displayCards(cards):
    global current_root
    
    # Destroy the previous root window if it exists
    if current_root is not None:
        current_root.destroy()
    
    root_width = 500
    root_height = 600
    x_shift = 200
    y_shift = -200
    
    # Create a new root window
    root = tkinter.Tk()
    frame_back_colour = 'darkgrey'
    
    # Center the new window
    centerWidget(root, root_width, root_height, x_shift, y_shift)
    
    # Create and display frames for cards
    for n, card in enumerate(cards):
        card_colour = card[1]
        card_text = card[0]
        
        frame = tkinter.Frame(root, bg=frame_back_colour, width=100, height=150, 
                              highlightbackground='black', highlightthickness=2, bd=1)
        frame.pack_propagate(False)

        card_button = tkinter.Button(frame, text=f'{card_text}', bg=card_colour, 
                                     fg='white', font=('Arial', 24))
        card_button.pack(fill='both', expand=True)

        frame.grid(row=n//3, column=n%3, padx=10, pady=10)
    
    # Update current_root to the new root window
    current_root = root
    
    root.mainloop()
