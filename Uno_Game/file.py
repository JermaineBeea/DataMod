import tkinter

cards = [('act_3', 'grey'), (0, 'yellow'), ['W_1', 'darkgrey'], (0, 'grey'), ['W_2', 'darkgrey'], ('act_1', 'yellow'), (1, 'red')]

def displayCards ():
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

displayCards()