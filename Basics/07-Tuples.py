# Tuple
coordinates = (10.0, 20.0)

# Accessing elements
print(coordinates[0])  # Output: 10.0

# Tuples cannot be modified
# coordinates[0] = 15.0  # This will raise a TypeError

# List of tuples
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]

# Sort by age
students.sort(key=lambda student: student[1])
print(students)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
