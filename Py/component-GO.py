#! pip install python-igraph
import glob, sys
import pandas as pd
import igraph as ig
from gprofiler import GProfiler

outDir = "Results/intersections/"
fname = "Results/intersections/inter-ctrl-stages.tsv"
print(fname)

df = pd.read_csv(fname, sep='\t', header=None, names=['src', 'dst'])
print(df)
g = ig.Graph.TupleList(df.itertuples(index=False), 
	directed=False, weights=True)

print(g.vcount(), g.ecount())

components = g.components()

df = pd.DataFrame({'gene':g.vs['name'],'components':components.membership })
# Order by size of component
df = df.iloc[df.groupby('components').components.transform('size').argsort(kind='mergesort')]
df = df.iloc[::-1]

#! Enrichment by GO
gp = GProfiler(return_dataframe=True)
enrich_components = pd.DataFrame()
for name, group in df.groupby('components', sort=False):
	print(name,group.shape)
	s = gp.profile(organism = 'hsapiens', query = group.gene.tolist())
	s['component'] = name
	enrich_components = enrich_components.append(s)
print(enrich_components)

oname = fname.split("/")[-1].split(".")[0] 
enrich_components.to_csv(outDir + oname + "-enrich.tsv", sep="\t",index=False)
df.to_csv(outDir + oname + "-components.tsv", sep="\t",index=False)

