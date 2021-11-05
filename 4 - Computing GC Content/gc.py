def readFile(path):
    with open(path, 'r') as f:
        return [l.strip() for l in f.readlines()]

FASTAfile = readFile("rosalind_gc.txt")

