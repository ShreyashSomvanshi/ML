# Add more complex syntax

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Handling multiple exceptions
# handle multiple exceptions in a single except block.
try:
    result = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")
