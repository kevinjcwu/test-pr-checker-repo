# Scenario 4: Ignoring Non-Functional Requirements
# Issue Intent: Optimize `process_large_file(filepath)` by reading it
# line-by-line instead of loading the whole file into memory,
# and return the number of lines containing the word "error".

import os

# --- Flawed Implementation ---
def process_large_file(filepath: str) -> int:
    """
    Counts lines containing "error" in a file.
    (Flaw: Reads the entire file into memory, ignoring the optimization intent).
    """
    print(f"Processing file: {filepath}")
    error_count = 0
    try:
        # Incorrect implementation: reads the whole file
        with open(filepath, 'r') as f:
            content = f.read() # Loads entire file - violates intent!
            lines = content.splitlines()
            for line in lines:
                if "error" in line.lower():
                    error_count += 1
        print(f"Finished processing. Found {error_count} lines with 'error'.")
        return error_count
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

# --- Example Usage ---
if __name__ == "__main__":
    # Create a dummy large file for testing
    dummy_file = "dummy_large_file.txt"
    print(f"Creating dummy file: {dummy_file}")
    try:
        with open(dummy_file, "w") as f:
            f.write("Line 1: All good.\n")
            f.write("Line 2: An error occurred.\n")
            f.write("Line 3: Another line.\n")
            f.write("Line 4: ERROR found here!\n")
            # Add more lines to simulate a larger file if needed
            for i in range(5, 100):
                 f.write(f"Line {i}: Normal operation.\n")
            f.write("Line 100: Final line, no error.\n")
        print("Dummy file created.")
    except Exception as e:
        print(f"Failed to create dummy file: {e}")

    # Run the flawed function
    count = process_large_file(dummy_file)
    print(f"Function returned count: {count}")

    # Clean up the dummy file
    try:
        os.remove(dummy_file)
        print(f"Cleaned up dummy file: {dummy_file}")
    except Exception as e:
        print(f"Failed to clean up dummy file: {e}")
