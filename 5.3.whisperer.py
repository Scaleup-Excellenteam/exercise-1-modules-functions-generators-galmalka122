def lazy_byte_open():
  """
  Opens and reads a file in bytes mode, yielding each line.

  Returns:
  generator: A generator object that yields each line of the file.
  """
  with open(r"resources\logo.jpg", 'rb') as logo:
      for line in logo:
          yield line

def decrypt_line(line: str):
  """
  Decrypts a string by extracting all words that are at least five characters long with exclamation mark at the end.

  Args:
  line (str): The string to be decrypted.

  Returns:
  list: A list of all decrypted words.
  """
  line = line.decode("ISO-8859-1")
  words = []
  temp = ''
  for char in line:
      if char.isalpha() and char.islower():
          temp += char
      elif char == '!' and len(temp) > 5:
          words.append(temp)
          temp = ''
      else:
          temp = ''
  return words

def whisperer():
  """
  Reads each line of a file, and decrypts it.

  Returns:
  str: A string containing all decrypted words separated by spaces.
  """
  line_generator = lazy_byte_open()
  decrypted_words = []
  for line in line_generator:
      found_words = decrypt_line(line)
      decrypted_words.extend(found_words)
  return ' '.join(decrypted_words)