'''
WUMPUS WORLD - ETAPA 1

Objetivo: Criar o ambiente da caverna.

Nesse código se encontra a criação do ambiente Caverna de ordem "N" e maior que 3, dispondo os 
Elementos e suas Percepções de forma aleatória e proporcional ao tamanho do ambiente.

A quantidade de Wumpus e Ouros foi definido como 1, não variando com o tamanho do ambiente. A
proporção de Poços é de 3 para 3/14. Essa proporção considera um ambiente de 16 casas (ondem 4)
preenchidas com 1 Wumpos, 1 Ouro e 3 Poços, sendo apenas 14 espaços dedicados a 3 poços.

A posição das percepções segue a seguinte lógica:
- Se ao norte do Ouro tem um poço: O brilho não vai ser perceptível no poço pois o agente não vai poder andar naquela casa;
- Se ao norte do Ouro tem um wumpus: O brilho vai ser perceptivel, pois caso o Agente mate o Wumpus, ele vai poder andar por aquele casa;
'''

import random

# Criando o ambiente Caverna:
tm_caverna = 6 # Define a ordem da matriz quadrada <<caverna>>
caverna = [[0 for _ in range(tm_caverna)] for _ in range(tm_caverna)]


## Distribuição dos Elementos
ouro = "(O)"
poço = "(P)"
wumpus = "(W)"

q_ouro = 1                              # Quantidade de Ouro
q_wumpus = 1                            # Quantidade de Wumpus
q_poço = int((tm_caverna ** 2) * 3/16 ) # Quantidade de Poços

def ad_elemento(q_elementos, elemento):                # Cria a função <<ad_elemento>> para adicionar Elementos na caverna
    for _ in range(q_elementos):                       # Cria um laço <<for>> para adicionar os Elementos de acordo com a quantidade de cada um
        linha = random.randint(0, tm_caverna - 1)      # Gera um número aleatório para "selecionar" uma linha
        coluna = random.randint(0, tm_caverna - 1)     #     ||            ||            ||             coluna
        while caverna[linha][coluna] != 0:             # Cria um laço <<while>> para verificar se Casa está preenchida com algum Elementos
            linha = random.randint(0, tm_caverna - 1)  # se verdadeiro, gera seleciona outra linha
            coluna = random.randint(0, tm_caverna - 1) #     ||            ||            ||  coluna
        caverna[linha][coluna] = elemento              # se falso, coloca o Elemento na Casa
        

### Informação para a função <<ad_elemento>>
ad_elemento(q_ouro, ouro)
ad_elemento(q_poço, poço)
ad_elemento(q_wumpus, wumpus)

print("Caverna com Elementos:")
for linha in caverna:
    for celula in linha:
        print(celula, end="\t")
    print()


## Distribuição as Percepções dos Elementos
brilho = "(*)" # Representação do Brilho
brisa = "(-)"  # Representação da Brisa
fedor = "($)"  # Representação do Fedor

for l in range(tm_caverna):
    for c in range(tm_caverna):
        if caverna[l][c] !=0:
            if caverna[l][c] == poço:   # DISTRIBUIÇÃO DA BRISA
                if (l > 0): ################################################# NORTE
                    if caverna[l-1][c] == 0 or caverna[l-1][c] == brisa:    # Se tiver 0 ou brisa, coloca brisa;
                        caverna[l-1][c] = brisa
                    elif caverna[l-1][c] == poço:                           # Se tiver poço, deixa poço;
                        caverna[l-1][c] = poço
                    else:
                        caverna[l-1][c] += brisa                            # Se tiver outra coisa, incrementa na casa.
                if (l + 1 < tm_caverna): #################################### SUL
                    if caverna[l+1][c] == 0 or caverna[l+1][c] == brisa:
                        caverna[l+1][c] = brisa
                    elif caverna[l+1][c] == poço:
                        caverna[l+1][c] = poço
                    else:
                        caverna[l+1][c] += brisa
                if (c + 1 < tm_caverna): #################################### LESTE
                    if caverna[l][c+1] == 0 or caverna[l][c+1] == brisa:
                        caverna[l][c+1] = brisa
                    elif caverna[l][c+1] == poço:
                        caverna[l][c+1] = poço
                    else:
                        caverna[l][c+1] += brisa
                if (c > 0): ################################################# OESTE
                    if caverna[l][c-1] == 0 or caverna[l][c-1] == brisa:
                        caverna[l][c-1] = brisa
                    elif caverna[l][c-1] == poço:
                        caverna[l][c-1] = poço
                    else:
                        caverna[l][c-1] += brisa
            
            
            elif ouro in caverna[l][c] or caverna[l][c] == ouro:    # DISTRIBUIÇÃO DO BRILHO
                if (l > 0): ######################### NORTE
                    if caverna[l-1][c] == 0:        # Se tiver 0, coloca Brilho;
                        caverna[l-1][c] = brilho
                    elif caverna[l-1][c] == poço:   # Se tiver Poço, coloca Poço;
                        caverna[l-1][c] = poço
                    else:
                        caverna[l-1][c] += brilho   # Senão, incrementa Brilho na casa.
                if (l + 1 < tm_caverna): ############ SUL
                    if caverna[l+1][c] == 0:
                        caverna[l+1][c] = brilho
                    elif caverna[l+1][c] == poço:
                        caverna[l+1][c] = poço
                    else:
                        caverna[l+1][c] += brilho
                if (c + 1 < tm_caverna): ############ LESTE
                    if caverna[l][c+1] == 0:
                        caverna[l][c+1] = brilho
                    elif caverna[l][c+1] == poço:
                        caverna[l][c+1] = poço
                    else:
                        caverna[l][c+1] += brilho
                if (c > 0): ######################### OESTE
                    if caverna[l][c-1] == 0:
                        caverna[l][c-1] = brilho
                    elif caverna[l][c-1] == poço:
                        caverna[l][c-1] = poço
                    else:
                        caverna[l][c-1] += brilho
            
            
            elif wumpus in caverna[l][c] or caverna[l][c] == wumpus: # DISTRIBUIÇÃO DO FEDOR
                if (l > 0): ######################### NORTE
                    if caverna[l-1][c] == 0:        # Se for 0, coloca Fedor
                        caverna[l-1][c] = fedor
                    elif caverna[l-1][c] == poço:   # Se for Poço, deixa Poço
                        caverna[l-1][c] = poço
                    else:
                        caverna[l-1][c] += fedor    # Caso contrário, incrementa Fedor
                if (l + 1 < tm_caverna): ############ SUL
                    if caverna[l+1][c] == 0:
                        caverna[l+1][c] = fedor
                    elif caverna[l+1][c] == poço:
                        caverna[l+1][c] = poço
                    else:
                        caverna[l+1][c] += fedor 
                if (c + 1 < tm_caverna): ############ LESTE
                    if caverna[l][c+1] == 0:
                        caverna[l][c+1] = fedor
                    elif caverna[l][c+1] == poço:
                        caverna[l][c+1] = poço
                    else:
                        caverna[l][c+1] += fedor
                if (c > 0): ######################### OESTE
                    if caverna[l][c-1] == 0:
                        caverna[l][c-1] = fedor
                    elif caverna[l][c-1] == poço:
                        caverna[l][c-1] = poço
                    else:
                        caverna[l][c-1] += fedor         
              

# Printado a caverna:
print("__________")
print("Caverna com Elementos e Percepções:")
for linha in caverna:
    for celula in linha:
        print(celula, end="\t")
    print()
