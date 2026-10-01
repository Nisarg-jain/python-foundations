"""Demonstrating concrete return values vs display side effects."""

def compute_tax(subtotal: float, rate: float = 0.18) -> float:
    """Computes and returns the tangible tax amount."""
    return subtotal * rate


def announce_tax(subtotal: float, rate: float = 0.18) -> None:
    """Prints the tax directly to terminal without returning data."""
    print(f"[DISPLAY ONLY] Tax amount: {subtotal * rate}")


# 1. Concrete value: captured and reusable in further math
tangible_tax = compute_tax(1000.0)
final_bill = 1000.0 + tangible_tax
print(f"Final payable bill: {final_bill}")

# 2. Hollow print: holds nothing (None), cannot be reused
hollow_result = announce_tax(1000.0)
print(f"Captured variable holds: {hollow_result}")