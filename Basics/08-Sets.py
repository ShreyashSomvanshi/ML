# Set
unique_numbers = {1, 2, 3, 4, 4, 5}

# Adding an element
unique_numbers.add(6)

# Sets automatically remove duplicates
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Set comprehension
unique_squares = {x**2 for x in [1, 2, 2, 3, 4]}
print(unique_squares)  # Output: {1, 4, 9, 16}

