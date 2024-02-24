def top_n (items, n):
  """Returns the top n items in an array, in desc order.

  Args:
      items (array): list or array-like object
      n (int): num of items, in desc order

  returns:
  array: top n items, in desc order

  Egs:
  >>> top_n([8, 2, 3, 4, 7], 3)
  [8,7,3]
  """
  for i in range(n): #keeps sorting until we have the top n items
      for j in range(len(items)-1-i):

        if items[j] > items[j+1]:
          items[j], items[j+1] = items[j+1], items[j] # swaps if this item is bigger than the next items

  #get last two items
  top_n = items[-n:]

  #return in descending order
  return top_n[::-1]
