# 1)
seqA = 'LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK'

seqB = 'KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS'

seqC = 'CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR'

if len(seqA) >= 80:
     print(seqA)
     
if len(seqB) >= 80:
     print(seqB)
     
if len(seqC) >= 80:
     print(seqC)


# 2)
media = (len(seqA) + len(seqB) + len(seqC)) / 3

if len(seqA) > media:
     print(seqA)

if len(seqB) > media:
     print(seqB)

if len(seqC) > media:
     print(seqC)


# 3)
if 'H' in seqA and 'P' not in seqA:
     print(seqA)
     
if 'H' in seqB and 'P' not in seqB:
     print(seqB)
     
if 'H' in seqC and 'P' not in seqC:
     print(seqC)
     
     
# 4)
if len(seqA) > len(seqB) and len(seqA)> len(seqC):
     print(seqA)
elif len(seqB) > len(seqA) and len(seqB) > len(seqC):
     print(seqB)
else:
     print(seqC)
     
     
# 5)
if len(seqA) > len(seqB) and len(seqA)> len(seqC):
     print(seqA)
     if len(seqB) > len(seqC):
          print(seqB)
          print(seqC)
     else:
          print(seqC)
          print(seqB)

elif len(seqB) > len(seqA) and len(seqB) > len(seqC):
     print(seqB)
     if len(seqA) > len(seqC):
          print(seqA)
          print(seqC)
     else:
          print(seqC)
          print(seqA)
          
else:
     print(seqC)
     if len(seqA) > len(seqB):
          print(seqA)
          print(seqB)
     else:
          print(seqB)
          print(seqA)
