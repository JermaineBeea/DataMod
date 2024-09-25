import difflib
import tkinter
import random
import numpy as np

from tkinter import messagebox

def flagFilter(user_input, flag_copy):
    # Copy of flag library to be used in flagFilter
    return_match = ''
    return_name = ''
    instance = False
    for flag_name, flag_elements in flag_copy.items():
      flag_match = difflib.get_close_matches(user_input, flag_elements, cutoff=0.7, n=1)
      if flag_match and flag_name == 'invalid':
        return flag_match, flag_name
      elif flag_match and not instance:
        instance = True
        return_match = flag_match
        return_name = flag_name
    return return_match, return_name

def checkDuplicate(user_input, list):
    characters = ['@', '$', '&']
    if user_input in list:
      appended = user_input
      while appended in list:
        rand_num = np.random.randint(1, 10, size = 2).astype(str)
        rand_char = random.choice(characters)
        str_num = ''.join(rand_num)
        appended = ''.join((user_input, rand_char, str_num))
      answer = messagebox.askyesno('NAME USED', f'{user_input.upper()} already used, do you want to try {appended}?')
      if answer:
        if answer == 'yes': 
          print(f'APPENDED IS {appended}')
          user_input = appended
          return user_input
      else: 
        messagebox.showerror('VOID ENTRY',f'User did not select "YES" or "NO", attempt terminated')
    else: 
      return user_input

# Functions for Widget Buttons
def parseInput(event = None):
  # Copy of flag library to be used in flagFilter
  flag_copy = flag_libr.copy()
  user_input = input_tab.get()

  if user_input:
      user_input = user_input.strip()
      user_input.lower()
      user_input = checkDuplicate(user_input, list(player_names.keys()))
      print(f'DATA TYPE IS {type(user_input)}')
      # Data Type validation for user input
      dtype_is_valid = True
      flag_dtype = flag_libr.get('data', None)

      if flag_dtype is not None:
        flag_copy.pop('data')
        if not isinstance(user_input, tuple(flag_dtype)):
          dtype_is_valid = False

      if dtype_is_valid:
        close_match, name_flag = flagFilter(user_input, flag_copy)
        if close_match:
          bool_flag = user_input == close_match[0]
          if name_flag == 'invalid':
            messagebox.showwarning('INVALID ENTRY', f'Please ensure input does not contain {close_match[0].upper()}')
          # Prompt for close match only valid if user input not exactly equal to match
          elif bool_flag:
            player_names[user_input] = []
          elif not bool_flag:
              answer = messagebox.askyesno('VALIDATION', f'Were you trying to type {close_match[0]}')
              if answer == 'yes':
                user_input = close_match[0]
              else:
                player_names[user_input] = []
        else:
          player_names[user_input] = []
      else:
        messagebox.showerror('INVALID DATA TYPE', f'Please ensure input is of data type {flag_dtype}')
  else:
    messagebox.showerror('VOID ENTRY ERROR', 'Void input invalid')

  input_tab.delete(0, 'end')

def cancel(event = None):
  widget_root.destroy()
# end region 

def centerWidget(widget_root, root_width, root_height, hoizontal_shift, vertical_shift):
  screen_width = widget_root.winfo_screenwidth()
  screen_height = widget_root.winfo_screenheight()
  x = (screen_width // 2) - (root_width // 2) + hoizontal_shift
  y = (screen_height // 2) - (root_height // 2) + vertical_shift
  widget_root.geometry(f"{root_width}x{root_height}+{x}+{y}")

def change_xy(x_change=0, y_change=0):
  global x_0, y_0  # Declare as global to modify outside this function
  x_0 += x_change
  y_0 += y_change
  cord_libr = {'relx': x_0, 'rely': y_0, 'anchor': 'center'}
  return cord_libr


flag_libr = {
  #"valid": ['david','susan','mathew'],
  'invalid': ['#', 'fuck', 'shit', 'crap', 'bitch', ],
  'data': [str],
}

player_names = {}

# Widget root

# Parameters
widget_colour = 'grey'
widget_width = 400
widget_height = 400
global_font = ('Arial', 16)
#shift vertical and horizontal from center
v_shift = -100
h_shift = 0

widget_root = tkinter.Tk()
widget_root.title('USER INPUT')
widget_root.config(bg=widget_colour)
centerWidget(widget_root, widget_width, widget_height, h_shift, v_shift)

entry_label = tkinter.Label(widget_root, text='Enter Name below', font=global_font, bg='black', fg='white')
x_0 = 0.5
y_0 = 0.3
entry_label.place(relx=x_0, rely=y_0, anchor='center')

input_tab = tkinter.Entry(widget_root, width=widget_width // 10)
y_0 += 0.2
input_tab.place(relx=x_0, rely=y_0, anchor='center')

submit_button = tkinter.Button(widget_root, command=parseInput, text='Submit', font=global_font, bg='darkred', fg='white')
x_0 += -0.2
y_0 += 0.2
submit_button.place(relx=x_0, rely=y_0, anchor='center')

cancel_button = tkinter.Button(widget_root, command=cancel, text='Cancel', font=global_font, bg='darkred', fg='white')
x_0 += 0.4
cancel_button.place(relx=x_0, rely=y_0, anchor='center')

widget_root.bind('<Return>', parseInput)
widget_root.bind('<Escape>', cancel)
# widget_root.bind('exit', cancel)

widget_root.mainloop()

if __name__ == '__main__':
    print(player_names)
