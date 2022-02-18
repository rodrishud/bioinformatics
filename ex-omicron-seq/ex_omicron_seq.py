# Exercício - Criando a sequência da proteína Spike da variante ômicron
# Realizado através do vídeo disponível em: https://www.youtube.com/watch?v=BhZukRrFD0A&t=1597s&ab_channel=OnlineBioinfoBioinform%C3%A1tica, pela profª Raquel Minardi

# O programa consiste em passar 3 parâmetros diretamente no terminal para a realização do sequenciamento:
# O primeiro é o nome desse programa, o segundo o arquivo da sequência original e o terceiro o arquivo com a lista de mutações.

# Importando o módulo sys para receber a leitura do arquivo diretamente da linha de comando do terminal
import sys


# Definindo a função de ler o arquivo de sequencia, utilizando a função with open() com o parâmentro 'r' (read)
# Armazenando o arquivo variável linha, convertendo o arquivo de texto em uma lista e depois retirando qualquer espaço após o fim da sequência no arquivo com o rstrip (right)
# Devido ao posicionamento no sequenciamento de proteínas comçar em 1, e posicionamentos no python começar em 0, é necessário inserir um gap (-) na posição 0 da lista para que as numerações do sequenciamento e do código estejam de acordo, utilizando o método insert().
def readSequence(fileName):
    with open(fileName, 'r') as file:
        linha = file.read()
        linha = list(linha.rstrip())
        linha.insert(0, '-')
        return linha

# Definindo a função de ler o arquivo de mutações, utilizando a função with open() com o parâmentro 'r' (read)
# Parecido com a função anterior, mas aqui a lista será organizada quebrando os itens após "," seguido de um espaço " "
def readMutations(fileName):
    with open(fileName, 'r') as file:
        linha = file.read()
        linha = linha.rstrip()
        m = linha.split(', ')
        return m

# Definindo a função que faz as substituições -> será incorporada dentro da próxima função
# Ela verifica se a posição informada corresponde ao aa1 informado. Caso seja diferente, ela não realiza nenhuma substituição.
def substituicao(lista, aa1, aa2, pos):
    if lista[pos] != aa1:
        print(f'A pósição {pos} não contém o aminoácido {aa1}')
        exit()
    else:
        lista[pos] = aa2

# Definindo a função que verifica se as mutações são substituições
# Com o for, a lista de mutações é percorrida;
# A primeira etapa verifica se os três primeiros caracteres correspondem a uma deleção (del) ou uma inserção (ins);
# Sendo uma substituição, então o primeiro valor é atribuído ao aminoácido 1 (original), o último valor ao aa2 (mutação), e a posição será o valor que está entre o índice 1 e o último.
# E ao final, chama a função que realiza a substituição na nova lista
def fazSubstituicao(lista, mut):
    for i in mut:
        if i[0:3] != 'del' and i[0:3] != 'ins':
            aa1 = i[0]
            aa2 = i[-1]
            pos = int(i[1:-1])
            substituicao(lista, aa1, aa2, pos)
            

### Programa principal

# Condição para abertura correta dos arquivos e funcionamento do algoritmo:
if len(sys.argv) != 3:
    print(f'USAGE: python3 <sequence> <mutations>')
    exit()

# Criando uma lista a partir da leitura do arquivo de sequências através da função readSequence() com o parâmetro que deverá ser inserido no terminal na posição [1]:
lista_original = readSequence(sys.argv[1])
# Criando uma lista a partir da leitura do arquivo de mutações através da função readMutations() com o parâmetro que deverá ser inserido no terminal na posição [2]:
lista_mutacoes = readMutations(sys.argv[2])
# Criando uma cópia da lista original que será o sequenciamento com as novas mutações:
lista_omicron = lista_original.copy()

# Chamando a função que fará as substituições na nova lista
fazSubstituicao(lista_omicron, lista_mutacoes)

print(lista_original[67], lista_omicron[67])