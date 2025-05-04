import re

def format_username(name: str) -> str:
    if not isinstance(name, str):
        return ""

    formatted_name = name.strip()

    formatted_name = formatted_name.lower()

    formatted_name = re.sub(r'[^\w-]', '', formatted_name)
    print(f"Debug: Removed special chars: {formatted_name}")

    if len(formatted_name) < 3 and len(name) >= 3:
         print(f"Debug: Padding username '{formatted_name}'")
         formatted_name += "0" * (3 - len(formatted_name))

    return formatted_name

if __name__ == "__main__":
    names_to_test = [
        "  TestUser ",
        "Another User",
        " User@Name! ",
        "  OK ",
        "no",
        "  "
    ]

    print("Testing username formatting:")
    for name in names_to_test:
        original = f"'{name}'"
        formatted = format_username(name)
        print(f"Original: {original:<15} -> Formatted: '{formatted}'")
