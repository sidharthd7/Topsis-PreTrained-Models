import numpy as np
import pandas as pd

models = ["GPT-3", "DialoGPT", "BlenderBot", "T5 Conversational", "BERT Dialogue"]

# Columns represent [Response Relevance, Fluency, Diversity, Latency, Memory Usage]
scores = np.array([
    [9, 8, 7, 6, 5],  # GPT-3
    [8, 7, 8, 7, 6],  # DialoGPT
    [7, 9, 6, 8, 7],  # BlenderBot
    [6, 6, 7, 9, 8],  # T5 Conversational
    [8, 7, 7, 6, 9]   # BERT Dialogue
])

weights = np.array([0.3, 0.25, 0.2, 0.15, 0.1])  

beneficial = [True, True, True, False, False]  

norm_scores = scores / np.sqrt((scores ** 2).sum(axis=0))

weighted_scores = norm_scores * weights

ideal_solution = np.max(weighted_scores, axis=0) if beneficial[0] else np.min(weighted_scores, axis=0)
anti_ideal_solution = np.min(weighted_scores, axis=0) if beneficial[0] else np.max(weighted_scores, axis=0)

for i, is_beneficial in enumerate(beneficial[1:], 1):
    if not is_beneficial:
        ideal_solution[i] = np.min(weighted_scores[:, i])
        anti_ideal_solution[i] = np.max(weighted_scores[:, i])

dist_ideal = np.sqrt(((weighted_scores - ideal_solution) ** 2).sum(axis=1))
dist_anti_ideal = np.sqrt(((weighted_scores - anti_ideal_solution) ** 2).sum(axis=1))

topsis_scores = dist_anti_ideal / (dist_ideal + dist_anti_ideal)

# ranking
ranking = np.argsort(-topsis_scores) + 1  

results_df = pd.DataFrame({
    "Model": models,
    "TOPSIS Score": topsis_scores,
    "Rank": ranking
}).sort_values(by="Rank")

print("Results:")
print(results_df)

results_df.to_csv("topsis_results.csv", index=False)
