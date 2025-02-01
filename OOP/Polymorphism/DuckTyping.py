"""
Polymorphism is a core concept in object-oriented programming that allows methods to do different things based on the object it is acting upon.

Duck typing is a type of polymorphism that is based on the idea that if an object behaves
like a certain type (i.e., it has the required methods and properties), it can be treated as
that type, regardless of its actual class. This is often summarized by
the phrase "If it looks like a duck and quacks like a duck, it must be a duck."
"""

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

# Usage
dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!


