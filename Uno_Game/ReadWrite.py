import os
import pathlib as path
import inspect

# Functions to Read/Write to(from) file

# Using Pathlib
# file_path = path('loc1/loc2/loc3/')
# if file_path.exist()

def write_toArray (file_path):
  array = []
  if os.path.exists(file_path):
    with open(file_path, 'r') as file:
      array = [line.strip() for line in file]
      file.close()
    return array
  else: raise FileNotFoundError(f'The path {file_path} does not exist')

# TODO fix pathFormat
def pathFormat (file_path):
  if os.path.exist(file_path):

    try: var_ = file_path
    except: file_path = file_path.replace("\\", "/")

  else: raise FileNotFoundError(f'The path {file_path} does not exist')

run_test = True
if __name__ == '__main__' and run_test:
  
  path = '/home/wtc/Documents/hello-friend/Uno/Docs/swear.txt'
  file_array = write_toArray(path)
  print(file_array)

