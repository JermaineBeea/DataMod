import difflib
import tkinter

from tkinter import messagebox

def centerWidget (widget_root, root_width, root_height):
  screen_width = widget_root.winfo_screenwidth()
  screen_height = widget_root.winfo_screenheight()
  x = (screen_width // 2) - (root_width // 2)
  y = (screen_height // 2) - (root_height // 2)
  widget_root.geometry(f"{root_width}x{root_height} + {x} + {y}")

def rgbHex (r, g, b):
  return f'#{r:02x}{b:02x}{b:02x}'


def librKeyMatch (user_input, libr):
  return_match = ''
  return_name = ''
  #Instance variable to check the instances of a close match
  instance = False
  for name_list, list_elements in libr.items():
    close_match = difflib.get_close_matches(user_input, list_elements, cutoff = 0.4, n = 1)
    # We only intereted in the first instance of a close match assuming its not invalid
    if close_match and name_list != 'invalid' and instance is False:
      instance = True
      return_match = close_match[0]
      return_name = name_list
    # If user input is invalid then return the invalid match
    elif close_match and name_list == 'invalid': 
      return close_match, name_list

  return return_match, return_name


def parseInput (event = None):    
  user_input = entry_tab.get()
  if user_input: 
    # Data Type validation
    is_valid_dtype = True
    valid_dtype = flag_libr.get('data', None)
    if valid_dtype is not None :
      # Library copy to pe passed as an argument to librKeyMatch function, without data as parameter
      libr_copy = flag_libr.copy()
      libr_copy.pop('data')
      # Check to see if data type of user input is correct
      if not isinstance(user_input, tuple(valid_dtype)) :
        messagebox.showerror('INVALID DATA TYPE', f'Please ensure input is of {str(valid_dtype).upper()}')
        is_valid_dtype = False
    # User input validation
    user_input_match, flag_name = librKeyMatch(user_input, libr_copy)
    if user_input_match: 
      # Check if user input does not equal close match, as prompt only applies for partial match
      bool_flag = user_input == user_input_match
      if flag_name == 'invalid': messagebox.showerror('PROFANE user_input', f'Profane user_input "{user_input_match[0].upper()}" not permitted in name')
      elif not bool_flag: messagebox.askyesno('VALIDATION', f'Did you imply to type {user_input_match}')
    elif is_valid_dtype: player_names[user_input] = []
  else: messagebox.showerror('ERROR', 'Void Entry: try again')

  entry_tab.delete(0, 'end')

def cancel (event = None):
  widget_root.destroy()

flag_libr = {
	'invalid': ['fuck', 'shit', 'cunt'],
  'valid': ['mat', 'susan', 'david'],
	'data': [str],
	'break_flag': ['done'],
	'exit_flag': ['cancel', 'exit']
}

player_names = {}

# Event root for User Input GUI
# Parameters for anchor :  must be n, ne, e, se, s, sw, w, nw, or center

# Widget configuration parameters
widget_colour = 'grey'
root_width = 350
root_height = 350
label_x = 0.5
label_y = 0.5

widget_root = tkinter.Tk()
#centerWidget(widget_root, root_width, root_height)
widget_root.geometry(f'{root_width}x{root_height}')
widget_root.title('USER INPUT')
widget_root.config(bg = widget_colour)

entry_label = tkinter.Label(widget_root, text = 'Enter name below', font = ('Arial', 20), fg = 'white', bg = widget_colour)
entry_label.place(relx = label_x, rely = label_y, anchor = 'center')

entry_tab = tkinter.Entry(widget_root, width = 30)
entry_tab.place(relx = label_x, rely = label_x + 0.2, anchor = 'center')

submit_button = tkinter.Button(widget_root, command = parseInput, text = 'Submit',  font = ('Arial', 15), bg = 'darkgrey', fg = 'white')
submit_button.place(relx = label_x , rely = label_y + 0.4, anchor = 'center')

cancel_button = tkinter.Button(widget_root, command = cancel, text = 'Cancel', font= ('Arial', 20), bg = 'darkgrey',  fg = 'white')

widget_root.bind('<Return>', parseInput)
widget_root.bind('<Escape>', cancel)

widget_root.mainloop()

