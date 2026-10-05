"""Simulating stochastic systems using Python's built-in random module."""

import random


class Dice:
    """Represents a pair of standard six-sided dice."""

    def __init__(self, sides: int = 6) -> None:
        self.sides = sides

    def roll(self) -> tuple[int, int]:
        """Simulates rolling two dice and returns the outcome as a tuple."""
        first_die = random.randint(1, self.sides)
        second_die = random.randint(1, self.sides)
        return first_die, second_die


# --- Driver Code ---
dice = Dice()

# Perform sample rolls and demonstrate tuple unpacking
for round_number in range(1, 4):
    first, second = dice.roll()
    print(f"Round {round_number}: Rolled ({first}, {second}) -> Total: {first + second}")

# Demonstrating random.choice from a pool of players
roster = ["Alex", "Dev", "Sarah", "Priya"]
selected_starter = random.choice(roster)
print(f"\nStarting Player: {selected_starter}")