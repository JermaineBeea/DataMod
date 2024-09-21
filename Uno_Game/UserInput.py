import os
import numpy as np
import difflib as df
import random
import tkinter
from tkinter import messagebox

from ReadWrite import write_toArray

# Print log is to display which condition in the ValidateInput function are active durig run of Main.
print_log = False

def closeMatch (input, valid_inputs, **kwargs):
  """
  KEY INPUTS:
    num_matches: Default is 1
    match_ratio: Default is 0.6
  """
  num_matches = kwargs.get('num_matches', 1)
  match_ratio = kwargs.get('match_ratio', 0.6)
  close_match = df.get_close_matches(input, valid_inputs, n = num_matches, cutoff = match_ratio)
  return close_match

def YesNo (initial_input, close_match, attempts = 3):
  for n in range(attempts):
    attempts_left = attempts - n
    text_ = 'attempts' if attempts_left > 1 else 'attempts'
    user_input = messagebox.askyesno('YES OR NO', f'Did you imply to type {close_match}')
    
    if user_input is False: messagebox.showwarning(f'ERROR', f'NO entry made {attempts_left} {text_} left before program Exists')
    elif n == attempts: messagebox.showinfo('USER ERROR', 'Too many invalid entries, program exited'); exit()

  # If use enter valid response YES or NO
  for n in range(attempts):
    attempts_left = attempts - n
    if user_input == 'yes': user_input = close_match[0]; return user_input
    elif user_input == 'no' : 
      user_input = messagebox.askretrycancel('RETRY OR CANCEL', f'Retry or Cancel to Exit program')
      if user_input is False: messagebox.showwarning(f'ERROR', f'NO entry made {attempts_left} {text_} left before program Exists')

def AppendInput (initial_input, num = 3):
  num_sample = np.random.randint(low = 1, high = 9, size = num).astype(str)
  str_1 = ''.join(num_sample)
  appended_input = ''.join((str_1, initial_input))
  return appended_input

def validateInput(user_input, **kwargs):
  """
  key Inputs:
    data_type Default -> None
    break_flag: Default -> []
    exit_flag = Default -> []
    invalid_input = Default -> []
    mandatory_input = Default -> []
    elective_input = Default -> []

  """
  is_valid = True
  user_input = user_input.lower()

  # region Default Key arguments
  break_flag = kwargs.get('break_flag', [])
  exit_flag = kwargs.get('exit_flag', [])
  data_type = kwargs.get('data_type', None)
  invalid_input = kwargs.get('invalid_input', [])
  mandatory_input = kwargs.get('mandatory_input', [])
  elective_input = kwargs.get('elective_input', [])
  # endregion

  # Break/Exit flag validation
  if break_flag or exit_flag:
    if print_log: print('BREAK/EXIT CONDITION')
    Break_Exit = [break_flag] + [exit_flag]
    close_match = closeMatch(user_input,Break_Exit, match_ratio = 0.8)
    if user_input in Break_Exit: return user_input, is_valid
    # Run YesNo function to validate if user wanted to type the close match
    elif close_match: 
      user_input = YesNo(user_input,close_match)
      return user_input, is_valid
  
  # User validation for DATA TYPE 
  input_type = type(user_input)
  if data_type is not None  and not isinstance(user_input, data_type):
    if print_log:print('DATA TYPE CONDITION')
    is_valid = False   
    print(f'Data type of {input_type} is invalid. Please enter correct data type {data_type}')
    return user_input, is_valid
  
  # User validation for INVALID input
  if invalid_input: 
    if print_log:print('INVALID CONDITION')
  # Check to see if input is part of invalid 
  # match_ratio is lowered to 0.4 to ensure better filetring of invalid data
    close_match = closeMatch(user_input, invalid_input, match_ratio = 0.6)
    if close_match:
      is_valid = False
      print(f'Please ensure your input does not contain {close_match[0].upper()}')
      return user_input, is_valid

  # User validation for MANDATORY input
  if mandatory_input and user_input not in mandatory_input:
    if print_log:print('MANDATORY CONDITION')
    # Check to see if User did not mispell
    close_match = closeMatch(user_input, mandatory_input)
    # Run YesNo function to determine if user wanted to type close match
    if close_match and user_input not in mandatory_input: YesNo(user_input, close_match)
    else: print(f'Please type one of the mandatory inputs -> {mandatory_input}')
    is_valid = False
    return user_input, is_valid

  # User input validation for ELECTIVE input
  if elective_input:
    if print_log:print('ELECTIVE CONDITION')
    close_match = closeMatch(user_input, elective_input)
    # Run YesNo function to determine if user wanted to type close match
    if close_match and user_input not in elective_input: YesNo(user_input, close_match)
    else: return user_input, is_valid

  return user_input, is_valid

# region Test Defined Functions
run_test = True
if __name__ == '__main__' and run_test is True:

  file_path = '/home/wtc/Documents/hello-friend/Uno_Game/Docs/swear.txt'
  profanities = write_toArray(file_path)
  count = 1
  exit_flag = 'exit'
  break_flag = 'done'

  key_inputs = {
    'break_flag' :break_flag,
    'exit_flag' :exit_flag,
    'data_type' : str,
    'invalid_input' : profanities
  }

  players = {}

  while True:
    message = f'Player {count} Please enter name, type {break_flag.upper()} to finish or {exit_flag.upper()} to quit game : '
    name_input = input(message)
    name_input = name_input.lower()
    name_input, is_valid = validateInput(name_input, **key_inputs)
    if name_input == break_flag: break
    if name_input == exit_flag: exit()
    if is_valid:
      if name_input not in players.keys():
        count = count + 1
        players[name_input] = []
      else: 
        suggested_name = AppendInput(name_input)
        print(f'ERROR!, Name {name_input} already taken, try name {suggested_name}')
         
  print(f'Players are {players}')

  # endregion