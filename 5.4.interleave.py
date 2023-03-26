def interleave(*iteratables):
  """
  Interleaves multiple iterables into a single list.

  Args:
  *iteratables: A variable number of iterables to be interleaved.

  Returns:
  list: A list containing the interleaved elements from all iterables.
  """
  interleave_list = []
  for i in range(len(iteratables)):
      for j in range(len(iteratables)):
          interleave_list.append(iteratables[j][i])
  return interleave_list


def iteratable_generator(iteratable):
  """
  Converts an iterable into a generator object.

  Args:
  iteratable: The iterable to be converted.

  Returns:
  generator: A generator object that yields the elements of the iterable.
  """
  for el in iteratable:
      yield el


def interleave_with_generators(*iteratables):
  """
  Interleaves the elements of multiple iterables and returns them in a list.

  Args:
  *iteratables: A variable number of iterables to be interleaved.

  Returns:
  list: A list containing the interleaved elements from all iterables.
  """
  new_list = []
  list_of_generators = [iteratable_generator(iteratable) for iteratable in iteratables]
  for i in range(len(iteratables[0])):
      for generator in list_of_generators:
          el = next(generator)
          new_list.append(el)
  return new_list