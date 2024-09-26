import tkinter
from functools import partial
from Modules.GeneratePlayers import centerWidget

def button1(n=1):
    print(n)

# Root Parameters
root_width = 300
root_height = 300
h_shift = 0
v_shift = -100

# Root Main
root = tkinter.Tk()
root.title('Player Card')
centerWidget(root, root_width, root_height, h_shift, v_shift)

# Create buttons and assign them correct commands with partial
buttons = []
for i in range(3):
    button_command = partial(button1, n=i+1)  # Pass button number as n
    button = tkinter.Button(root, text=f'Button {i+1}', command=button_command)
    buttons.append(button)

# Place buttons in the GUI
for button in buttons:
    button.pack(pady=30)

root.mainloop()
