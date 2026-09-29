# --- While Loop Fundamentals ---

# 1. Basic increment loop
counter = 1
while counter <= 5:
    print(f"Iteration step: {counter}")
    counter += 1

print("Loop completed successfully.")

# 2. String repetition pattern
step = 1
while step <= 5:
    print("*" * step)
    step += 1

# 3. while-else demonstration
search_index = 0
while search_index < 3:
    print(f"Scanning index {search_index}...")
    search_index += 1
else:
    print("Scan finished without interruption.")