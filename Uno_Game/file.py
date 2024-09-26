import difflib
import tkinter

from tkinter import messagebox

def centerWidget (widget_root, root_width, root_height):
    screen_width = widget_root.winfo_screenwidth()
    screen_height = widget_root.winfo_screenheight()
	
    x = (screen_width // 2) - (root_width // 2)
    y = (screen_height // 2) - (root_height // 2)
	
    widget_root.geometry(f"{root_width}x{root_height} + {x} + {y}")

def librKeyMatch (word, libr):
    key_match = []
    first_match = []
    for key, val in libr.items():
      first_match = difflib.get_close_matches(word, val, cutoff = 0.4, n = 1)
      if first_match: key_match = key; first_match = first_match[0]; return first_match, key_match

def rgbHex (r, g, b):
    return f'#{r:02x}{b:02x}{b:02x}'

def parseInput (event = None):
    
    user_input = entry_tab.get()
    
    if flag_libr['data']:print(f'DATAFLAG ACTIVE')
    if user_input: 
       word_match, flag_name = librKeyMatch(user_input, flag_libr)
       if word_match: 
          bool_flag = user_input == word_match
       	  if flag_name == 'invalid': messagebox.showerror('PROFANE WORD', f'Profane word "{word_match.upper()}" not permitted in name')
          if not bool_flag: messagebox.askyesno('VALIDATION', f'Did you imply to type {word_match}')
       else: player_names[user_input] = []
    else: messagebox.showerror('ERROR', 'Void Entry: try again')

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
root_bg = 'grey'
root_width = 350
root_height = 350
label_x = 0.5
label_y = 0.5

event_root = tkinter.Tk()
#centerWidget(event_root, root_width, root_height)
event_root.geometry(f'{root_width}x{root_height}')
event_root.title('USER INPUT')
event_root.config(bg = root_bg)

entry_label = tkinter.Label(event_root, text = 'Enter name below', font = ('Arial', 20), fg = 'white', bg = root_bg)
entry_label.place(relx = label_x, rely = label_y, anchor = 'center')

entry_tab = tkinter.Entry(event_root, width = 30)
entry_tab.place(relx = label_x, rely = label_x + 0.2, anchor = 'center')

submit_button = tkinter.Button(event_root, command = parseInput, text = 'Submit',  font = ('Arial', 15), bg = 'darkgrey', fg = 'white')
submit_button.place(relx = label_x , rely = label_y + 0.4, anchor = 'center')

event_root.mainloop()

