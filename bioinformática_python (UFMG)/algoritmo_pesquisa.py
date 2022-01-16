def pesquisa(reg, lista):
    for i in range(0, len(lista)):
        if lista[i] == reg:
            return i
    
    return -1


def pesquisaOrdenada(reg, lista):
    i = 0
    while i < len(lista) and reg >= lista[i]:
        if lista[i] == reg:
            return i
        
        i += 1
    
    return -1


def pesquisaBinaria(reg, lista):
    if len(lista) == 0:
        return -1
    
    esq = 0
    dir = len(lista)-1
    i = int((esq + dir)/2)
    
    while esq <= dir and reg != lista[i]:
        if reg > lista[i]:
            esq = i + 1
        else:
            dir = i - 1
        
        i = int((esq+dir)/2)
    
    if reg == lista[i]:
        return i
    else:
        return -1
