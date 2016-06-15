#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# USAGE:
# ./rgyr.py system_descripter pdb_file traj_file 

# calculate radius of gyration for a solute;  

# PREAMBLE:

import numpy as np
import MDAnalysis
import sys
from sel_list import *

system = sys.argv[1]
pdb = sys.argv[2]
traj = sys.argv[3]


# SUBROUTINES:

# MAIN PROGRAM:

u = MDAnalysis.Universe('%s' %(pdb), '%s' %(traj))

sel = ['']*len(selection)
for i in range(len(selection)):
	sel[i] = u.select_atoms(selection[i][1])

important = u.select_atoms('not (resname WAT or resname Na+ or resname Cl-)')
protein = u.select_atoms('protein')
rest =  u.select_atoms('not (resname WAT or resname Na+ or resname Cl- or protein)')

num_res = len(rest.residues)

out = open('%s.rgyr.dat' %(system), 'w')

for ts in u.trajectory:
	if num_res != 0:
		dimensions = u.dimensions[:3]
		
		important.translate(-protein.center_of_mass())

		# Fix the wrapping issues
		for i in range(num_res):
			COM = np.zeros(3)
			# Calculate the COM of residues;
			COM = rest.residues[i].center_of_mass()
			# CALCULATING AND APPLYING THE TRANSLATIONAL MATRIX TO RESIDUE i
			t = wrapping(COM,dimensions)
			rest.residues[i].atoms.translate(t)
		
	for i in range(len(selection)):
		rgyr = sel[i].radius_of_gyration()
		out.write('%10.6f    ' %(rgyr))
	out.write('\n')

out.close()

