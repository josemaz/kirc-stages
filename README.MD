# Introduction

This repository contains code and supplementary materials for paper named "xxx". 

Jose Maria Zamora-Fuentes, Jesus Espinal-Enriquez, Enrique Hernandez-Lemus

## Pre-requisites

Considerations:

- R (3.6.3)
- Python 3

Pre-requisites to run scripts in theses paheses are obtained with:

`$ Rscript pkgs-requiremnts.R`


## 01 - Data Adquisition, Control Quality and Normalization

These three phases of the process are performed by next R script:

`$ Rscript RNAseq-KIRC.R`

The expression data for control and each stage are saved on:

`$ ls pipeline/TCGA/Outs/`

Plots for pre Normalization Quality Control are saved on:

`$ ls pipeline/TCGA/Plots/QC_PRE/`

Plots for post Normalization Quality Control are saved on:

`$ ls pipeline/TCGA/Plots/QC_POST/`


## 02 - Mutual Information

You can use repository of parallel mulitcore [ARACNe](https://github.com/CSB-IG/ARACNE-multicore)

From ARACNe2 output writing out MI network cuts of 10k interactions into `Results`  directory in this repository:

`$ cp kirc-ctrl-10k.tsv kirc-stagei-10k.tsv kirc-stageii-10k.tsv kirc-stageiii-10k.tsv kirc-stageiv-10k.tsv Results/MI/`

## 03 - Differential Expression (DEG)

Script to write out DEG in a *tsv* file:

`$ Rscript DEG.R`

Output for each stage is saved on:

`$ ls Results/DEG/`

This output contains volcano plot in html format.

# 04 - Networks Analysis

Script to generate intersections of stages and control.

`$ python Py/intersections.py`

Intersections are saved on:

`$ ls Results/intersections`

To generate heatmaps intersection plots:

`$ python Py/make-heatmaps.py`

Plots are saved on:

`$ ls Plots`

