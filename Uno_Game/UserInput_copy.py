import os
import numpy as np
import difflib as df
import random
import tkinter
from tkinter import messagebox

from ReadWrite import write_toArray
from ReadWrite import pathFormat

# Print log is to display which condition in the ValidateInput function is active during the run of Main.
print_log = True

def closeMatch(input_str, valid_inputs, num_matches=1, match_ratio=0.6):
  """
  Find close matches to the input string within the valid inputs.
  """
  return df.get_close_matches(input_str, valid_inputs, n=num_matches, cutoff=match_ratio)

def YesNo_RetryCancel(close_match, attempts=3):
  """
  Handles user confirmation dialogs with 'YES', 'NO', 'RETRY', and 'CANCEL' options.
  """
  for n in range(attempts):
    attempts_left = attempts - n
    text_ = 'attempts' if attempts_left > 1 else 'attempt'
    if print_log: print(f'ITERATION {n + 1}')

    user_input = messagebox.askquestion('YES OR NO', f'Did you mean to type {close_match}?')
    if print_log: print(f'BEYOND USER INPUT ')

    if user_input == 'yes':
      return close_match

    elif user_input is False:
      messagebox.showwarning('ERROR', f'Invalid entry. {attempts_left} {text_} left before program exits.')
    if n == attempts - 1:
      messagebox.showinfo('USER INPUT ERROR', 'Too many invalid entries, program exited.')
      exit()

  return None

def AppendInput(initial_input, num=3):
    """
    Append a random number string to the initial input to create a new suggestion.
    """
    num_sample = np.random.randint(1, 9, size=num).astype(str)
    return ''.join(num_sample) + initial_input

def validateInput(user_input, **kwargs):
    """
    Validate the user input against several conditions such as break/exit flags,
    invalid inputs, mandatory inputs, and data types.
    """
    is_valid = True
    user_input = user_input.lower()

    # Retrieve validation criteria from kwargs
    break_flag = kwargs.get('break_flag', [])
    exit_flag = kwargs.get('exit_flag', [])
    data_type = kwargs.get('data_type', None)
    invalid_input = kwargs.get('invalid_input', [])
    mandatory_input = kwargs.get('mandatory_input', [])
    elective_input = kwargs.get('elective_input', [])

    # Break/Exit flag validation
    if break_flag or exit_flag:
        if print_log: print('BREAK/EXIT CONDITION')
    
    # Break/Exit Validation
    if user_input in [break_flag, exit_flag]:
      if print_log: print('BREAK/EXIT CONDITION')
      return user_input, is_valid
    close_match = closeMatch(user_input, [break_flag, exit_flag], match_ratio=0.8)
    if close_match:
      if print_log: print('CLOSE MATCH FOUND')
      user_input = YesNo_RetryCancel(close_match[0])
      return user_input, is_valid

    # Data type validation
    if data_type is not None and not isinstance(user_input, data_type):
      if print_log: print('DATA TYPE CONDITION')
      is_valid = False
      print(f'Invalid data type. Expected {data_type}, got {type(user_input)}')
      return user_input, is_valid

    # Invalid input validation
    if invalid_input:
      if print_log: print('INVALID CONDITION')
      close_match = closeMatch(user_input, invalid_input, match_ratio=0.6)
      if close_match:
        is_valid = False
        print(f'Invalid input: {close_match[0].upper()}')
        return user_input, is_valid

    # Mandatory input validation
    if mandatory_input and user_input not in mandatory_input:
      if print_log: print('MANDATORY CONDITION')
      close_match = closeMatch(user_input, mandatory_input)
      if close_match and user_input not in mandatory_input:
        user_input = YesNo_RetryCancel(close_match[0])
        return user_input, False
      else:
        print(f'Please enter one of the mandatory inputs: {mandatory_input}')
        return user_input, False

    # Elective input validation
    if elective_input:
      if print_log: print('ELECTIVE CONDITION')
      close_match = closeMatch(user_input, elective_input)
      if close_match and user_input not in elective_input:
        user_input = YesNo_RetryCancel(close_match[0])
        return user_input, is_valid

    return user_input, is_valid

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

  while True:
    message = f'Player {count}, please enter your name. Type {break_flag.upper()} to finish or {exit_flag.upper()} to quit the game: '
    name_input = input(message).lower()
    name_input, is_valid = validateInput(name_input, **key_inputs)

    if name_input == break_flag: break
    if name_input == exit_flag: exit()

    if is_valid:
      if name_input not in players:
        players[name_input] = []
        count += 1
      else:
        suggested_name = AppendInput(name_input)
        print(f'ERROR! Name "{name_input}" is already taken. Try "{suggested_name}" instead.')

  print(f'Players: {players}')
