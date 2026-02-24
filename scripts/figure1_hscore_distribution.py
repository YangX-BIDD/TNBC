#!/usr/bin/env python3
"""
Generate Figure 1: H-Score Distribution for TNBC, HER2, and Luminal Subtypes
Three-panel histogram with normal distribution fit
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Set plot style
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("="*80)
print("Generating Figure 1: H-Score Distribution")
print("="*80)

# Read data
df = pd.read_excel('../data/TNBC_HER2_Luminal-SOST.xlsx')

tnbc_scores = df['TNBC'].dropna().values
her2_scores = df['HER2'].dropna().values
luminal_scores = df['Luminal'].dropna().values

# Define subtypes
subtypes = {
    'TNBC': tnbc_scores,
    'HER2': her2_scores,
    'Luminal': luminal_scores
}

# Colors for each subtype
colors = ['#E74C3C', '#3498DB', '#2ECC71']  # Red, Blue, Green

# Cutoff values (can be adjusted)
cutoffs = {
    'TNBC': 50,
    'HER2': 50,
    'Luminal': 50
}

# ============================================================================
# Generate Figure: 1x3 layout with normal fit
# ============================================================================

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.patch.set_facecolor('white')

for idx, (subtype, scores) in enumerate(subtypes.items()):
    ax = axes[idx]
    
    # Histogram with density
    n, bins, patches = ax.hist(scores, bins=15, density=True, alpha=0.7,
                                color=colors[idx], edgecolor='black', linewidth=1)
    
    # Normal distribution fit
    mu = np.mean(scores)
    sigma = np.std(scores, ddof=1)
    x = np.linspace(scores.min(), scores.max(), 100)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'k-', linewidth=2,
            label=f'Normal fit\nμ={mu:.1f}, σ={sigma:.1f}')
    
    # Cutoff line
    cutoff = cutoffs[subtype]
    ax.axvline(cutoff, color='red', linestyle='--', linewidth=2.5, 
              label=f'Cutoff = {cutoff}')
    
    # Shade positive region
    n_pos = np.sum(scores > cutoff)
    rate = n_pos / len(scores) * 100
    ax.fill_between([cutoff, scores.max()], 0, ax.get_ylim()[1], 
                     alpha=0.2, color='red')
    
    # Labels and title
    ax.set_xlabel('H-Score', fontsize=13, fontweight='bold')
    ax.set_ylabel('Density', fontsize=13, fontweight='bold')
    ax.set_title(f'{subtype}\n(N={len(scores)})',
                 fontsize=15, fontweight='bold')
    ax.legend(fontsize=10, loc='upper right', frameon=True, shadow=True)
    ax.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('../figures/figure1_hscore_distribution.png', dpi=300, bbox_inches='tight', facecolor='white')
print(f"\n✓ Figure saved: ../figures/figure1_hscore_distribution.png")

print("\n" + "="*80)
print("Summary Statistics:")
print("="*80)
for subtype, scores in subtypes.items():
    cutoff = cutoffs[subtype]
    n_pos = np.sum(scores > cutoff)
    rate = n_pos / len(scores) * 100
    print(f"{subtype:8s}: n={len(scores):3d}, Mean={np.mean(scores):5.1f}, "
          f"SD={np.std(scores, ddof=1):5.1f}, Positive={n_pos:3d} ({rate:4.1f}%)")

print("\n✅ Figure generation complete!")
