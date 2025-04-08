# Sample Python code for testing the PR Intent Checker

def greet(name):
  """Returns a simple greeting."""
  return f"Hello, {name}!"

def add(a, b):
  """Calculates the sum of two numbers."""
  # Intentionally simple for testing
  return a + b

# Placeholder for future functions
# def subtract(a, b):
#   pass
def factorial_plus_n(n, addend):
  """Calculates the factorial of n and adds a given number."""
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  return factorial + addend