#! pip install python-igraph
import glob, sys
import pandas as pd
import igraph as ig
from gprofiler import GProfiler

# outDir = "Results/intersections/"
# fname = "Results/intersections/inter-ctrl-stages.tsv"
fname = sys.argv[1]
oname1 = fname.split('.')[0] + "-communities.go.txt"
oname2 = fname.split('.')[0] + "-communities.id.txt"
print(oname1)
print(oname2)

# df = pd.read_csv(fname, sep='\t', header=None, names=['src', 'dst'])
df = pd.read_csv(fname, sep='\t')
# print(df)
g = ig.Graph.TupleList(df.itertuples(index=False), 
	directed=False, weights=True)
# print(g.vcount(), g.ecount())

community = g.community_infomap()
print("Number of Communities:", len(community))

df = pd.DataFrame({'gene':g.vs['name'],'community':community.membership })
# Order by size of communities
valuec = df['community'].value_counts()
biggest = valuec.unique()[0]                          # Corta el valor con mas cuentas
values = valuec[(valuec >= biggest) | (valuec >= 10)] # Values of communities filtered
order = values.index.tolist()
df = df[df['community'].isin(order)]
df = df.set_index('community')
df = df.loc[order].reset_index()
# print("community id - Number of Genes")
# print(valuec)


#! Enrichment by GO
gp = GProfiler(return_dataframe=True)
enrich_communities = pd.DataFrame()
print("Community id - Number of nodes")
for name, group in df.groupby('community', sort=False):
	print(name,group.shape[0])
	s = gp.profile(organism = 'hsapiens', query = group.gene.tolist())
	s['community'] = name
	enrich_communities = enrich_communities.append(s)
# print(enrich_components)

#! OUTPUT
enrich_communities.to_csv(oname1, sep="\t", index=False)
df.to_csv(oname2, sep="\t",index=False)


