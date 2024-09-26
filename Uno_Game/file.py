import tkinter as tk


cards = [(9, 'white'), (1, 'white'), ['W_2', 'brown'], ('act_1', 'white'), (1, 'white'), (3, 'white'), ('act_2', 'white')]

root = tk.Tk()
root.geometry('300x300')

for card in cards:
  colour = card[1].lower()
  frame = tk.Frame(root, bg= colour, width=200, height=100)
  frame.pack(fill = 'both', expand= True, pady=10)



root.mainloop()
