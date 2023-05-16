
'''
WUMPUS WORLD - ETAPA 1
Objetivo: Criar um ambiente da Caverna com tamanho "N". A caverna deve conter os elementos
'''

espaço = 6
caverna = [[0 for _ in range(espaço)] for _ in range(espaço)]

# Definindo a posição do Wumpus
caverna[0][1] = "(W)"

# Definindo a posição dos Poços
caverna[1][0] = "(P)"
caverna[1][2] = "(P)"
caverna[3][3] = "(P)"

# Definindo a posição do Ouro
caverna[0][3] = "(O)"

# Definindo a posição do Agente
caverna[3][0] = "(A)"

# Imprimindo o ambiente
for linha in caverna:
    for celula in linha:
        print(celula, end="\t")
    print()