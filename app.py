# ==============================================================================
# 1. LIST TRAVERSAL & DEFENSIVE MAX CALCULATION
# ==============================================================================
raw_dataset = [15, 42, 8, 99, 23, 54]

# Defensive guard against empty lists (IndexError prevention)
if not raw_dataset:
    max_value = None
    print("Warning: Dataset is empty.")
else:
    # Baseline linear scan: O(n) time complexity, O(1) space
    max_value = raw_dataset[0]
    for element in raw_dataset[1:]:
        if element > max_value:
            max_value = element

print(f"Max Value (Algorithmic): {max_value}")
# Idiomatic Python equivalent: max_value = max(raw_dataset) if raw_dataset else None


# ==============================================================================
# 2. 2D LISTS / MATRIX PROCESSING
# ==============================================================================
# 3x3 Coordinate Matrix
grid_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n--- Matrix Coordinate Traversal ---")
for row_idx, row in enumerate(grid_matrix):
    for col_idx, value in enumerate(row):
        print(f"Cell [{row_idx}][{col_idx}] = {value}")


# ==============================================================================
# 3. LIST MUTATIONS VS. TUPLE IMMUTABILITY
# ==============================================================================
# Mutable sequence (Dynamic Array)
mutable_buffer = [10, 20, 30]
mutable_buffer.append(40)
mutable_buffer.insert(1, 15)
removed_element = mutable_buffer.pop()  # Removes and returns the last item (40)

# Safe membership checking before index lookup to prevent ValueError
target_item = 20
if target_item in mutable_buffer:
    print(f"\nItem {target_item} found at index: {mutable_buffer.index(target_item)}")

# Immutable sequence (Read-Only Tuple)
# Used for coordinates, configuration records, and write-protected state
screen_dimensions = (1920, 1080)
print(f"Display Dimensions (Width, Height): {screen_dimensions[0]}x{screen_dimensions[1]}")