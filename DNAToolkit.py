dnaNucleotides = ['A', 'C', 'G', 'T']

dnaReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

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

