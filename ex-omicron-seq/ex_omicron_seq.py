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
    

### Programa principal

# Condição para abertura correta dos arquivos e funcionamento do algoritmo:
if len(sys.argv) != 3:
    print(f'USAGE: python3 <sequence> <mutations>')
    exit()

# Criando uma lista a partir da leitura do arquivo de sequências através da função readSequence() com o parâmetro que deverá ser inserido no terminal na posição [1]:
lista_original = readSequence(sys.argv[1])
# Criando uma lista a partir da leitura do arquivo de mutações através da função readMutations() com o parâmetro que deverá ser inserido no terminal na posição [2]:
lista_mutacoes = readMutations(sys.argv[2])


print(lista_original)
print(f'O sequenciamento original possui {len(lista_original)} aminoácidos.')
print(lista_mutacoes)