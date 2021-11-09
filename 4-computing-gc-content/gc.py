def readFile(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def gcContent(sequence):
    return round(((sequence.count('C') + sequence.count('G')) / len(sequence) * 100), 6)


# Define uma variável com o conteúdo da lista
FASTAfile = readFile('4-computing-gc-content/rosalind_gc.txt')

# Dicionário com os labels + data
FASTAdict = {}

# String que recebe o label atual
FASTAlabel = ''

# Função que converte o FASTAfile (lista) no dicionário
for line in FASTAfile:
    if '>' in line:
        FASTAlabel = line
        FASTAdict[FASTAlabel] = ''
    else:
        FASTAdict[FASTAlabel] += line

# Formata os dados usando uma compreensão de dicionário para gerar um novo dicionário com os valores indicando a porcentagem de GC Content
RESULTdict = {key: gcContent(value) for (key, value) in FASTAdict.items()}

# Busca pelo maior valor no novo dicionário
MaxGCKey = max(RESULTdict, key=RESULTdict.get)

# Printa o formato para o Rosalind
print(f'{MaxGCKey[1:]}\n{RESULTdict[MaxGCKey]}')