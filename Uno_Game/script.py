import tkinter

root = tkinter.Tk()
root.title("Name Entry")

entry = tkinter.Entry(root,width = 60)
entry.pack(pady = 70)
user_input = entry.get()

root.mainloop()