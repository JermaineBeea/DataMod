import tkinter as tk
from tkinter import messagebox

# Function to handle button click
# def submit_input():
#     user_input = entry.get()  # Get input from entry widget
#     if user_input:
#         messagebox.showinfo("Input Received", f"You entered: {user_input}")
#     else:
#         messagebox.showwarning("Empty Input", "Please enter something!")


run_exmaple = False
if run_exmaple:
# Create the main window
  root = tk.Tk()
  root.title("Simple Input GUI")

  # Add a label
  label = tk.Label(root, text="Enter something:")
  label.pack(pady= 50)

  # Add an entry widget for user input
  entry = tk.Entry(root, width = 50)
  entry.pack(pady= 30)

  # Add a submit button
  submit_button = tk.Button(root, text="Submit", command= 'SUBMIT INPUT')
  submit_button.pack(pady= 30)

  # Start the Tkinter event loop
  root.mainloop()

root = tk.Tk()
root.title('This is a test GUI')

entry = tk.Entry(root, width = 60)
entry.pack(pady = 70)
user_input = entry.get()
messagebox.showinfo(f'Did you type {user_input}')
button = tk.Button(root, text = 'Type your NAME', command = 'Type below')
button.pack(pady = 70)

root.mainloop()