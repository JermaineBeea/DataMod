import random
import numpy as np

user_input = 'david'

characters = ['@', '$', '&']
rand_num = np.random.randint(1, 10, size = 2).astype(str)
rand_char = random.choice(characters)
str_num = ''.join(rand_num)
appended = ''.join((user_input, rand_char, str_num))

type_ = type(appended)
print(type_)