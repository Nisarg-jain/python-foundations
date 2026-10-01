"""Object-oriented domain model demonstrating state initialization via __init__."""

class CoordinatePoint:
    """Represents a 2D geometric coordinate point."""

    def __init__(self, x: int | float, y: int | float) -> None:
        # Bind parameter inputs directly to instance state
        self.x = x
        self.y = y

    def render(self) -> None:
        """Outputs current coordinate state to stdout."""
        print(f"CoordinatePoint rendered at: ({self.x}, {self.y})")


class Person:
    """Represents an individual entity with identity and behavioral methods."""

    def __init__(self, name: str) -> None:
        self.name = name

    def talk(self) -> None:
        """Greets with the instance-bound name attribute."""
        print(f"Hi, I am {self.name}.")


# 1. Coordinate Point Instantiation
origin = CoordinatePoint(0, 0)
target = CoordinatePoint(1920, 1080)
origin.render()
target.render()

# 2. Entity State Isolation
engineer = Person("Alex")
lead = Person("Sarah")
engineer.talk()
lead.talk()