import pandas as pd
import numpy as np
# Load dataset
df = pd.read_csv("students.csv")
# Convert math_score column to NumPy array
math_scores = df["math_score"].values
# Mean, Median, Max, Min
mean_val = np.mean(math_scores)
median_val = np.median(math_scores)
max_val = np.max(math_scores)
min_val = np.min(math_scores)
print("Mean:", mean_val)
print("Median:", median_val)
print("Max:", max_val)
print("Min:", min_val)
# Normalization (Min-Max Scaling)
normalized_scores = (math_scores - min_val) / (max_val - min_val)
# Add normalized column to dataframe
df["normalized_math"] = normalized_scores
# Final output
print("\nFinal Dataset:\n")
print(df)

