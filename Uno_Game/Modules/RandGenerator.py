import random
import numpy as np

def modulos(numSize, unique_Id):
    # A helper function to compute the modular indexes
    return unique_Id // numSize, unique_Id % numSize
    
def generateExclude(exclude, start = 0, end = 10, change = 1):
  for n in range(start, end, change):
    if n not in exclude: yield n

def randId(set_1, set_2, exclude = [], unique_Id = None, output_Id = True):
 
    set_size = len(set_1)
    numSize = len(set_2)
    productMap_size = set_size * numSize

    # Generate the unique ID if not provided
    # TODO address if exclude should be part of randID
    #valid_range = list(generateExclude(exclude, 0, productMap_size))
    #unique_Id = random.choice(valid_range) if unique_Id is None else unique_Id
    unique_Id = np.random.randint(low = start, high = end, size = 1)
    # Compute the index for set_1 and set_2 using modular arithmetic
    set1_indx, set2_indx = modulos(numSize, unique_Id)

    # Select the corresponding elements from set_1 and set_2
    set1_choice = set_1[set1_indx]
    set2_choice = set_2[set2_indx]

    if output_Id:  return unique_Id, (set1_choice, set2_choice)
    else: return set1_choice, set2_choice

# region Test
run_test = True
if __name__ == '__main__' and run_test is True:
	
  list_1 = ['red', 'blue', 'yellow', 'green']
  list_2 = np.array(range(10))
  rand_choice = randId(list_1, list_2)

  exlude = [1, 2, 3, 4]
  list_1 = list(generateExclude(exlude, 0, 10))
  print(f'{list_1}')

  # print(list_2)
# endregion

