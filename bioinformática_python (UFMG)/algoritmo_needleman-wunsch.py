v = ['*', 'A', 'T', 'C', 'G', 'T', 'A', 'C']
w = ['*', 'A', 'T', 'G', 'T', 'T', 'A', 'T']

def lcs(v, w):
    pontuacao = []
    ponteiros = []
    pontuacao = [0]*len(v)
    ponteiros = ['']*len(v)

    for i in range(0, len(w)):
        pontuacao[i] = [0]*len(v)
        ponteiros[i] = ['']*len(v)

    for i in range(0, len(w)):
        ponteiros[i][0] = '|'
    for j in range(0, len(v)):
        ponteiros[0][j] = '_'


    for i in range(0, len(w)):
        for j in range(0, len(v)):
            print(ponteiros[i][j], end='')
        print()


lcs(v,w)