import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("Card Game Example")
root.geometry("400x500")

# Define your card deck: a list of lists with card number and color
cards = [
    [1, 'red'],
    [2, 'yellow'],
    [3, 'orange'],
    [4, 'blue'],
    [5, 'green'],
    [6, 'grey']
]

# Function to create a card widget
def create_card(frame, card_number, card_color):
    # Create a card frame with background color
    card = tk.Frame(frame, bg=card_color, width=100, height=150, highlightbackground="black", highlightthickness=2)
    card.pack_propagate(False)  # Prevent the frame from resizing to fit the content
    
    # Add the card number label inside the card frame
    card_label = tk.Label(card, text=str(card_number), font=("Arial", 24), bg=card_color, fg="white")
    card_label.pack(fill = 'both', expand=True)  # Center the label in the frame

    return card

# Create a frame to hold the cards
card_frame = tk.Frame(root)
card_frame.pack(pady=20)

# Display cards in a grid layout
for i, card in enumerate(cards):
    card_number, card_color = card
    card_widget = create_card(card_frame, card_number, card_color)
    card_widget.grid(row=i//3, column=i%3, padx=10, pady=10)  # Adjust grid placement

# Start the Tkinter event loop
root.mainloop()

