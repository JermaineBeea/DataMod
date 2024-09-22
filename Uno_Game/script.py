import tkinter

run_test= True
if run_test:
  
  global l_1
  l_1 = []
  
  root = tkinter.Tk()
  root.title("Name Entry")

  entry = tkinter.Entry(root, width = 60)
  entry.pack(pady = 70)

  def submit ():
    l_1.append(entry.get())
  tkinter.Button(root, text = "Submit", command = submit).pack(pady = 70)

  root.mainloop()
  print(l_1)
  
else:

  # Initialize the main window
  root = tkinter.Tk()
  root.title("Name Entry")

  # Create an entry widget with a specified width
  entry = tkinter.Entry(root, width=60)
  entry.pack(pady=70)

  # Define a function to get the user input when called
  def get_user_input():
      user_input = entry.get()
      print(f"User Input: {user_input}")  # Print the user input or handle it as needed

  # Create a button to trigger the get_user_input function
  submit_button = tkinter.Button(root, text="Submit", command=get_user_input)
  submit_button.pack(pady=20)

  # Start the main loop to keep the window open and interactive
  root.mainloop()

