# File Correspondence Guide

## 📊 Figure 1: H-Score Distribution (TNBC/HER2/Luminal)

**对应关系**:
- **图片**: `figures/figure1_hscore_distribution.png`
- **代码**: `scripts/figure1_hscore_distribution.py`
- **数据**: `data/TNBC_HER2_Luminal-SOST.xlsx`

**说明**: 
- 展示三种乳腺癌亚型的H-Score分布
- TNBC (n=100), HER2+ (n=94), Luminal (n=99)
- 统一cutoff = 51.80 (Q3)

---

## 📊 Figure 2: SOST-MKI67 Correlation in TNBC

**对应关系**:
- **图片**: `figures/figure2_sost_mki67_correlation.png`
- **代码**: `scripts/figure2_sost_mki67_correlation.py`
- **数据**: `data/SOST_MKI67_Unique_Samples.csv`

**说明**:
- SOST和MKI67在TNBC中的相关性
- Pooled analysis, n=798患者
- 4个独立GEO数据集 (GSE21653, GSE20685, GSE31448, GSE58812)
- Pearson r = 0.571, p < 0.0001

---

## 📁 完整文件结构

```
github/
├── data/                                    (2 files)
│   ├── TNBC_HER2_Luminal-SOST.xlsx         → Figure 1 数据
│   └── SOST_MKI67_Unique_Samples.csv       → Figure 2 数据
│
├── figures/                                 (2 files)
│   ├── figure1_hscore_distribution.png     → Figure 1 图片
│   └── figure2_sost_mki67_correlation.png  → Figure 2 图片
│
├── scripts/                                 (2 files)
│   ├── figure1_hscore_distribution.py      → Figure 1 生成代码
│   └── figure2_sost_mki67_correlation.py   → Figure 2 生成代码
│
├── README.md                                (使用说明)
└── FILE_CORRESPONDENCE.md                   (本文件)
```

**总计**: 2张图 + 2个代码文件 + 2个数据文件 = 完美对应 ✓
