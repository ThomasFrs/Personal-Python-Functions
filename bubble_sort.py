def bubble_sort(list):
  """
  list: array of unsorted integers
  return: list sorted in ascending order
  """
  for i in range(len(list)):
    # length of the list left to run through
    for j in range(len(list) - i - 1):
      # swap elements
      if list[j] > list [j+1]:
        list[j], list[j+1] = list[j+1], list[j]
  return list

assert bubble_sort([1,3,5,4,2]) == [1, 2, 3, 4, 5], "bubble_sort([1,3,5,4,2]),[1, 2, 3, 4, 5]"
assert bubble_sort([0,1,545,2]) == [0,1,2,545], "bubble_sort([0,1,545,2]), [0,1,2,545]"