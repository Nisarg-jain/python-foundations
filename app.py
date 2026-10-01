"""Positional vs Keyword Arguments demonstration."""

def calculate_invoice(subtotal: float, tax_rate: float, discount: float) -> float:
    """Calculates final total after applying tax and flat discount."""
    tax_amount = subtotal * tax_rate
    final_total = (subtotal + tax_amount) - discount
    return round(final_total, 2)


# 1. Positional Arguments (Order strictly defines parameter mapping)
total_a = calculate_invoice(100.0, 0.18, 10.0)
print(f"Total A (Positional): ${total_a}")

# 2. Keyword Arguments (Explicit labels; order does not matter)
total_b = calculate_invoice(tax_rate=0.18, discount=10.0, subtotal=100.0)
print(f"Total B (Keyword):    ${total_b}")

# 3. Hybrid Call (Positional must always precede Keyword arguments)
total_c = calculate_invoice(100.0, discount=10.0, tax_rate=0.18)
print(f"Total C (Hybrid):     ${total_c}")