'''
WUMPUS WORLD - ETAPA 1

Objetivo: Criar o ambiente da caverna.

Nesse código se encontra a criação do ambiente Caverna de ordem "N" e maior que 3, dispondo os Elementos
de forma aleatória e proporcional ao tamanho do ambiente.
A quantidade de Wumpus e Ouros foi definido como 1, não variando com o tamanho do ambiente.
A proporção de Poços é de 3 para 3/14. Essa proporção considera um ambiente de 16 casas (ondem 4)
preenchidas com 1 Wumpos, 1 Ouro e 3 Poços, sendo apenas 14 espaços dedicados a 3 poços.
 
'''

import random

# Criando o ambiente Caverna:
tm_caverna = 5 # Define a ordem da matriz quadrada <<caverna>>
caverna = [[0 for _ in range(tm_caverna)] for _ in range(tm_caverna)]


## Distribuição dos Elementos
q_ouro = 1                              # Quantidade de Ouro
q_wumpus = 1                            # Quantidade de Wumpus
q_poço = int((tm_caverna ** 2) * 3/16 ) # Quantidade de Poços

def ad_elemento(q_elementos, elemento):                # Cria a função <<ad_elemento>> para adicionar Elementos na caverna
    for _ in range(q_elementos):                       # Cria um laço <<for>> para adicionar os Elementos de acordo com a quantidade de cada um
        linha = random.randint(0, tm_caverna - 1)      # Gera um número aleatório para "selecionar" uma linha
        coluna = random.randint(0, tm_caverna - 1)     #     ||            ||            ||             coluna
        while caverna[linha][coluna] != 0:             # Cria um laço <<while>> para verificar se Casa já está preenchida com algum Elementos
            linha = random.randint(0, tm_caverna - 1)  # se falso, gera seleciona outra linha
            coluna = random.randint(0, tm_caverna - 1) #     ||            ||           coluna
        caverna[linha][coluna] = elemento              # se verdadeiro, coloca o Elemento na Casa

### Informação para a função <<ad_elemento>>
ad_elemento(q_ouro, "(O)")
ad_elemento(q_poço, "(P)")
ad_elemento(q_wumpus, "(W)")


# Imprimindo o ambiente
for linha in caverna:
    for celula in linha:
        print(celula, end="\t")
    print()
