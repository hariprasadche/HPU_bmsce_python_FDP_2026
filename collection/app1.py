def analyze_dataset(data):
    """Calculates min, max, and sum of a dataset."""
    min_val = min(data)
    max_val = max(data)
    total_sum = sum(data)

    # Return results as a single tuple (packing)
    return (min_val, max_val, total_sum)


# --- Application ---
# A fixed set of student scores that should not be changed
scores = (88, 92, 75, 95, 89)

# Call function and unpack the tuple into individual variables
min_score, max_score, total_score = analyze_dataset(scores)

print(f"Dataset: {scores}")
print(f"Lowest Score: {min_score}")
print(f"Highest Score: {max_score}")
print(f"Total Points: {total_score}")