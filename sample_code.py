# Sample Python code for testing the PR Intent Checker

def greet(name):
  """Returns a simple greeting."""
  return f"Hello, {name}!"

def add(a, b):
  """Calculates the sum of two numbers."""
  # Intentionally simple for testing
  return a + b

def subtract(a, b):
  """Calculates the difference between two numbers."""
  return a - b

# Placeholder for future functions
# def subtract(a, b):
#   pass
def factorial(n):
  """Calculates the factorial of a non-negative integer n.
  
  Args:
      n (int): The number to calculate the factorial for.
      
  Returns:
      int: The factorial of the number n.
      
  Raises:
      ValueError: If n is negative.
  """
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  if n == 0:
    return 1
  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  return factorial
