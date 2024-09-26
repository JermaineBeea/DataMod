import tkinter

cards = [(9, 'white'), (1, 'white'), ['W_2', 'brown'], ('act_1', 'white'), (1, 'white'), (3, 'white'), ('act_2', 'white')]

root = tkinter.Tk()
root.geometry('300x300')
 
# Adding black border with highlightthickness and bd
frame_back_colour = 'darkgrey'
frame = tkinter.Frame(root, bg = frame_back_colour, width=200, height=100, 
highlightbackground='black', highlightthickness=2, bd=2)
frame.pack(fill='both', expand=True, pady=10)

label = tkinter.Label(frame, text= 'Frame label', bg= 'blue', font=('Arial', 24))
label.pack(pady=10)

root.mainloop()
