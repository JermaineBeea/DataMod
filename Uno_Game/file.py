import tkinter

cards = [(9, 'white'), (1, 'white'), ['W_2', 'brown'], ('act_1', 'white'), (1, 'white'), (3, 'white'), ('act_2', 'white')]

root = tkinter.Tk()
root.geometry('400x400')

# FRAME 1
# Adding black border with highlightthickness and bd
frame_back_colour = 'darkgrey'
frame = tkinter.Frame(root, bg = frame_back_colour, width=200, height=100, highlightbackground='black', highlightthickness=2, bd=2)
frame.pack_propagate(False)

label = tkinter.Label(frame, text= f'1', bg = 'red', font=('Arial', 24))
label.pack(fill = 'both', expand = True)

frame.grid(row= 2, column=3, padx=10, pady=10)

# FRAME 2
# Adding black border with highlightthickness and bd
frame_back_colour = 'darkgrey'
frame2 = tkinter.Frame(root, bg = frame_back_colour, width=200, height=100, highlightbackground='black', highlightthickness=2, bd=2)
frame2.pack_propagate(False)

label = tkinter.Label(frame2, text= f'2', bg = 'red', font=('Arial', 24))
label_2.pack(fill = 'both', expand = True)

frame2.grid(row= 3, column=2, padx=10, pady=10)


root.mainloop()
