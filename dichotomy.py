def dichotomy(list, value):
  """
  list: array of integers in ascending order
  value: value to return its position in list
  return: False in value not in list, else the position of value in the list
  """
  list_beginning = 0
  list_end = len(list)
  list_middle = ((list_beginning+list_end)//2)
  if value not in list:
    return False
  while list[list_middle] != value:
    # middle index is calculated at each iteration
    list_middle = ((list_beginning+list_end)//2)
    # tests if value is superior to the middle value
    if value > list[list_middle]:
      list_beginning = list_middle
    # tests if value is inferior to the middle value
    if value < list[list_middle]:
      list_end = list_middle
  return list_middle

assert dichotomy([1,2,3,4], 3) == 2, "dichotomy([1,2,3,4], 3), 2"
assert dichotomy([1,2,3,4,5,6], 7) == False, "dichotomy([1,2,3,4,5,6], 7), False"