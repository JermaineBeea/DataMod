import tkinter


cards = [(9, 'white'), (1, 'white'), ['W_2', 'brown'], ('act_1', 'white'), (1, 'white'), (3, 'white'), ('act_2', 'white')]

root = tkinter.Tk()
root.geometry('300x300')

for card in cards:
  frame_colour = card[1].lower()
  frame = tkinter.Frame(root, bg = frame_colour, width=200, height=100)
  frame.pack(fill = 'both', expand= True, pady=10)

  frame_text = str(card[0])
  label = tkinter.Label(frame, text = frame_text, bg = frame_colour, font = ('Arial', 24))
  label.pack(pd = 10)

root.mainloop()
