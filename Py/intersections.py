# Este script calcula las intersecciones entre todas las redes
# ubicadas en: Results/Kidney/MI 
# Los archivos tienen la notacion: Kidney-IM-Control-10k.txt
# Ejecucion en raiz: python Py/nets/intersecciones.py

import numpy as np
import pandas as pd
import sys, os, glob
from itertools import combinations
from pathlib import Path

wd = os.getcwd()
imDir = "Results/MI/"
imDir = sys.argv[1]
os.chdir(imDir)
# df = pd.DataFrame(columns=['Tissue', 'Valor', 'Stage', 'cuts'])
df = pd.DataFrame(columns=['Tissue', 'Stage', 'cuts'])
i = 0
for fname in glob.glob('*.txt'):
	df.loc[i] = fname.split('.')[0].split('-')
	i = i + 1
cuts = df.groupby(['cuts'])
os.chdir(wd)
print(df)

outdir="Results/intersections/"
outdir=sys.argv[2]
path = Path(outdir).mkdir(parents=True, exist_ok=True)
for gname, g in cuts:
	print(gname)
	etapas = g.Stage.values
	t = g.Tissue.unique()[0]
	# v = g.Valor.unique()[0]
	c = g.cuts.unique()[0]
	etapas.sort()
	print("\n", "SORT:", etapas, "\n")
	for pair in list(combinations(etapas, 2)):
		p1 = pair[0]
		p2 = pair[1]
		# fname1 = t + "-" + v + "-" + p1 + "-" + c  + ".txt"
		fname1 = t + "-" + p1 + "-" + c  + ".txt"
		# fname2 = t + "-" + v + "-" + p2 + "-" + c  + ".txt"
		fname2 = t + "-" + p2 + "-" + c  + ".txt"
		f1 = np.genfromtxt(imDir + "/" + fname1, delimiter='\t', dtype='unicode') #Unicode to read names
		f2 = np.genfromtxt(imDir + "/" + fname2, delimiter='\t', dtype='unicode') #Unicode to read names

		edge1 = set([(x[0], x[1]) for x in f1])
		edge2 = set([(x[0], x[1]) for x in f2])

		edges_intersec = edge1 & edge2
		nodos_intersec = set(np.array(list(edges_intersec)).reshape(-1))
		print(len(edges_intersec),len(nodos_intersec))

		edges_diff_file2 = (edge2 - edge1)
		nodos_diff_file2 = set(np.array(list(edges_diff_file2)).reshape(-1))
		print(len(edges_diff_file2),len(nodos_diff_file2))

		edges_diff_file1 = (edge1 - edge2)
		nodos_diff_file1 = set(np.array(list(edges_diff_file1)).reshape(-1))
		print(len(edges_diff_file1),len(nodos_diff_file1))

		out = outdir + "/" +  "inter-" + t + "-" + p1 + "-" + p2 + "-" + c + ".txt"
		open(out, 'w').write('\n'.join('%s %s' % x for x in edges_intersec))
		out = outdir + "/" +  "diff-" + t + "-" + p1 + "-" + p2 + "-" + c + ".txt"
		open(out, 'w').write('\n'.join('%s %s' % x for x in edges_diff_file2))
		out = outdir + "/" +  "diff-" + t + "-" + p2 + "-" + p1 + "-" + c + ".txt"
		open(out, 'w').write('\n'.join('%s %s' % x for x in edges_diff_file1))

		print("\t", fname1, fname2)





