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

# Criando o ambiente caverna:
tm_caverna = 7 # Define a ordem da matriz quadrada <caverna>
caverna = [[0 for _ in range(tm_caverna)] for _ in range(tm_caverna)]

# Distribuição e organização dos elementos:
ouro = "(O)"
poço = "(P)"
wumpus = "(W)"

caverna[2][0] = ouro
caverna[4][5] = poço
caverna[4][4] = wumpus

# Printado a caverna com os elementos:
print("Caverna com Elementos:")
for linha in caverna:
    for celula in linha:
        print(celula, end="\t")
    print()


# Distribuição as Percepções dos Elementos:
brilho = "(*)" # Representação do Brilho
brisa = "(-)"  # Representação da Brisa
fedor = "($)"  # Representação do Fedor


def dist_perp(percepcao, l, c): # Cria uma função para distribuir as percepções
    direcoes = [0,0,0,0]        # Matriz com as direções
    if (l > 0):                 # Norte
        direcoes[0] = (l-1, c)
    if (l + 1 < tm_caverna):    # Sul
        direcoes[1] = (l+1, c)
    if (c + 1 < tm_caverna):    # Leste
        direcoes[2] = (l, c+1)
    if (c > 0):                 # Oeste
        direcoes[3] = (l, c-1)
    # Adiciona as percepções no ambiente
    for direc in direcoes:
        if direc != 0:
            ll, cc = direc
            if caverna[ll][cc] == 0 or caverna[ll][cc] == percepcao:
                caverna[ll][cc] = percepcao
            elif caverna[ll][cc] == poço:
                caverna[ll][cc] = poço
            else:
                caverna[ll][cc] += percepcao


for l in range(tm_caverna):
    for c in range(tm_caverna):
        if caverna[l][c] != 0:
            if caverna[l][c] == poço:                                # Quando for poço
                dist_perp(brisa,l,c)
            elif ouro in caverna[l][c] or caverna[l][c] == ouro:     # Quando for ouro
                dist_perp(brilho,l,c)
            elif wumpus in caverna[l][c] or caverna[l][c] == wumpus: # Quando for wumpus
                dist_perp(fedor,l,c)


# Printado a caverna com percepções:
print("__________")
print("Caverna com elementos e percepções:")
for linha in caverna:
    for celula in linha:
        print(celula, end="\t")
    print()
    
