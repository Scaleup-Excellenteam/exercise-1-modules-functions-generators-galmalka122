from datetime import date, datetime, timedelta
from random import randrange

def i_dont_have_vinaigrette() -> date:
  """Generates a random date within a given range and checks if it falls on a Monday.
  If the generated date falls on a Monday, prints "i dont have vinaigrette!".
  
  Returns:
    A datetime.date object representing the generated date."""
  
  date_format = '%Y-%m-%d'
  
  # Prompt the user to enter the starting and ending dates in 'YYYY-MM-DD' format
  starting_date = input("Please enter a starting date in 'YYYY-MM-DD' format: ")
  ending_date = input("Please enter a ending datein in 'YYYY-MM-DD' format: ")
  
  # Parse the starting and ending dates into datetime.date objects
  starting_date = datetime.strptime(starting_date, date_format).date()
  ending_date = datetime.strptime(ending_date, date_format).date()
  
  # Generate a random number of days within the given range and add it to the starting date
  random_num = randrange(0, (ending_date - starting_date).days)
  random_date = starting_date + timedelta(days=random_num)
  
  # Check if the generated date falls on a Monday, and print a message if it does
  if random_date.weekday() == 0:
    print("i dont have vinaigrette!")
    
  # Return the generated date 
  return random_date