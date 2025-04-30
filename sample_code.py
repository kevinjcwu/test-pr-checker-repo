# Sample Python code for testing the PR Intent Checker

def greet(name):
  """Returns a simple greeting."""
  return f"Hello, {name}!"

def add(a, b):
  """Calculates the sum of two numbers."""
  return a + b

# Placeholder for future functions
# def subtract(a, b):
#   pass

def process_user_data(user_list):
  """
  Processes a list of user records, filtering for active users
  and returning only their email addresses.
  """
  if not user_list:
    return []

  active_user_data = []
  for user in user_list:
    # Correctly checks if user is active (assuming 'is_active' key exists)
    if user.get('is_active', False):
      # CORRECT: Append only the email if it exists
      if 'email' in user:
          active_user_data.append(user['email'])

  return active_user_data

def factorial(n):
    """
    Calculates the factorial of a non-negative integer n using recursion.
    Raises ValueError for negative input.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 1
    else:
        # Recursive step
        return n * factorial(n - 1)

def greet():
    """Returns a greeting string."""
    return "Goodbye from action"