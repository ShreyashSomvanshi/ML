# add more complex example

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAppending a new line.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
