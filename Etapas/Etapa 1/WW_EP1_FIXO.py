'''
WUMPUS WORLD - ETAPA 1

Objetivo: Criar o ambiente da caverna.

Com intuito de inicialização e ambientação ao projeto do Mundo de Wumpus, esse código
gera o ambiente em forma de matriz de ordem 4 com os elementos distribuidos de forma 
pré-definida:
    - 1 Ouro;
    - 3 Poços;
    - 1 Wumpus.
 
'''

# Criando o ambiente Caverna:
tm_caverna = 4 # Define a ordem da matriz quadrada <Caverna>
caverna = [[0 for _ in range(tm_caverna)] for _ in range(tm_caverna)]

# Distribuição e organização dos elementos
caverna[3][3] = "(O)"       # Ouro posicionado na linha 0, coluna 3
caverna[0][3] = "(P)"       # Poço posicionado na linha 0, coluna 3
caverna[2][0] = "(P)"       # ||
caverna[2][2] = "(P)"       # ||
caverna[3][1] = "(W)"       # Wumpus posicionado na linha 0, coluna 1


# Printado a caverna:
for linha in caverna:
    for celula in linha:
        print(celula, end="\t")
    print()
