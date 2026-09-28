total_samples = input("Enter total dataset samples: ")
batch_size = input("Enter batch size: ")

samples_count = int(total_samples)
batch_count = int(batch_size)

full_batches = samples_count // batch_count
remaining_samples = samples_count % batch_count

print(f"Full Batches: {full_batches} | Remaining Samples: {remaining_samples}")