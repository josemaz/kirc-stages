#!/bin/bash

. "`dirname \"$0\"`"/bash_colors.sh

d="/datos/ot/biodata/stages/kirc/mi"
# d="Results/MI"
grps=("ctrl" "stagei" "stageii" "stageiii" "stageiv")
cutsdir="Results/cuts-mi"


for i in $(seq 2 6)
do
	n=$(( 10 ** i ))
	nstr=$(numfmt --format="%.f" --to=si ${n}) # Ex. 1K,10K, 1M
	clr_bold clr_green "Making cuts for $nstr"
	dout="${cutsdir}/${nstr}"
	mkdir -p $dout
	for g in ${grps[@]}; do
		[[ ! -f ${d}/kirc-${g}.sort ]] \
			&& echo "dosen't exist: ${d}/kirc-${g}.sort" && exit 15
  		head -n ${n} ${d}/kirc-${g}.sort > $dout/kirc-${g}-${nstr}.txt
	done
	clr_bold clr_green"Making Intersections files"
	python Py/intersections.py ${dout} ${dout}/intersections
	clr_bold clr_green "Making Heatmaps"
	python Py/make-heatmaps.py ${dout}/intersections $n
	clr_bold clr_green "Making Venn Diagrams"
	Rscript R/make-venn-intersec.R $nstr
	clr_bold clr_green "Making Enrichment"
	python Py/component-GO.py Results/cuts-mi/$nstr/inter-all-groups-$nstr.tsv
	python Py/component-GO.py Results/cuts-mi/$nstr/inter-only-stages-$nstr.tsv
done
rm -rf Plots/*.log