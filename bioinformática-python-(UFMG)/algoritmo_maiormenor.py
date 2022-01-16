def maiorMenor3(lista):
    if len(lista) % 2 == 1:
        lista.append(lista[0])
        
    if lista[0] < lista [1]:
        menor = lista[0]
        maior = lista[1]
    
    else:
        menor = lista[1]
        maior = lista[0]
        
    i = 2
    while i < len(lista):
        if lista[i] > lista[i+1]:
            if lista[i] > maior:
                maior = lista[i]
            
            if lista[i+1] < menor:
                menor = lista[i+1]
            
        else:
            if lista[i+1] > maior:
                maior = lista[i+1]
            if lista[i] < menor:
                menor = lista[i]
                
        i += 2
    
    tupla = (menor, maior)
    return tupla
    