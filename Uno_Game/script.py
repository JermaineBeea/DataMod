
import tkinter

from Modules.GeneratePlayers import centerWidget

def button1 (n = 1):
  print(n)

button2 = button1(n = 2)
button3 = button1(n = 3)

buttons = button1, button2, button3
 
lst = (8, 'red'), (6, 'yellow'), (8, 'blue'), (2, 'yellow')

# Root Paraemeters
root_width = 300
root_height = 300
h_shift = 0
v_shift = -100

for num, button in enumerate(buttons):
  # Root Main
  root = tkinter.Tk()
  root.title('Player Card')
  centerWidget(root, root_width, root_height, h_shift, v_shift)

  button = tkinter.Button(root, text = f'Button {num}', command = button)
  button.pack(pady = 30)

  root.mainloop()
