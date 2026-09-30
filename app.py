# --- For Loops & Range Traversals ---

# 1. Sequence and Range Iteration
total_cart_cost = 0
prices = [10, 25, 45, 90]

for price in prices:
    total_cart_cost += price

print(f"Total Cart Value: ${total_cart_cost}")

# 2. Cartesian Coordinates via Nested Loops
print("\n--- Coordinate Grid (x, y) ---")
for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")

# 3. Shape Generation (Nested Loop Matrix Traversal)
print("\n--- Matrix-Generated 'F' Shape ---")
f_shape_blueprint = [5, 2, 5, 2, 2]

for row_width in f_shape_blueprint:
    row_buffer = ""
    for _ in range(row_width):
        row_buffer += "x"
    print(row_buffer)