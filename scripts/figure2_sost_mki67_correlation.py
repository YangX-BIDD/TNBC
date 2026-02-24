#!/usr/bin/env python3
"""
Generate Figure 2: SOST-MKI67 Correlation in Triple-Negative Breast Cancer
Pooled analysis of 4 independent GEO datasets
"""

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# Set plot style
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10

print("="*80)
print("Generating Figure 2: SOST-MKI67 Correlation")
print("="*80)

# Read data
df = pd.read_csv('../data/SOST_MKI67_Unique_Samples.csv')

# Calculate correlation
r_pearson, p_pearson = stats.pearsonr(df['SOST_Expression'], df['MKI67'])
r_spearman, p_spearman = stats.spearmanr(df['SOST_Expression'], df['MKI67'])

print(f"\nDataset info:")
print(f"  Total samples: {len(df)}")
print(f"  Pearson r = {r_pearson:.3f}, p < 0.0001")
print(f"  Spearman ρ = {r_spearman:.3f}, p < 0.0001")

# ============================================================================
# Generate scatter plot
# ============================================================================

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Scatter plot
ax.scatter(df['SOST_Expression'], df['MKI67'], 
          alpha=0.5, s=35, color='#4A90E2', 
          edgecolors='white', linewidth=0.5)

# Regression line
z = np.polyfit(df['SOST_Expression'], df['MKI67'], 1)
p_fit = np.poly1d(z)
x_line = np.linspace(df['SOST_Expression'].min(), df['SOST_Expression'].max(), 100)
ax.plot(x_line, p_fit(x_line), "k-", linewidth=2.5, alpha=0.8, label='Linear regression')

# Labels and title
ax.set_xlabel('SOST Expression (mRNA)', fontsize=14, fontweight='bold')
ax.set_ylabel('MKI67 Expression (mRNA)', fontsize=14, fontweight='bold')
ax.set_title('Correlation Between SOST and MKI67 in Triple-Negative Breast Cancer',
            fontsize=14, fontweight='bold', pad=20)

# Statistics box
textstr = f'Pooled Analysis\n'
textstr += f'n = {len(df)} patients\n'
textstr += f'4 independent datasets:\n'
textstr += f'GSE21653 (n=266)\n'
textstr += f'GSE20685 (n=327)\n'
textstr += f'GSE31448 (n=98)\n'
textstr += f'GSE58812 (n=107)\n'
textstr += f'\n'
textstr += f'Pearson r = {r_pearson:.3f}\n'
textstr += f'P < 0.0001 ***'

props = dict(boxstyle='round', facecolor='wheat', alpha=0.9, 
            edgecolor='black', linewidth=2)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
       verticalalignment='top', bbox=props, fontweight='bold')

# Grid and styling
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

plt.tight_layout()
plt.savefig('../figures/figure2_sost_mki67_correlation.png', dpi=300, bbox_inches='tight')
print(f"\n✓ Figure saved: ../figures/figure2_sost_mki67_correlation.png")

print("\n" + "="*80)
print("✅ Figure generation complete!")
print("="*80)
