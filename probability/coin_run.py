import numpy as np
import matplotlib.pyplot as plt

# Simulate a single trial of 50 coin flips and find the longest run of heads or tails
def simulate_coin_flip(trials=50):
    flips = np.random.choice(['H', 'T'], size=trials)
    longest_run = 1
    current_run = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 1
    return longest_run

# Generate data for 18 trials
trials_data = [simulate_coin_flip(50) for _ in range(18)]

# Step 2: Dotplot of longest runs with vertical dots
# Count the occurrences of each value in trials_data
values, counts = np.unique(trials_data, return_counts=True)

plt.figure(figsize=(8, 6))
for value, count in zip(values, counts):
    plt.plot([value] * count, np.arange(count), 'bo', markersize=8)  # Stack dots vertically
plt.title("Dotplot of Longest Runs of Coin Flips")
plt.xlabel("Longest Run Length")
plt.ylabel("Frequency (Stacked Dots)")
plt.xticks(range(1, max(values) + 1))  # Set x-ticks for each possible run length
plt.grid(True)
plt.show()

# Step 3: Calculate mean and standard deviation
mean_run = np.mean(trials_data)
std_dev_run = np.std(trials_data, ddof=1)

# Sample data from the lesson (replace with your actual data)
lesson_data = [0, 0, 3, 5, 5, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mean_lesson = np.mean(lesson_data)
std_dev_lesson = np.std(lesson_data, ddof=1)

# Step 4: Calculate z-scores for a run of 4
z_score_run = (4 - mean_run) / std_dev_run
z_score_lesson = (4 - mean_lesson) / std_dev_lesson

# Print results
print("Your data:")
print(f"Mean: {mean_run}, Standard Deviation: {std_dev_run}")
print(f"Z-score for a run of 4 in your data: {z_score_run}")

print("\nLesson data:")
print(f"Mean: {mean_lesson}, Standard Deviation: {std_dev_lesson}")
print(f"Z-score for a run of 4 in lesson data: {z_score_lesson}")
