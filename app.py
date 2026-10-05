"""Driver script demonstrating package-level modular architecture."""

from ecommerce.shipping import calculate_shipping, calculate_tax

order_weight = 3.5  # in kilograms
order_subtotal = 1200.0

shipping_cost = calculate_shipping(order_weight)
tax_amount = calculate_tax(order_subtotal)
final_total = order_subtotal + shipping_cost + tax_amount

print(f"Order Subtotal: Rs. {order_subtotal:.2f}")
print(f"Shipping Cost:  Rs. {shipping_cost:.2f}")
print(f"Estimated Tax:  Rs. {tax_amount:.2f}")
print(f"Total Payable:  Rs. {final_total:.2f}")