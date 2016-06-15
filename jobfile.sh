#!/bin/bash

# USAGE:
# ./jobfile.sh 

NPRODS=150

function rgyr {
	./rgyr.py Amber.ssrna_atp.prod.$1 ../truncated.pdb ../Trajectories/production.$1/production.$1.dcd
	cat Amber.ssrna_atp.prod.$1.rgyr.dat >> ssrna_atp.rgyr.dat
}

for (( prod=1; prod<=$NPRODS; prod++))
do
	rgyr $prod
done

