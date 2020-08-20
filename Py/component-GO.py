#! pip install python-igraph
import glob, sys
import pandas as pd
import igraph as ig
from gprofiler import GProfiler

# outDir = "Results/intersections/"
# fname = "Results/intersections/inter-ctrl-stages.tsv"
fname = sys.argv[1]
oname1 = fname.split('.')[0] + "-components.go.txt"
oname2 = fname.split('.')[0] + "-components.ids.txt"
print(oname1)
print(oname2)

# df = pd.read_csv(fname, sep='\t', header=None, names=['src', 'dst'])
df = pd.read_csv(fname, sep='\t')
# print(df)
g = ig.Graph.TupleList(df.itertuples(index=False), 
	directed=False, weights=True)

# print(g.vcount(), g.ecount())

components = g.components()
# print(components)
print("Number of Components:", len(components))

df = pd.DataFrame({'gene':g.vs['name'],'components':components.membership })
# Order by size of component
# df = df.iloc[df.groupby('components').components.transform('size').argsort(kind='mergesort')]
# df = df.iloc[::-1]
valuec = df['components'].value_counts()
biggest = valuec.unique()[0]                          # Corta el valor con mas cuentas
values = valuec[(valuec >= biggest) | (valuec >= 10)] # Values of components filtered
order = values.index.tolist()
df = df[df['components'].isin(order)]
df = df.set_index('components')
df = df.loc[order].reset_index()
print("Component id - Number of Genes")
print(valuec)


#! Enrichment by GO
gp = GProfiler(return_dataframe=True)
enrich_components = pd.DataFrame()
print("Component id - shape")
for name, group in df.groupby('components', sort=False):
	print(name,group.shape)
	s = gp.profile(organism = 'hsapiens', query = group.gene.tolist())
	s['component'] = name
	enrich_components = enrich_components.append(s)
# print(enrich_components)

#! OUTPUT
# oname = fname.split("/")[-1].split(".")[0] 
enrich_components.to_csv(oname1, sep="\t", index=False)
# df.to_csv(outDir + oname + "-components.tsv", sep="\t",index=False)
df.to_csv(oname2, sep="\t",index=False)


