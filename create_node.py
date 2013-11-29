import pandas as pd
import numpy as np

data = np.loadtxt('hsindex.csv', dtype='str', delimiter=',')
pdata = data[:,2:4]
s = pd.Series(pdata[:,0])
l = [list(t) for t in set(tuple(element) for element in pdata)]
f=open('./hsi_node.gml', 'w+')
for x in l:
    f.writelines('node [\n')
    f.writelines('    id ' + x[0] + '\n')
    f.writelines('    label "' + x[1] + '"\n')    
    f.writelines(']\n')
f.close()
