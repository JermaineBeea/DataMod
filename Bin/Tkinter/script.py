import tkinter as tk

# Sample data
data = {
    'dave': [(0, 'blue'), (1, 'red'), (1, 'blue'), (2, 'red')],
    'mat': [(6, 'yellow'), (2, 'white'), (6, 'blue'), (0, 'yellow')]
}

# Create the main window
root = tk.Tk()
root.title("Card Representation")

# Function to display player cards
def display_cards(data):
    for player, cards in data.items():
        # Create a string for the player's cards
        card_info = f"{player}\n"
        for index, (num, color) in enumerate(cards):
            card_info += f"Card {index + 1}: {num}, {color}\n"
        
        # Create a label for each player
        label = tk.Label(root, text=card_info, justify=tk.LEFT)
        label.pack(anchor='w', padx=10, pady=5)

# Display the cards
display_cards(data)

# Start the Tkinter main loop
root.mainloop()
