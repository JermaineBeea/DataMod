import tkinter


root = tkinter.Tk()

frame = tkinter.Frame(root, bg = 'red')
frame.pack(pady = 10)

label = tkinter.Label(frame, text= 'Lable')
label.pack(pady = 10)

root.mainloop()