data = np.loadtxt('hsindex.csv', dtype='str', delimiter=',')
stocks = pd.Series(data[:,0])
s = stocks.unique()
f=open('./hsi_edge.gml', 'w+')
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
f.close()
