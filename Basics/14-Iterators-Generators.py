# Generators are a way to create iterators using the yield keyword

# Generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)  # Output: 1, 2, 3, 4, 5
