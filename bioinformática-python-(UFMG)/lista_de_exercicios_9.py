# 1)
for i in range(1, 151):
    c = (5/9)*(i-32)
    print(f'{i}°F = {c:.2f}°C')
    
#2)
seq = ['ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN'], ['TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'], ['ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN']
DNA = {'A', 'C', 'G', 'T'}
RNA = {'A', 'C', 'G', 'U'}
PROTEINA = {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'}


#3)
seqDNA = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
lista = []

for i in seqDNA:
    if i == 'T':
        lista.append('A')
    elif i == 'A':
        lista.append('U')
    elif i == 'C':
        lista.append('G')
    elif i == 'G':
        lista.append('C')

seqRNA = ''.join(lista)
print(seqRNA)

#4)
n = int(input('Insira um número: '))
fatorial = n

print(n)

while n > 1:
    fatorial = (fatorial * (n-1))
    n = n-1
    
print(fatorial)


#5)
n = 1

while n <= 15:
    for i in range(1, 11):
        result = n*i
        print(f'{n} x {i} = {result}')
    
    print()
    n += 1


#6)
seq = 'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
massa = {'A':71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259, 'F':147.06841, 'G':57.02146, 'H':137.05891, 'I':113.08406, 'K':128.09496,
          'L':113.08406, 'M':131.04049, 'N':114.04293, 'P':97.05276, 'Q':128.05858, 'R':156.10111, 'S':87.03203, 'T':101.04768, 'V':99.06841, 'W':186.07931, 'Y':163.06333}
m = 0

for a in seq:
    m += massa[a]
print(m)


#7)
