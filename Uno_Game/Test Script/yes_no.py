import tkinter as tk
from tkinter import messagebox

def on_enter(event):
    # This function will handle the Enter key press
    answer = messagebox.askyesno('VALIDATION', f'Were you trying to type {close_match[0]}')
    if answer:  # If user clicked "Yes"
        user_input = close_match[0]
        print(f"User input set to: {user_input}")
    # No need to handle 'No' here, as nothing will be set

# Create a sample list to simulate close matches
close_match = ['example_text']

# Set up the main application window
root = tk.Tk()
root.title("Example App")

# Bind the Enter key to the on_enter function
root.bind('<Return>', on_enter)

# Create a button to simulate an action
button = tk.Button(root, text="Press Enter or Click Me", command=lambda: on_enter(None))
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

