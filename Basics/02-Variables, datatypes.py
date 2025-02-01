# Variables
name = "Alice"        # String
age = 30              # Integer
height = 5.5          # Float
is_student = True     # Boolean

# insert data type operations - rounding, revresing, conversions, etc

print(name, age, height, is_student)

# String Operations

# String methods
text = "  Hello, World!  "

# Stripping whitespace
cleaned_text = text.strip()

# Changing case
upper_text = cleaned_text.upper()

# Replacing text
replaced_text = cleaned_text.replace("World", "Python")

print(cleaned_text)  # Output: "Hello, World!"
print(upper_text)    # Output: "  HELLO, WORLD!  "
print(replaced_text) # Output: "  Hello, Python!  "

# Using join()
words = ["Hello", "World"]
sentence = " ".join(words)
print(sentence)  # Output: "Hello World"

# Using split()
text = "Hello, World"
words = text.split(", ")
print(words)  # Output: ['Hello', 'World']
