"""Driver script demonstrating module imports and utility consumption."""

from utils import find_max

data_sample = [15, 3, 89, 42, 7, 98, 23]
peak_value = find_max(data_sample)

print(f"Dataset: {data_sample}")
print(f"Maximum Value: {peak_value}")