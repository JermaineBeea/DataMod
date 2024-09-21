# Password Guess
from UserInput import validateInput

Password = 'I Love bananas'

guesses = []
attempts = 100

break_flag = 'end'

key_input = {
  'break_flag': break_flag
}

attempt_counter = 0
while attempt_counter < attempts:
  user_input = input(f'Try guess password or type end to stop program: ')

  is_valid = validateInput(user_input, **key_input)
  if is_valid: attempt_counter += 1
  if user_input == Password or user_input == break_flag: break
  else:guesses.append(user_input)

print('Program finished')



