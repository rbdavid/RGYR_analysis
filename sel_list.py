
selection = []
selection.append(['prot','protein'])
selection.append(['prot-12','protein and not (resid 0:12)'])
selection.append(['ssRNA','nucleic or (resname A5 or resname A3 or resname U5) and not (resname atp or resname adp)'])
selection.append(['ATP','resname atp'])

