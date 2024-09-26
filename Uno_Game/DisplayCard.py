import tkinter
from Modules.GeneratePlayers import centerWidget
def displayCards (cards):
  """" 
  Function to display cards 
  """
  root_width = 500
  root_height = 600
  x_shit = + 200
  y_shift = - 200
  root = tkinter.Tk()
  frame_back_colour = 'darkgrey'
 #root.geometry(f'{root_width}x{root_height}')
  centerWidget(root,root_width, root_height, x_shit, y_shift)

  for n,card in enumerate(cards):
    card_colour = card[1]
    card_text = card[0]

    frame = tkinter.Frame(root, bg = frame_back_colour, width = 100, height = 150, highlightbackground='black', highlightthickness=2, bd=1)
    frame.pack_propagate(False)

    card_button = tkinter.Button(frame, text= f'{card_text}', bg = card_colour, fg = 'white', font=('Arial', 24))
    card_button.pack(fill = 'both', expand = True)

    frame.grid(row=n//3, column=n%3, padx=10, pady=10)

  root.mainloop()

