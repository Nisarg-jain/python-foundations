"""Shipping cost calculation and logistics services."""

def calculate_shipping(weight_kg: float, base_rate: float = 50.0) -> float:
    """Calculates shipping cost based on weight and standard base tier."""
    if weight_kg <= 0:
        raise ValueError("Package weight must be greater than zero.")
    return base_rate + (weight_kg * 12.5)


def calculate_tax(order_subtotal: float, standard_rate: float = 0.18) -> float:
    """Calculates order tax liability."""
    return order_subtotal * standard_rate