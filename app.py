import math

# 1. Division variations and powers
loss_value = 10 / 3
epoch_step = 10 // 3
scale_factor = 2 ** 4
remainder = 10 % 3

print(f"Float division: {loss_value}")
print(f"Floor division: {epoch_step}")
print(f"Power: {scale_factor}")
print(f"Remainder: {remainder}")

# 2. Augmented assignment
current_learning_rate = 0.1
current_learning_rate *= 0.5
print(f"Adjusted LR: {current_learning_rate}")

# 3. Operator precedence: () -> ** -> * / // % -> + -
precedence_result = (10 + 2) * 3 ** 2 / 2
print(f"Precedence result: {precedence_result}")

# 4. Built-in functions and math module
raw_score = -4.72
print(f"Absolute: {abs(raw_score)}")
print(f"Rounded: {round(raw_score, 1)}")
print(f"Ceil: {math.ceil(4.1)}")
print(f"Floor: {math.floor(4.9)}")