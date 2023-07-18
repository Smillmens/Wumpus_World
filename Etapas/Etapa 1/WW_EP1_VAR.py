'''
WUMPUS WORLD - ETAPA 1

Objetivo: Criar o ambiente da caverna.

Nesse código se encontra a criação do ambiente Caverna de ordem "N" e maior que 3, dispondo os 
elementos e suas percepções de forma aleatória e proporcional ao tamanho do ambiente.

A quantidade de wumpus e ouros foi definido como 1, não variando com o tamanho do ambiente. A
proporção de Poços é de 3 para 3/14. Essa proporção considera um ambiente de 16 casas (ondem 4)
preenchidas com 1 wumpos, 1 ouro e 3 poços, sendo apenas 14 espaços dedicados a 3 poços.

A posição das percepções segue a seguinte lógica:
- Se ao norte do ouro tem um poço: O brilho não vai ser perceptível no poço pois o agente não vai poder andar naquela casa;
- Se ao norte do ouro tem um wumpus: O brilho vai ser perceptivel, pois caso o agente mate o wumpus, ele vai poder andar por aquele casa;
'''

import random

# Criando o ambiente caverna:
tm_caverna = 6 # Define a ordem da matriz quadrada <<caverna>>
caverna = [[0 for _ in range(tm_caverna)] for _ in range(tm_caverna)]


## Distribuição dos elementos
ouro = "(O)"
poço = "(P)"
wumpus = "(W)"

q_ouro = 1                              # Quantidade de ouro
q_wumpus = 1                            # Quantidade de wumpus
q_poço = int((tm_caverna ** 2) * 3/16 ) # Quantidade de poços

def ad_elemento(q_elementos, elemento):                # Cria a função <<ad_elemento>> para adicionar elementos na caverna
    for _ in range(q_elementos):                       # Cria um laço <<for>> para adicionar os elementos de acordo com a quantidade de cada um
        linha = random.randint(0, tm_caverna - 1)      # Gera um número aleatório para "selecionar" uma linha
        coluna = random.randint(0, tm_caverna - 1)     #     ||            ||            ||             coluna
        while caverna[linha][coluna] != 0:             # Cria um laço <<while>> para verificar se casa está preenchida com algum elemento
            linha = random.randint(0, tm_caverna - 1)  # se verdadeiro, gera seleciona outra linha
            coluna = random.randint(0, tm_caverna - 1) #     ||            ||            ||  coluna
        caverna[linha][coluna] = elemento              # se falso, coloca o elemento na casa
        

### Informação para a função <<ad_elemento>>
ad_elemento(q_ouro, ouro)
ad_elemento(q_poço, poço)
ad_elemento(q_wumpus, wumpus)

print("Caverna com elementos:")
for linha in caverna:
    for celula in linha:
        print(celula, end="\t")
    print()


## Distribuição as percepções dos elementos
brilho = "(*)" # Representação do brilho
brisa = "(-)"  # Representação da brisa
fedor = "($)"  # Representação do fedor

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
    # Adiciona as Percepções no Ambiente:
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
