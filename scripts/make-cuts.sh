#!/bin/bash


d="/datos/ot/biodata/stages/kirc/mi"
grps=("ctrl" "stagei" "stageii" "stageiii" "stageiv")
cutsdir="Results/cuts-mi"

for i in $(seq 2 6)
do
	n=$(( 10 ** i ))
	nstr=$(numfmt --format="%.f" --to=si ${n})
	echo "Making cuts for $nstr"
	dout="${cutsdir}/${nstr}"
	mkdir -p $dout
	for g in ${grps[@]}; do
  		head -n ${n} ${d}/kirc-${g}.sort > $dout/kirc-${g}-${nstr}.txt
	done
	echo "Making Intersections files"
	python Py/intersections.py ${dout} ${dout}/intersections
	echo "Making Heatmaps"
	python Py/make-heatmaps.py ${dout}/intersections $n
done