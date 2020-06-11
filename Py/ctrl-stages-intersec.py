#! Codiugo para hacer el heatmap con las interacciones en las
#! de las intersecciones y las diferencias
import glob, os, sys
from itertools import combinations
from os import path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dirnets = "Results/intersections/"
stages = ["ctrl", "stagei", "stageii", "stageiii", "stageiv"]


fname = "inter-kirc-stagei-stageii-10k.txt"
f1 = np.genfromtxt(dirnets + fname, delimiter=' ', dtype='unicode')
edge1 = set([(x[0], x[1]) for x in f1])

fname = "inter-kirc-stageii-stageiii-10k.txt"
f2 = np.genfromtxt(dirnets + fname, delimiter=' ', dtype='unicode')
edge2 = set([(x[0], x[1]) for x in f2])

edges_intersec = edge1 & edge2
print("Etapa (1&2) & Etapa (2&3): ", len(edges_intersec))

fname = "inter-kirc-stageiii-stageiv-10k.txt"
f2 = np.genfromtxt(dirnets + fname, delimiter=' ', dtype='unicode')
edge2 = set([(x[0], x[1]) for x in f2])

edges_intersec = edges_intersec & edge2
print("Etapa (1&2) & Etapa (2&3) & Etapa (3&4): ", len(edges_intersec))


fname = "inter-kirc-stageii-stagei-10k.txt"

dirnets = "Results/MI/"
mi = "kirc-ctrl-10k.txt"
f2 = np.genfromtxt(dirnets + mi, delimiter='\t', dtype='unicode')
edge2 = set([(x[0], x[1]) for x in f2])
print(len(edge2))

edges_intersec = edges_intersec & edge2
print("ctrl & Etapas (1&2&3&4): ", len(edges_intersec))

df = pd.DataFrame(list(edges_intersec), columns =['source', 'target'])
fname = "biomart-20200526.txt"
mart = pd.read_csv(fname, sep='\t', dtype={'Gene name': str})
print(mart.dtypes)

df.to_csv('Results/intersections/inter-ctrl-stages.tsv', header=None, index = False, sep="\t")

source = pd.merge(df, mart, how="left", left_on="source", right_on="Gene stable ID")
target = pd.merge(df, mart, how="left", left_on="target", right_on="Gene stable ID")
# print(source)
# print(target)

source.to_csv('Results/intersections/source-inter-ctrl-stages.tsv', index = False, sep="\t")
target.to_csv('Results/intersections/target-inter-ctrl-stages.tsv', index = False, sep="\t")

