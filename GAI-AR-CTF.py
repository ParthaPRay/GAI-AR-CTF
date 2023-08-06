#Generative AI-Augmented Reality Combat Training Framework (GAI-AR CTF)
#Created by Partha Pratim Ray

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming reliability_scores is already defined. If not, please define it above this code.
days = list(range(1, 31))
accuracy = np.random.random(30) * 0.05 + np.linspace(0.7, 0.95, 30)
complexity = np.random.random(30) * 0.1 + np.linspace(0.5, 0.8, 30)
performance = np.random.normal(65, 10, 30)

# 1. Data Source Reliability vs Framework Accuracy
plt.figure(figsize=(12,6))
plt.plot(days, accuracy, marker='o', color='green', label='Framework Accuracy')
for label, scores in reliability_scores.items():
    plt.plot(days, scores, label=label)
plt.annotate(f'{accuracy[-1]:.2f}', xy=(days[-1], accuracy[-1]), textcoords="offset points", xytext=(0,10), ha='center')
plt.title('Data Source Reliability vs Framework Accuracy')
plt.xlabel('Days')
plt.ylabel('Score')
plt.ylim(0, 1)
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# 2. Trainee Performance Distribution & Median Performance
plt.figure(figsize=(12,6))
plt.hist(performance, bins=20, color='purple', alpha=0.7, label='Trainee Performance')
median_val = np.median(performance)
plt.axvline(median_val, color='red', linestyle='dashed', linewidth=1, label='Median Performance')
plt.annotate(f'Median: {median_val:.2f}', xy=(median_val, 0), textcoords="offset points", xytext=(0,10), ha='center', color='red')
plt.title('Trainee Performance Distribution & Median Performance')
plt.xlabel('Scores')
plt.ylabel('Number of Trainees')
plt.legend()
plt.grid(axis='y', linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# 5. Correlation Matrix remains unchanged.
correlation_matrix = np.corrcoef([accuracy, complexity] + list(reliability_scores.values()), rowvar=True)
plt.figure(figsize=(10, 10))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm",
            xticklabels=['Framework Accuracy', 'Scenario Complexity'] + list(reliability_scores.keys()),
            yticklabels=['Framework Accuracy', 'Scenario Complexity'] + list(reliability_scores.keys()))
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()


# 6. Cumulative Framework Accuracy
plt.figure(figsize=(12,6))
plt.plot(days, cumulative_accuracy, marker='o', color='green')
plt.annotate(f'{cumulative_accuracy[-1]:.2f}', xy=(days[-1], cumulative_accuracy[-1]), textcoords="offset points", xytext=(0,10), ha='center')
plt.title('Cumulative Framework Accuracy Over Time')
plt.xlabel('Days')
plt.ylabel('Cumulative Accuracy')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# 7. Moving Averages
plt.figure(figsize=(12,6))
plt.plot(days[:-6], accuracy_moving_avg, marker='o', color='green', label='7-Day Average Framework Accuracy')
plt.plot(days[:-6], complexity_moving_avg, marker='x', color='orange', label='7-Day Average Scenario Complexity')
plt.annotate(f'{accuracy_moving_avg[-1]:.2f}', xy=(days[-7], accuracy_moving_avg[-1]), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(f'{complexity_moving_avg[-1]:.2f}', xy=(days[-7], complexity_moving_avg[-1]), textcoords="offset points", xytext=(0,-20), ha='center')
plt.title('7-Day Moving Averages of Framework Accuracy and Scenario Complexity')
plt.xlabel('Days')
plt.ylabel('Score')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# 9. Boxplots for each Data Reliability Score with median annotations
plt.figure(figsize=(12, 6))
ax = sns.boxplot(data=reliability_data, palette="Set3")
plt.xticks(np.arange(len(data_types)), data_types)
plt.ylabel('Reliability Score')
plt.title('Boxplots of Data Reliability Scores for Different Data Types')
for i, key in enumerate(data_types):
    median_value = np.median(reliability_scores[key])
    plt.annotate(f'{median_value:.2f}', xy=(i, median_value), textcoords="offset points", xytext=(0,10), ha='center')
plt.grid(axis='y', linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()
