import pandas as pd
import numpy as np

data = np.loadtxt('hsindex.csv', dtype='str', delimiter=',')
pdata = data[:,2:4]
s = pd.Series(pdata[:,0])
l = [list(t) for t in set(tuple(element) for element in pdata)]
f=open('./hsi.gml', 'w+')
f.writelines('graph\n')
f.writelines('[\n')
f.writelines('directed 0\n')
for x in l:
    f.writelines('node [\n')
    f.writelines('    id ' + x[0] + '\n')
    f.writelines('    label "' + x[1] + '"\n')    
    f.writelines(']\n')

stocks = pd.Series(data[:,0])
s = stocks.unique()
for i in range(0, s.size-1):
    l = data[ np.where(data[:,0]==s[i]) ,1:3]
    for i in range(0, (l.size-1)/2):
        for j in range (i, (l.size-1)/2):
            if i != j:
                f.writelines('edge [' + '\n')
                f.writelines('     source ' + l[0][i][1] + '\n')
                f.writelines('     target ' + l[0][j][1] + '\n')
                f.writelines('     value ' + l[0][i][0] + '\n')
                f.writelines(']' + '\n')
f.writelines(']')
f.close()
