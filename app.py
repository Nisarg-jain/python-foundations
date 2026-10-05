"""Demonstrating class inheritance, method reuse, and specialization."""

class Mammal:
    """Base parent class defining shared mammalian behaviors."""

    def __init__(self, name: str) -> None:
        self.name = name

    def walk(self) -> None:
        """Generic locomotion method common to all mammals."""
        print(f"{self.name} is walking.")


class Dog(Mammal):
    """Derived child class specializing Mammal with canine behaviors."""

    def bark(self) -> None:
        """Canine-specific behavior."""
        print(f"{self.name} says: Woof! Woof!")


class Cat(Mammal):
    """Derived child class specializing Mammal with feline behaviors."""

    def meow(self) -> None:
        """Feline-specific behavior."""
        print(f"{self.name} says: Meow!")


# 1. Instantiating derived objects
dog = Dog("Buddy")
cat = Cat("Luna")

# 2. Invoking inherited methods from the Mammal parent class
dog.walk()
cat.walk()

# 3. Invoking specialized child methods
dog.bark()
cat.meow()