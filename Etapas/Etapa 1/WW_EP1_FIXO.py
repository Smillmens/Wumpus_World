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
tm_caverna = 7 # Define a ordem da matriz quadrada <Caverna>
caverna = [[0 for _ in range(tm_caverna)] for _ in range(tm_caverna)]

# Distribuição e organização dos elementos
ouro = "(O)"
poço = "(P)"
wumpus = "(W)"

caverna[3][1] = ouro       # Ouro posicionado na linha 0, coluna 3
# caverna[2][1] = ouro       # Ouro posicionado na linha 0, coluna 3
caverna[3][3] = poço      # Poço posicionado na linha 0, coluna 3
# caverna[3][5] = poço       # ||
# caverna[5][3] = poço       # ||
caverna[3][0] = wumpus       # Wumpus posicionado na linha 0, coluna 1

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
