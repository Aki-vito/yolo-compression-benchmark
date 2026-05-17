# YOLO Compression Benchmark
 
Benchmarking YOLO11n instance segmentation performance across image compression formats and quality levels on the Cityscapes dataset.
 
## What this is
 
This repository contains the code and results from my undergraduate thesis at Yıldız Technical University (Industrial Engineering, 2026).
 
**The core question:** How does lossy image compression affect YOLO instance segmentation accuracy across formats and quality levels?
 
**Formats evaluated:** JPEG · WebP · HEIC  
**Quality levels:** 90, 75, 50, 30, 15, 10, 5 (per format)  
**Model:** YOLO11n-seg (Ultralytics)  
**Dataset:** Cityscapes (instance segmentation, urban driving)  
**Baseline:** PNG (lossless), Mask mAP@50-95 = 0.366, Average file size = 2306.87 KB  
**Primary metric:** Mask mAP@50-95
 
---
 
## Metrics
 
Four metrics were developed to quantify the storage-vs-accuracy tradeoff:
 
**Compression Score (CS)**
```
CS = Size Reduction % − mAP Drop %
```
Net benefit of compression relative to the uncompressed baseline.
 
**Weighted Compression Score (WCS)**
```
WCS = Size Reduction % − λ × mAP Drop %
```
Configurable lambda for deployment contexts where storage or accuracy is prioritized differently. At λ=1, WCS reduces to CS.
 
**Efficiency Ratio (ER)**
```
ER = Size Reduction % / mAP Drop %
```
Storage saved per unit of accuracy lost. Undefined when mAP drop is zero.
 
**Marginal Efficiency (ME)**
```
ME = ΔSize Reduction % / ΔmAP Drop %   (between adjacent quality levels)
```
Rate of storage gain relative to accuracy cost when moving one step down the quality ladder.
 
---
 
## Results
 
### Mask mAP@50-95 by format and quality
 
| Quality | JPEG  | WebP  | HEIC  |
|---------|-------|-------|-------|
| 90      | 0.359 | 0.348 | 0.365 |
| 75      | 0.322 | 0.304 | 0.361 |
| 50      | 0.236 | 0.272 | 0.342 |
| 30      | 0.138 | 0.235 | 0.228 |
| 15      | 0.031 | 0.197 | 0.128 |
| 10      | 0.012 | 0.183 | 0.073 |
| 5       | 0.002 | 0.139 | 0.048 |
 
Baseline (PNG): 0.366
 
### Average file size (KB) by format and quality
 
| Quality | JPEG    | WebP   | HEIC    |
|---------|---------|--------|---------|
| 90      | 345.702 | 153.60 | 1024.00 |
| 75      | 143.155 | 63.488 | 607.437 |
| 50      | 89.293  | 45.261 | 94.413  |
| 30      | 62.874  | 33.587 | 27.648  |
| 15      | 38.707  | 25.190 | 12.083  |
| 10      | 29.491  | 22.323 | 8.397   |
| 5       | 19.866  | 19.046 | 6.758   |
 
Baseline (PNG): 2306.87 KB
 
### Size Reduction (%) by format and quality
 
| Quality | JPEG  | WebP  | HEIC  |
|---------|-------|-------|-------|
| 90      | 85.01 | 93.34 | 55.61 |
| 75      | 93.79 | 97.25 | 73.67 |
| 50      | 96.13 | 98.04 | 95.91 |
| 30      | 97.27 | 98.54 | 98.80 |
| 15      | 98.32 | 98.91 | 99.48 |
| 10      | 98.72 | 99.03 | 99.64 |
| 5       | 99.14 | 99.17 | 99.71 |
 
### Compression Score (CS) by format and quality
 
| Quality | JPEG   | WebP  | HEIC  |
|---------|--------|-------|-------|
| 90      | 83.00  | 88.44 | 55.24 |
| 75      | 81.75  | 80.35 | 72.33 |
| 50      | 60.72  | 72.23 | 89.26 |
| 30      | 35.08  | 62.74 | 61.06 |
| 15      | 6.76   | 52.79 | 34.41 |
| 10      | 2.07   | 49.05 | 19.47 |
| 5       | −0.38  | 37.23 | 12.90 |
 
### Efficiency Ratio (ER) by format and quality
 
| Quality | JPEG  | WebP | HEIC   |
|---------|-------|------|--------|
| 90      | 42.29 | 19.05 | 150.30 |
| 75      | —     | —    | 54.98  |
| 50      | —     | —    | 14.42  |
| 30      | —     | —    | —      |
 
Note: ER values below 1.0 are omitted for brevity; full values available in `results/results.csv`.
 
### Marginal Efficiency (ME) across quality transitions
 
| Transition | JPEG | WebP | HEIC  |
|------------|------|------|-------|
| q90 → q75  | 0.88 | 0.33 | 18.62 |
| q75 → q50  | 0.10 | 0.09 | 4.19  |
| q50 → q30  | 0.04 | 0.05 | 0.09  |
| q30 → q15  | 0.04 | 0.04 | 0.02  |
| q15 → q10  | 0.08 | 0.03 | 0.01  |
| q10 → q5   | 0.15 | 0.01 | 0.01  |
 
ME > 1 indicates an efficient quality step (at λ=1). ME > λ for other thresholds.
 
### Optimal format per mAP threshold (Table 6)
 
| Minimum mAP | Optimal Format | Quality | Size Reduction (%) | mAP Drop (%) |
|-------------|----------------|---------|-------------------|--------------|
| 0.36        | HEIC           | q75     | 73.67             | 1.34         |
| 0.35        | JPEG           | q90     | 85.01             | 2.01         |
| 0.34        | HEIC           | q50     | 95.91             | 6.65         |
| 0.30        | WebP           | q75     | 97.25             | 16.90        |
| 0.25        | WebP           | q50     | 98.04             | 25.81        |
 
---
 
## Stack
 
- Python 3.x
- [Ultralytics](https://github.com/ultralytics/ultralytics) — YOLO11n-seg training and inference
- PyTorch
- OpenCV, Pillow — image compression pipeline
- Pandas, NumPy — metrics computation
- Matplotlib — plots
Environment: Linux (Fedora), Neovim, tmux, IPython
