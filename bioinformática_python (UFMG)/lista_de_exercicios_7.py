# 1)

import math

Nx1 = 108.304
Nx2 = 107.670
Ny1 = 100.827
Ny2 = 101.359
Nz1 = 67.992
Nz2 = 70.074

CAx1 = 108.477
CAx2 = 108.477
CAy1 = 100.389
CAy2 = 100.389
CAz1 = 69.362
CAz2 = 69.362

Cx1 = 109.907
Cx2 = 109.513
Cy1 = 100.555
Cy2 = 101.011
Cz1 = 69.817
Cz2 = 68.450

Ox1 = 110.821
Ox2 = 110.667
Oy1 = 100.799
Oy2 = 100.572
Oz1 = 69.027
Oz2 = 68.425

somaN = ((Nx1 - Nx2)**2) + ((Ny1 - Ny2)**2) + ((Nz1 - Nz2)**2)
somaCA = ((CAx1 - CAx2)**2) + ((CAy1 - CAy2)**2) + ((CAz1 - CAz2)**2)
somaC = ((Cx1 - Cx2)**2) + ((Cy1 - Cy2)**2) + ((Cz1 - Cz2)**2)
somaO = ((Ox1 - Ox2)**2) + ((Oy1 - Oy2)**2) + ((Oz1 - Oz2)**2)

somaTotal = somaN + somaCA + somaC + somaO
quoc = somaTotal/4

rmsd = math.sqrt(quoc)
print(rmsd)


# 2)
seqA = 'ATGATCTCGTAATTAACCGGAATTTTGGGCC'
seqB = 'GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA'

contagemA_C = seqA.count('C')
contagemA_G = seqA.count('G')

porcentagemA_GC = (contagemA_C + contagemA_G) * 100 / len(seqA)
print(porcentagemA_GC)


contagemB_C = seqB.count('C')
contagemB_G = seqB.count('G')

porcentagemB_GC = (contagemB_C + contagemB_G) * 100 / len(seqB)
print(porcentagemB_GC)
