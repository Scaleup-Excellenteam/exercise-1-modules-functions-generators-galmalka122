def join(*lists: list, sep='-'):
  """Concatenates multiple lists into a single list with a specified separator.

    Args:
        *lists (list): Any number of lists to be concatenated.
        sep (str): Separator to be used between elements of each list. Default is '-'.

    Returns:
        A list containing all elements from the input lists concatenated with the specified separator in between.
        If no input lists are provided, returns None."""
   
  # Check if the list is not empty
  if len(lists) > 0:
    joined = []
    for li in lists:
      for el in li:
        joined.append(el)
      joined.append(sep)
    joined.pop()
    return joined
  return None