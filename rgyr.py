#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# ----------------------------------------
# USAGE:
# ./rgyr.py system_descripter pdb_file traj_file  	# calculate radius of gyration for a solute;  

# ----------------------------------------
# PREAMBLE:

import numpy as np
import MDAnalysis
import sys
from sel_list import *
from distance_functions import *

pdb = sys.argv[1]
traj_loc = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])
system = sys.argv[5]

nSel = len(selection)
WRAPPED = True

flush = sys.stdout.flush

# ----------------------------------------
# FUNCTIONS:

def ffprint(string):
	print '%s' %(string)
	flush()

def summary():
	with open('%s.rgyr.summary' %(system),'w') as f:
		f.write('Using MDAnalysis version: %s\n' %(MDAnalysis.version.__version__))
		f.write('To recreate this analysis, run this line:\n')
		for i in range(len(sys.argv)):
			f.write('%s ' %(sys.argv[i]))
		f.write('\n\n')
		f.write('Output has been written to:\n')
		f.write('	%s.rgyr.dat\n' %(system))
		f.write('Number of steps analyzed: %d\n' %(nSteps))
		f.write('Atom selections analyzed:\n')
		for i in range(nSel):
			f.write('	Output Column %d   %s\n' %(i,selection[i][1]))
		### ADD TIMING FUNCTIONALITY...

# ----------------------------------------
# MAIN PROGRAM:

u = MDAnalysis.Universe('%s' %(pdb))

sel = ['']*nSel
for i in range(nSel):
	sel[i] = u.select_atoms(selection[i][1])

protein = u.select_atoms('protein')
important = u.select_atoms('not (resname WAT or resname Na+ or resname Cl-)')
rest =  u.select_atoms('not (resname WAT or resname Na+ or resname Cl- or protein)')
num_res = len(rest.residues)

out = open('%s.rgyr.dat' %(system), 'w')
while start <= end:
	u.load_new('%sproduction.%s/production.%s.dcd' %(traj_loc,start,start))
	nSteps += len(u.trajectory)
	for ts in u.trajectory:
		if num_res != 0 or WRAPPED != True:		# Fix the wrapping issues if told to...
			dims = u.dimensions[:3]
			dims_2 = dims/2.0
			important.translate(-protein.center_of_mass())
			for i in range(num_res):
				COM = rest.residues[i].center_of_mass()
				t = wrapping(COM,dims,dims_2)
				rest.residues[i].atoms.translate(t)
		for i in range(nSel):
			rgyr = sel[i].radius_of_gyration()
			out.write('%10.8f   ' %(rgyr))
		out.write('\n')
	start += 1
out.close()
summary()

