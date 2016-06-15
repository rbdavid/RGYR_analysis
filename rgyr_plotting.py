#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# USAGE:

# PREAMBLE:

from fn_plotting import *
from sel_list import *

stdev = np.std
sqrt = np.sqrt
nullfmt = NullFormatter()

dat1 = sys.argv[1]  
system1 = sys.argv[2]

# ----------------------------------------
# MAIN PROGRAM:

datalist1 = np.loadtxt(dat1)

nSteps = len(datalist1[:,0])

time = np.zeros(nSteps)

for i in range(nSteps):
	time[i] = i*0.002		# units of time in ns; each frame is separated by 0.002 ns 

for i in range(len(sel)):
	system = selection[i][0]
	num = i

	scat_hist(time[:], datalist1[:,i], 'k', 'Time', 'RGYR ($\AA$)', '%02d.%s.%s' %(num, system1, system), 'RGYR',xunits='ns',yunits='$\AA$',)

