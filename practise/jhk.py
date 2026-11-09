import pandas as pd
import numpy as np
from scipy import stats

# 1. Loading the Dataset
# Make sure 'train.csv' is in the same folder as this script!
try:
    df = pd.read_csv('train.csv')
    print("File loaded successfully!\n")
except FileNotFoundError:
    print("Error: 'train.csv' not found. Please place it in the same folder.")
    exit()

# 2. Chi-Square Test: Is 4G dependent on Price Range?
# Create a cross-tabulation table
contingency_table = pd.crosstab(df['four_g'], df['price_range'])

# Perform Chi-Square Test
chi2, p_val_chi, dof, expected = stats.chi2_contingency(contingency_table)

# 3. ANOVA Test: Does RAM vary across Price Ranges? 
# Grouping RAM values by Price Range (0, 1, 2, 3)
groups = [df[df['price_range'] == i]['ram'] for i in range(4)]

# Perform One-Way ANOVA
f_stat, p_val_anova = stats.f_oneway(*groups)

# --- Display Results ---
print("--- Chi-Square Analysis (4G vs Price Range) ---")
print(f"Chi2 Statistic: {chi2:.4f}")
print(f"P-value: {p_val_chi:.4f}")

print("\n--- ANOVA Analysis (RAM vs Price Range) ---")
print(f"F-Statistic: {f_stat:.4f}")
print(f"P-value: {p_val_anova:.4f}")

# Brief Interpretation
if p_val_anova < 0.05:
    print("\nResult: RAM has a significant impact on Price Range.")
else:
    print("\nResult: No significant difference in RAM across Price Ranges.")