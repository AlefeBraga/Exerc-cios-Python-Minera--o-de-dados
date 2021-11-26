Xstr =input('Vetor X:\n')
XSTRList = Xstr.split ()

X = [int(i) for i in XSTRList ]

Ystr =input('Vetor Y:\n')
YSTRList = Ystr.split ()

Y = [int(i) for i in YSTRList ]
ProdutoEscalar = 0

for i in range(3):
    ProdutoEscalar += X[i]*Y[i]

ProdutoEscalar = list()
ProdutoEscalar .append( X[1]*Y[2] - X[2]*Y[1] )
ProdutoEscalar .append( X[0]*Y[2] - X[2]*Y[0] )
ProdutoEscalar .append( X[0]*Y[1] - X[1]*Y[0] )

print('Produto escalar =', ProdutoEscalar )
print('Produto vetorial =', ProdutoEscalar )