# Context managers help ensure that resources are properly managed, such as closing files after their use.
# Context managers are used to manage resources, such as file streams. The with statement is commonly used for this purpose.

# Using a context manager
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# The file is automatically closed after the block
# No need to call file.close()
