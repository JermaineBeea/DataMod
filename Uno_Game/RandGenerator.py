import random
import numpy as np

def modulos(numSize, unique_Id):
    # A helper function to compute the modular indexes
    return unique_Id // numSize, unique_Id % numSize

def randId(set_1, set_2, unique_Id = None, output_Id = False):
    """
  Generates a random unique identifier and selects a pair of elements from set_1 and set_2
  based on the generated identifier. The identifier corresponds to an index in the product
  of the two sets.

  Args:
      set_1 (list): A list of elements in the first set.
      set_2 (list): A list of elements in the second set.
      unique_Id (int, optional): A predefined identifier to select the pair from set_1 and set_2.
                                  If not provided, a random identifier will be generated.

  Returns:
      list: A list where the first element is the unique identifier (int) and the second element
            is a tuple containing the selected pair from set_1 and set_2.
  
  Example:
      >>> randId([1, 2], ['A', 'B'])
      [2, (1, 'B')]
    """
    
    set_size = len(set_1)
    numSize = len(set_2)
    productMap_size = set_size * numSize

    # Generate the unique ID if not provided
    unique_Id = random.randrange(productMap_size) if unique_Id is None else unique_Id

    # Compute the index for set_1 and set_2 using modular arithmetic
    set1_indx, set2_indx = modulos(numSize, unique_Id)

    # Select the corresponding elements from set_1 and set_2
    set1_choice = set_1[set1_indx]
    set2_choice = set_2[set2_indx]

    if output_Id:  return unique_Id, (set1_choice, set2_choice)
    else: return set1_choice, set2_choice

import numpy as np

def generateExclude(exclude, start=0, end=10, change=1):
  # Ensure 'exclude' is an array, convert to list if it's a single value
  # Filter out the elements of 'exclude' that are outside the range [start, end)
  # Iterate over the range, yielding only those not in the 'exclude' array

  # TODO fix code below
  # exclude = np.array([exclude])
  # if exclude: exclude = exclude[(exclude >= start) & (exclude < end)]

  for n in range(start, end, change):
    if n not in exclude: yield n

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

