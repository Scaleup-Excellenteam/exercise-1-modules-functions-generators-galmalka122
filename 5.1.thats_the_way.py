from os import listdir

def thats_the_way(path: str) -> None:
  """Print a numbered list of files in a directory that starts with the string "deep"

  Args:
      path (str): Path to a directory
  """
  files_starts_with_deep = [file_name for file_name in listdir(path) if file_name.startswith("deep")]
  for index, starts_with_deep in enumerate(files_starts_with_deep,1):
    print(f"{index} : {starts_with_deep}")