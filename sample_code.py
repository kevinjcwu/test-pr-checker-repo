# Sample Python code for testing the PR Intent Checker

def greet(name):
  """Returns a simple greeting."""
  # Note: This might have been modified in previous test runs if not reset
  return f"Hello, {name}!"

def add(a, b):
  """Calculates the sum of two numbers."""
  # Intentionally simple for testing
  return a + b

# Placeholder for future functions
# def subtract(a, b):
#   pass

def process_user_data(user_list):
  """
  Processes a list of user records, filtering for active users.
  (Incorrectly returns full user dicts instead of just emails).
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

# --- Group Products Test Case ---
from collections import defaultdict

def group_products_by_category(products):
    """
    Groups products by category.
    INCORRECT: Groups the full product dictionaries instead of just names.
    """
    grouped_products = defaultdict(list)
    if not isinstance(products, list):
        return {} # Return empty dict for non-list input

    for product in products:
        if isinstance(product, dict) and 'category' in product and 'name' in product:
            category = product['category']
            # INCORRECT: Appending the whole dictionary
            grouped_products[category].append(product)
        # Skips products missing name or category implicitly
    return dict(grouped_products) # Convert back to regular dict

# --- CORRECT IMPLEMENTATION (Commented Out) ---
# from collections import defaultdict
#
# def group_products_by_category(products):
#     """
#     Groups product names by their category from a list of product dictionaries.
#     """
#     grouped_products = defaultdict(list)
#     if not isinstance(products, list):
#         return {} # Return empty dict for non-list input
#
#     for product in products:
#         if isinstance(product, dict):
#             category = product.get('category')
#             name = product.get('name')
#             # Ensure both category and name are present and non-empty strings
#             if isinstance(category, str) and category and isinstance(name, str) and name:
#                 grouped_products[category].append(name)
#         # Skips products missing name or category or if they are not strings
#     return dict(grouped_products) # Convert back to regular dict
