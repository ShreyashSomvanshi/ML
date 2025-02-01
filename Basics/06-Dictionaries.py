# add all other operations

# Dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: Alice

# Adding a new key-value pair
person["email"] = "alice@example.com"
print(person)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Dictionary
scores = {"Alice": 85, "Bob": 90, "Charlie": 80}

# Sort by value
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
print(sorted_scores)  # Output: {'Charlie': 80, 'Alice': 85, 'Bob': 90}

