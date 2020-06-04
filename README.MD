## Introduction

This repository contains code and supplementary materials for paper named "xxx". 

Jose Maria Zamora-Fuentes, Jesus Espinal-Enriquez, Enrique Hernandez-Lemus

# Pre-requisites

Considerations:

- R (3.6.3)
- Python 3

Pre-requisites to run scripts in theses paheses are obtained with:

`$ Rscript pkgs-requiremnts.R`


# Data Adquisition, Control Quality and Normalization

These three phases of the process are performed by next R script:

`$ Rscript RNAseq-KIRC.R`

The expression data for control and each stage are saved on:

`$ ls pipeline/TCGA/Outs/`


# Mutual Information

You can use repository of parallel mulitcore [ARACNe]() 