#! Codiugo para hacer el heatmap con las interacciones en las
#! de las intersecciones y las diferencias
import glob, os, sys
from itertools import combinations
from os import path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

dirnets = "Results/intersections/"
stages = ["ctrl", "stagei", "stageii", "stageiii", "stageiv"]


df1 = pd.DataFrame(columns = stages, index=stages)
for i in combinations(stages, 2):
	# inter-kirc-stageii-stageiv-10k.txt
	fname = "inter-kirc-" + i[0] + "-" + i[1] +"-10k.txt"
	fname = dirnets + "/" + fname
	fname_rev = "inter-kirc-" + i[1] + "-" + i[0] +"-10k.txt"
	fname_rev = dirnets + "/" + fname_rev
	if path.exists(fname):
		# print("File exist: ", fname)
		f = fname
	elif path.exists(fname_rev):
		# print("File reverse exist: ", fname_rev)
		f = fname_rev
	else:
		print("ERROR in tuple: ", i)
		sys.exit(15);
	df1.at[i[0],i[1]] = sum(1 for line in open(f))
	df1.at[i[1],i[0]] = sum(1 for line in open(f))
	# print(i)

df1.fillna(0, inplace = True) 
print(df1)
# ax = sns.heatmap(df, cmap='coolwarm', annot=True, robust=True, fmt="d", 
# 	yticklabels=stages, cbar=False)
# ax.xaxis.set_ticks_position('top')
# plt.show()

df2 = pd.DataFrame(columns = stages, index=stages)
for i in combinations(stages, 2):
	fname = "diff-kirc-" + i[0] + "-" + i[1] +"-10k.txt"
	fname = dirnets + "/" + fname
	fname_rev = "diff-kirc-" + i[1] + "-" + i[0] +"-10k.txt"
	fname_rev = dirnets + "/" + fname_rev
	if not path.exists(fname):
		print("ERROR in tuple: ", i)
		sys.exit(15);
	if not path.exists(fname_rev):
		print("ERROR in tuple: ", i[::-1])
		sys.exit(15);
	df2.at[i[0],i[1]] = sum(1 for line in open(fname))
	df2.at[i[1],i[0]] = sum(1 for line in open(fname_rev))
	# print(i)

df2.fillna(0, inplace = True) 
print(df2)

outdir="Plots"
path = Path(outdir).mkdir(parents=True, exist_ok=True)

fig, (ax0,ax1) = plt.subplots(1, 2, sharex=True, sharey=True)
fig.set_size_inches(8.53, 5.5)
ax0 = sns.heatmap(df1, cmap='coolwarm', annot=True, robust=True, fmt="d", 
	yticklabels=stages, cbar=False, ax=ax0)
ax0.xaxis.set_ticks_position('top')
ax0.set_title('intersecciones')
ax1 = sns.heatmap(df2, cmap='coolwarm', annot=True, robust=True, fmt="d", 
	yticklabels=stages, cbar=False, ax=ax1)
ax1.xaxis.set_ticks_position('top')
ax1.set_title('diferencias')
fig.suptitle('Interacciones entre etapas de cancer de rinon',fontsize=12)
plt.subplots_adjust(top=0.85)
plt.savefig(outdir + "/interacciones-etapas.png",dpi=300)






