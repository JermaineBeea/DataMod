
import tkinter

from Modules.GeneratePlayers import centerWidget

def buttonAction (num):
  if num == 1: print('Button 1')
  if num == 2: print('Button 2')
  if num == 3: print('Button 3')


lst = (8, 'red'), (6, 'yellow'), (8, 'blue'), (2, 'yellow')

# Root Paraemeters
root_width = 300
root_height = 300
h_shift = 0
v_shift = -100

# Root Main
root = tkinter.Tk()
root.title('Player Card')
centerWidget(root, root_width, root_height, h_shift, v_shift)

buttons = {}
for n, item in enumerate(lst):
  button = tkinter.Button(root, text = f'Button {n}' ,command = buttonAction(n))
  button.pack(pady = 30)

root.mainloop()
