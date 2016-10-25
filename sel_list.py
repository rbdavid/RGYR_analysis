
selection = []
selection.append(['prot','protein'])
selection.append(['prot-12','protein and not (resid 0:12)'])
selection.append(['ssRNA','nucleic or (resname A5 A3 U5) and not (resname atp adp)'])
selection.append(['ATP','resname atp'])
#selection.append(['ADP','resname adp'])

