import random
import numpy as np

def modulos(numSize, unique_Id):
  """
  Computes the quotient and remainder when dividing unique_Id by numSize.

  Args:
    numSize (int): The size of the second set (used for modulo operation).
    unique_Id (int): A unique identifier to map to elements in set_1 and set_2.

  Returns:
    tuple: A tuple containing the quotient and remainder, representing indexes.
  """
  return unique_Id // numSize, unique_Id % numSize
    
def generateExclude(exclude, start=0, end=10, change=1):
  """
  Generator that yields numbers in a given range excluding specified values.

  Args:
    exclude (list): List of values to exclude from the generation.
    start (int, optional): Start of the range. Defaults to 0.
    end (int, optional): End of the range. Defaults to 10.
    change (int, optional): Step size for the range. Defaults to 1.

  Yields:
    int: The next number in the range, excluding those in the exclude list.
  """
  for n in range(start, end, change):
    if n not in exclude:
      yield n

def genRandId(set_1, set_2, unique_Id=None, output_Id=False):
  """
  Generates a random pair of elements, one from set_1 and one from set_2.

  Args:
    set_1 (list): First set of elements to choose from.
    set_2 (list or array): Second set of elements to choose from.
    unique_Id (int, optional): Unique identifier for deterministic choice. Defaults to None.
    output_Id (bool, optional): If True, returns unique_Id along with the chosen pair. Defaults to False.

  Returns:
    tuple: A tuple of elements from set_1 and set_2, or the unique_Id with the pair if output_Id is True.
  """
  set_size = len(set_1)
  numSize = len(set_2)
  productMap_size = set_size * numSize

  # Generate the unique ID if not provided
  unique_Id = random.randint(0, productMap_size) if unique_Id is None else unique_Id
  
  # Compute the index for set_1 and set_2 using modular arithmetic
  set1_indx, set2_indx = modulos(numSize, unique_Id)

  # Select the corresponding elements from set_1 and set_2
  set1_choice = set_1[set1_indx]
  set2_choice = set_2[set2_indx]

  if output_Id: 
    return unique_Id, (set1_choice, set2_choice)
  else: 
    return set1_choice, set2_choice

# region Test
run_test = True
if __name__ == '__main__' and run_test is True:
  list_1 = ['red', 'blue', 'yellow', 'green']
  list_2 = np.array(range(10))
  rand_choice = genRandId(list_1, list_2)
  print(rand_choice)
