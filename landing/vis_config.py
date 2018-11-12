# set an alias e.g., vis='visit -nosplash -s ~/path/to/vis_config.py'

from glob import glob

dbs = glob('*.nek5000')

if len(dbs) == 0: dbs.append('$HOME/Developer/Templates/t.nek5000')

db = sorted(dbs,key=os.path.getmtime)[-1] 
OpenDatabase(db)

md = GetMetaData(db)

ifheat = False
iplot = (1,3)

for i in xrange(md.GetNumScalars()): # check if temperature exists
    if md.GetScalars(i).name == 'temperature': ifheat = True; iplot = (1,2,4)

# Pseudocolor

p = PseudocolorAttributes()
p.colorTableName = "hot_desaturated"

SetDefaultPlotOptions(p)

AddPlot('Pseudocolor','velocity_mag')
AddPlot('Pseudocolor','pressure')

if ifheat: AddPlot('Pseudocolor','temperature')

# Subset

AddPlot('Subset','blocks')

s = SubsetAttributes()
s.colorType = 0
s.wireframe = 1

SetPlotOptions(s)

# Mesh

AddPlot('Mesh','mesh')

# Hide Plots

SetActivePlots(iplot)
HideActivePlots()
DrawPlots()
SetActivePlots(0)
