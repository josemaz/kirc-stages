# Introduction

This repository contains code and supplementary materials for paper: *Gene expression and co-expression networks are strongly altered through stages in clear cell renal carcinoma*. 

Jose Maria Zamora-Fuentes, Jesus Espinal-Enriquez, Enrique Hernandez-Lemus



## Pre-requisites

Considerations:

- R (3.6.3)
- Python 3

Pre-requisites to run scripts in theses paheses are obtained with:

`$ Rscript pkgs-requiremnts.R`

Python Pre-requisites (optional):

`$ bash install-miniconda.sh`



## Directory structure

- */pipeline* : Files to fetch data of GDC. Make preQC, postQC and normalization
- */Results/DEG* : Output of Differential Expression of genes (DEG)
- */Results/Expression* : Clean Expression Matrix (Genes x Samples)
- */Results/MI* : 10000 biggest Mutual Information pairs of genes
- */Extras* : Data, Plots and Utils for this paper.



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



## 04 - Networks Analysis

### Intersections between all cohorts

Script to generate intersection for each cohort:

`$ python Py/intersections.py`

Intersections are saved on:

`$ ls Results/intersections`

To generate heatmaps intersection plots:

`$ python Py/make-heatmaps.py`

Plots are saved on:

`$ ls Plots`

### Intersections only between control and stages

To generate intersections:

`$ python Py/ctrl-stages-intersec.py`

Output are a network saved on:

`$ ls Results/intersections/inter-ctrl-stages.tsv`

and annotation for every MI interaction in:

`$ ls Results/intersections/source-inter-ctrl-stages.tsv`

`$ ls Results/intersections/target-inter-ctrl-stages.tsv`

### Network Enrichment

To get enrichment by component:

`$ python Py/component-GO.py`

Output gene-idcomponent:

`$ ls Results/intersections/inter-ctrl-stages-components.tsv`

and annotation enrichement by component is saved:

`$ ls Results/intersections/inter-ctrl-stages-enrich.tsv`


### DEG Contrast analysis




