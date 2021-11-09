from structures import *

def validateSequence(sequence):
    tempSeq = sequence.upper()
    for nucleotide in tempSeq:
        if nucleotide not in dnaNucleotides:
            return False
    return tempSeq

def countNucFrequency(sequence):
    tempFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in sequence:
        tempFreqDict[nucleotide] += 1
    return tempFreqDict

def transcription(sequence):
    return sequence.replace('T', 'U')

def reverseComplement(sequence):
    return ''.join([dnaReverseComplement[nucleotide] for nucleotide in sequence])[::-1]

def gcContent(sequence):
    return round(((sequence.count('C') + sequence.count('G')) / len(sequence) * 100), 6)    # round() statement: arredonda o valor ao número de casas decimais passado como segundo parâmetro;



def readFile(path):
    with open(path, 'r') as file:    # 'r' read
        return file.read()
# retorna uma lista com os elementos separados por espaço;
#       return [line.strip() for line in file.readlines()]   

# open statement in VSCode: a pasta onde os arquivos estão precisa estar aberta no software para que seja reconhecida como diretório raíz;
# caso não esteja aberta: é possível utilizar uma raw string (r'C:\exemplo\exemplo') ou duplo-backslash ('C:\\exemplo\\exemplo') ou slash simples no windows ('C:/exemplo/exemplo');