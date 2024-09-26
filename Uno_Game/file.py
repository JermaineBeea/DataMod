import tkinter

cards = [(9, 'white'), (1, 'white'), ['W_2', 'brown'], ('act_1', 'white'), (1, 'white'), (3, 'white'), ('act_2', 'white')]

root = tkinter.Tk()
root.geometry('400x550')


frame_back_colour = 'darkgrey'
for n,card in enumerate(cards):
  card_colour = card[1]
  card_text = card[0]

  frame = tkinter.Frame(root, bg = frame_back_colour, width = 100, height = 150, highlightbackground='black', highlightthickness=2, bd=2)
  frame.pack_propagate(False)

  card_button = tkinter.Button(frame, text= f'{card_text}', bg = card_colour, font=('Arial', 24))
  card_button.pack(fill = 'both', expand = True)

  frame.grid(row=n//3, column=n%3, padx=10, pady=10)

root.mainloop()
