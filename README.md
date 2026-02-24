# SOST in Triple-Negative Breast Cancer: Analysis Code and Figures

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18752090.svg)](https://doi.org/10.5281/zenodo.18752090)

## Overview
This repository contains code and data for generating key figures in the SOST-TNBC research project.

## Directory Structure

```
github/
├── data/              # Input data files
├── figures/           # Generated figures
├── scripts/           # Python scripts for analysis
└── README.md         # This file
```

## Figures

### Figure 1: H-Score Distribution Across Breast Cancer Subtypes
**File**: `figures/figure1_hscore_distribution.png`  
**Script**: `scripts/figure1_hscore_distribution.py`  
**Data**: `data/TNBC_HER2_Luminal-SOST.xlsx`

This figure shows:
- H-Score distribution across TNBC (n=100), HER2+ (n=94), and Luminal (n=99) subtypes
- Unified cutoff analysis (Q3 = 51.80)
- Statistical comparison between subtypes
- 4-panel layout: distribution, boxplot, positivity rates, and summary statistics

**Key Results**:
- TNBC: 25% positivity rate
- HER2+: 9.6% positivity rate  
- Luminal: 82.8% positivity rate
- Chi-square test: p < 0.0001 ***

### Figure 2: SOST-MKI67 Correlation in TNBC
**File**: `figures/figure2_sost_mki67_correlation.png`  
**Script**: `scripts/figure2_sost_mki67_correlation.py`  
**Data**: `data/SOST_MKI67_Unique_Samples.csv`

This figure shows:
- Pooled analysis of 798 TNBC patients from 4 independent datasets
- Positive correlation between SOST and MKI67 expression
- Datasets: GSE21653 (n=266), GSE20685 (n=327), GSE31448 (n=98), GSE58812 (n=107)

**Key Results**:
- Pearson r = 0.571, p < 0.0001 ***
- All data from publicly available GEO datasets

## Data Sources

All gene expression data are from publicly available GEO (Gene Expression Omnibus) datasets:
- **GSE21653**: Sabatier et al., Clin Cancer Res 2011
- **GSE20685**: Kao et al., BMC Genomics 2011  
- **GSE31448**: Minn et al., PNAS 2005
- **GSE58812**: Maire et al., Oncotarget 2013

**Note**: Raw GEO data files are NOT included in this repository. Users can download them directly from NCBI GEO database using the accession numbers above.

## Requirements

### Python packages:
```bash
pip install pandas numpy scipy matplotlib seaborn openpyxl
```

### Python version:
- Python 3.7+

## Usage

### Generate Figure 1 (H-Score Distribution):
```bash
cd scripts
python figure1_hscore_distribution.py
```

**Input**: `../data/TNBC_HER2_Luminal-SOST.xlsx`  
**Output**: 
- `Figure_UnifiedCutoff_Clean.png` (main 4-panel figure)
- `Figure_SubtypeDetails_Clean.png` (supplementary 3-panel figure)

### Generate Figure 2 (SOST-MKI67 Correlation):
```bash
cd scripts
python figure2_sost_mki67_correlation.py
```

**Input**: `../data/SOST_MKI67_Unique_Samples.csv`  
**Output**:
- `Figure_SOST_MKI67_Correlation.png` (high-resolution PNG)
- `Figure_SOST_MKI67_Correlation.pdf` (vector PDF)
- `SOST_MKI67_Validation_Complete.xlsx` (detailed statistics)

## Data Files Included

1. **TNBC_HER2_Luminal-SOST.xlsx** (12 KB)
   - H-Score measurements from IHC analysis
   - Three subtypes: TNBC, HER2+, Luminal
   - Clinical cohort data (not from GEO)

2. **SOST_MKI67_Unique_Samples.csv** (33 KB)
   - Processed expression data from 4 GEO datasets
   - 798 unique TNBC patient samples
   - SOST and MKI67 mRNA expression values

## Citation

If you use this code or data, please cite:

**Zenodo DOI**: 
```
Yang, X. (2026). Code and Data for SOST Analysis in Triple-Negative Breast Cancer (Version v1.0.0) [Software]. Zenodo. https://doi.org/10.5281/zenodo.18752090
```

**BibTeX**:
```bibtex
@software{yang_2026_sost_tnbc,
  author       = {Yang, X.},
  title        = {{Code and Data for SOST Analysis in Triple-Negative Breast Cancer}},
  month        = feb,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.18752090},
  url          = {https://doi.org/10.5281/zenodo.18752090}
}
```

## Contact

For questions or issues, please contact:
[Your contact information]

## License

[Add appropriate license]
