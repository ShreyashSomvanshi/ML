'''
Polymorphism allows methods to do different things based on the object it is acting upon, even if they share the same name.
 This can be achieved through method overriding and duck typing.
'''

class Bird:
    def fly(self):
        return "Flies in the sky"

class Penguin(Bird):
    def fly(self):
        return "Cannot fly"

# Usage
def make_bird_fly(bird):
    print(bird.fly())

sparrow = Bird()
penguin = Penguin()

make_bird_fly(sparrow)  # Output: Flies in the sky
make_bird_fly(penguin)  # Output: Cannot fly
