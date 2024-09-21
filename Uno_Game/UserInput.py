import os
import numpy as np
import difflib
import random
import tkinter
from tkinter import messagebox

from ReadWrite import write_toArray
from ReadWrite import pathFormat

# Print log is to display which condition in the ValidateInput function is active during the run of Main.
print_log = True

# def closeMatch(input_str, valid_inputs, num_matches=1, match_ratio=0.6):
  # '''
  # Find close matches to the input string within the valid inputs.
  # '''
  # return df.get_close_matches(input_str, valid_inputs, n=num_matches, cutoff=match_ratio)

# def YesNo_RetryCancel(close_match, attempts=3):
#   '''
#   Handles user confirmation dialogs with 'YES', 'NO', 'RETRY', and 'CANCEL' options.
#   '''
#   for n in range(attempts):
#     attempts_left = attempts - n
#     text_ = 'attempts' if attempts_left > 1 else 'attempt'
#     if print_log: print(f'ITERATION {n + 1}')

#     user_input = messagebox.askquestion('YES OR NO', f'Did you mean to type {close_match}?')
#     if print_log: print(f'BEYOND USER INPUT ')

#     if user_input == 'yes':
#       return close_match

#     elif user_input is False:
#       messagebox.showwarning('ERROR', f'Invalid entry. {attempts_left} {text_} left before program exits.')
#     if n == attempts - 1:
#       messagebox.showinfo('USER INPUT ERROR', 'Too many invalid entries, program exited.')
#       exit()

#   return None

# def AppendInput(initial_input, num=3):
#     '''
#     Append a random number string to the initial input to create a new suggestion.
#     '''
#     num_sample = np.random.randint(1, 9, size=num).astype(str)
#     return ''.join(num_sample) + initial_input

def validateInput(user_input, **kwargs):
    '''
    Validate the user input against several conditions such as break/exit flags,
    invalid inputs, mandatory inputs, and data types.
    '''
    is_valid = True
    user_input = user_input.lower()

    # Retrieve validation criteria from kwargs
    default_values = {
        'break_flag': [],             
        'exit_flag': [],              
        'data_type': str,                  
        'invalid_input': [],  
        'mandatory_input': [],     
        'elective_input': [],         
        'match_ratio': 0.6,
    }
    default_values.update(kwargs)

    default_copy = default_values.copy()
    # Remove data type and Match Ratio
    for item_ in ['data_type', 'match_ratio']:
     default_copy.popitem(item_)

    # Get List of all words user input is compared to
    Net_matches = list(default_copy.values())

    #Match ratio determines proximaty to which user input can match a word from list
    match_ratio = default_values['match_ratio']
    close_match = difflib.get_close_matches(user_input, Net_matches, cutoff = match_ratio)
    if close_match:
      answer = messagebox.askyesno('YES OR NO VALIDATION', f'Did you try to type {close_match}')
      if answer == 'yes': return user_input
      elif answer == 'no': exit()
      elif answer is False: 
        messagebox.showerror('ERROR', F'No input by user')
        exit()
    return None

# Main test function

if __name__ == '__main__':

  file_path = r'C:\Users\Work\OneDrive\Programming\Repositories\JermaineRepo\Uno_Game\Docs\swear.txt'
  profanities = write_toArray(file_path)
  count = 1
  exit_flag = 'exit'
  break_flag = 'done'

  key_inputs = {
    'break_flag': break_flag,
    'exit_flag': exit_flag,
    'data_type': str,
    'invalid_input': profanities
  }

  players = {}

  
  run_while = False
  if run_while:
    while True:
      ...

    print(f'Players: {players}')
