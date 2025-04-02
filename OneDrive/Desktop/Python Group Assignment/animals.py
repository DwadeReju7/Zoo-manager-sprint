# animals.py

class Animal:
    """Parent class representing an animal."""

    def __init__(self, name, species):
        """Initializes an Animal object."""
        self.name = name
        self.species = species

    def make_sound(self):
        """Prints a generic animal sound."""
        print("Generic animal sound.")

    def move(self):
        """Prints a generic movement."""
        print("Animal walks.")

class Dog(Animal):
    """Child class representing a dog."""

    def __init__(self, name, breed):
        """Initializes a Dog object."""
        super().__init__(name, species="Dog")  # Call parent's __init__
        self.breed = breed

    def make_sound(self):
        """Prints the dog's bark."""
        print("Bark!")

    def move(self):
      print("Dog catches a ball.")

class Cat(Animal):
    """Child class representing a cat."""

    def __init__(self, name, color):
        """Initializes a Cat object."""
        super().__init__(name, species="Cat")  # Call parent's __init__
        self.color = color

    def make_sound(self):
        """Prints the cat's meow."""
        print("Meow!")

    def move(self):
      print("Cat scurries quickly.")

class Bird(Animal):
  """Child class representing a Bird."""

  def __init__(self, name, wingspan):
    """Initializes a bird object"""
    super().__init__(name, species = "Bird")
    self.wingspan = wingspan

  def make_sound(self):
    print("Chirp!")

  def move(self):
    print("Bird talks.")

class Reptile(Animal):
  """Child Class representing a reptile"""

  def __init__(self, name, scale_type):
    """Initializes a reptile object"""
    super().__init__(name, species = "Reptile")
    self.scale_type = scale_type

  def make_sound(self):
    print("Hiss!")

  def move(self):
    print("Reptile slithers.")

# Example Usage (for testing):
if __name__ == "__main__":
    animal = Animal("Generic Animal", "Unknown")
    dog = Dog("Fido", "Golden Retriever")
    cat = Cat("Fluffy", "White")
    bird = Bird("Chica", "16 inches")
    reptile = Reptile("Python", "Diamond")

    animal.make_sound()
    dog.make_sound()
    cat.make_sound()
    bird.make_sound()
    reptile.make_sound()

    animal.move()
    dog.move()
    cat.move()
    bird.move()
    reptile.move()