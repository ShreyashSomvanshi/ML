# Lists are used to store multiple items in a single variable.

# List comprehension
squares = [x**2 for x in range(10)]
print(squares)


# List
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple

# Adding an element
fruits.append("orange")
print(fruits)

# List methods
numbers = [1, 2, 3, 4, 5]

# Append
numbers.append(6)

# Remove
numbers.remove(3)

# Sort
numbers.sort(reverse=True)

print(numbers)  # Output: [6, 5, 4, 2, 1]


# Sorting a list
numbers = [5, 2, 9, 1, 5, 6]

# Using sort() method (in-place)
numbers.sort()

# Using sorted() function (returns a new list)
sorted_numbers = sorted(numbers, reverse=True)

print(numbers)         # Output: [1, 2, 5, 5, 6, 9]
print(sorted_numbers) # Output: [9, 6, 5, 5, 2, 1]

# List of tuples
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]

# Sort by age
students.sort(key=lambda student: student[1])
print(students)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# Filtering even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6]
