'''
WUMPUS WORLD - ETAPA 2

Objetivo: Criar o ambiente da caverna e fazer o agente andar por ela.
Missão do agente: Partir da entrada, pegar o ouro e voltar para a entrada sem morrer.

Com intuito de inicialização e ambientação ao projeto do Mundo de Wumpus, esse código
gera o ambiente em forma de matriz de ordem 4 com os elementos distribuidos de forma 
pré-definida:
    - 1 Ouro;
    - 3 Poços;
    - 1 Wumpus.
    
Inicialmente a idéia aqui é fazer o agente ir até o ouro sem morrer. Ele pode matar o 
Wumpus com base na quantidade de flechas e se o Wumpus morrer, ele e os fedores são 
apagados do mapa. A mesma idéia vale para o ouro, se o agente o pegar, ele e os brilhos
somem do mata. Porém esse dinãmica deve ser repensada para que a cada morte do agente,
o ambiente resete.
'''

import random

'''
////////////////////// CRIAÇÃO DO AMBIENTE //////////////////////
'''
# Criando o ambiente Caverna:
tm_caverna = 4 # Define a ordem da matriz quadrada
caverna = [[0 for _ in range(tm_caverna)] for _ in range(tm_caverna)]

# Distribuição e organização dos elementos:
ouro = "(O)"
poço = "(P)"
wumpus = "(W)"

caverna[3][3] = ouro
caverna[0][3] = poço
caverna[2][0] = poço
caverna[2][2] = poço
caverna[3][1] = wumpus

# Printado a caverna com os Elementos:
print("Caverna com Elementos:")
for linha in caverna:
    for celula in linha:
        print(celula, end="\t")
    print()


'''
////////////////////// DISTRIBUIÇÃO DE PERCEPÇÕES //////////////////////
'''
# Distribuição as Percepções dos Elementos:
brilho = "(*)" # Representação do Brilho
brisa = "(~)"  # Representação da Brisa
fedor = "($)"  # Representação do Fedor

def dist_perp(percepcao, l, c): # Cria uma função para distribuir as Percepções
    direcoes = [0,0,0,0]        # Matriz com as direções
    if (l > 0):                 # Norte
        direcoes[0] = (l-1, c)
    if (l + 1 < tm_caverna):    # Sul
        direcoes[1] = (l+1, c)
    if (c + 1 < tm_caverna):    # Leste
        direcoes[2] = (l, c+1)
    if (c > 0):                 # Oeste
        direcoes[3] = (l, c-1)
    # Adiciona as Percepções no Ambiente
    for direc in direcoes:
        if direc != 0:
            ll, cc = direc
            if caverna[ll][cc] == 0 or caverna[ll][cc] == percepcao:
                caverna[ll][cc] = percepcao
            elif caverna[ll][cc] == poço:
                caverna[ll][cc] = poço
            else:
                caverna[ll][cc] += percepcao

# Aplica as percepções na caverna:
for l in range(tm_caverna):
    for c in range(tm_caverna):
        if caverna[l][c] != 0:
            if caverna[l][c] == poço:                                # Quando for Poço
                dist_perp(brisa,l,c)
            elif ouro in caverna[l][c] or caverna[l][c] == ouro:     # Quando for Ouro
                dist_perp(brilho,l,c)
            elif wumpus in caverna[l][c] or caverna[l][c] == wumpus: # Quando for Wumpus
                dist_perp(fedor,l,c)

# Printado a caverna com Percepções:
print("__________")
print("Caverna com Elementos e Percepções:")
for linha in caverna:
    for celula in linha:
        print(celula, end="\t")
    print()



'''
////////////////////// MOVIMENTAÇÃO DO AGENTE //////////////////////
'''
# Variáveis auxiliares:
agente_pos = (0, 0) # Posição inicial do agente
ouro_encontrado = False # Variável para controlar se o ouro foi encontrado
direc_cardinais = [(-1, 0), (1, 0), (0, 1), (0, -1)] # Movimentos possíveis: norte, sul, leste, oeste
morte_pelo_poço = 0    # Contador da morte do agente pelo poço
morte_pelo_wumpus = 0  # Contador da morte do agente pelo wumpus
morte_do_wumpus = 0    # Contador da morte do Wumpus
tentaiva_pegar_ouro =0 # Contador de tentativas do agente pegar o ouro
flechas = 5            # Quantidade de flechas

def posicao_in_caverna(linha, coluna): # Função para verificar se uma posição está dentro dos limites da caverna
    return 0 <= linha < tm_caverna and 0 <= coluna < tm_caverna

def escolher_prox_casa(pos_atual_agente): # Função para escolher a próxima casa
    direc_sorteada = random.choice(direc_cardinais)  # Escolhe um movimento aleatório
    nova_pos = (pos_atual_agente[0] + direc_sorteada[0], pos_atual_agente[1] + direc_sorteada[1])    # Calcula a nova posição do agente
    return nova_pos

def mover_agente(): # Função para realizar o movimento do agente
    global agente_pos, ouro_encontrado, morte_pelo_poço, morte_pelo_wumpus, morte_do_wumpus, tentaiva_pegar_ouro, flechas 
    # print("começou a andar")
    
    # Laço para pegar o ouro:
    while True:
        nova_pos_agente = escolher_prox_casa(agente_pos)                   
        if posicao_in_caverna(nova_pos_agente[0], nova_pos_agente[1]): # Verifica se ta nos limites da matriz
                     
            # Poço: (tá certo) 
            if caverna[nova_pos_agente[0]][nova_pos_agente[1]] == poço:  # Verifica se a nova posição contém um poço
                agente_pos = (0, 0)  # Agente "morre" e volta para a posição inicial
                morte_pelo_poço += 1
                print("Agente caiu no poço: ","(",nova_pos_agente[0],",",nova_pos_agente[1],")")
                break

            # Mecânica da flecha
            if str(caverna[nova_pos_agente[0]][nova_pos_agente[1]]).find(fedor) != -1: # Verifica se a posição tem fedor
                if flechas >= 1:
                    flechas -= 1
                    pos_casa_tiro = None  # Inicializa a variável antes do loop
                    while True:
                        if pos_casa_tiro is None or not posicao_in_caverna(pos_casa_tiro[0], pos_casa_tiro[1]): # verifica se a posição tá dentro dos limites 
                            pos_casa_tiro = escolher_prox_casa(nova_pos_agente)  # Atualiza a posição da casa
                            print("$$$$$$ Posição onde o agente sentiu fedor",nova_pos_agente)
                            print("$$$$$$ casa selecionada para atirar",pos_casa_tiro)
                        else:
                            break  # Sai do loop se a posição estiver dentro dos limites da caverna
                                        
                    if caverna[pos_casa_tiro[0]][pos_casa_tiro[1]] == wumpus:
                        morte_do_wumpus += 1
                        print(" ")
                        print("Ahhhhhhhhh!!!! ") # grito
                        print("(Agente matou o Wumpus)")
                        print(" ")
                        caverna[pos_casa_tiro[0]][pos_casa_tiro[1]] = 0 # tira o Wumpus do mapa
                        # tira os fedores: 
                        for l in range(tm_caverna):
                            for c in range(tm_caverna):
                                if str(caverna[l][c]).find(fedor) != -1: 
                                    caverna[l][c] = caverna[l][c].replace(fedor,'')
                    else:
                        print("O agente não matou o Wumpus, Restam ", flechas," flechas")
                        break             
                elif flechas == 0:
                    print("As flechas acabaram ಥ_ಥ") 
                    break
            
            # Wumpus:
            elif caverna[nova_pos_agente[0]][nova_pos_agente[1]] == wumpus:  # Verifica se a nova posição contém O Wumpus
                agente_pos = (0, 0)  # Agente "morre" e volta para a posição inicial
                morte_pelo_wumpus += 1
                print("Agente morreu Wumpus: ","(",nova_pos_agente[0],",",nova_pos_agente[1],")")
                break
            
            # Ouro/Brilho: !(precisa colocar a questão da percepção)
            elif str(caverna[nova_pos_agente[0]][nova_pos_agente[1]]).find(brilho) != -1: 
                pos_casa_pegar_ouro = None  # Inicializa a variável antes do loop

                while True:
                    if pos_casa_pegar_ouro is None or not posicao_in_caverna(pos_casa_pegar_ouro[0], pos_casa_pegar_ouro[1]): # verifica se a posição tá dentro dos limites 
                        pos_casa_pegar_ouro = escolher_prox_casa(nova_pos_agente)  # Atualiza a posição da casa
                        print("--------- Posição onde o agente sentiu brilho",nova_pos_agente)
                        print("--------- casa selecionada para pegar o ouro",pos_casa_pegar_ouro)
                    else:
                        break  # Sai do loop se a posição estiver dentro dos limites da caverna

                if caverna[pos_casa_pegar_ouro[0]][pos_casa_pegar_ouro[1]] == ouro:  # Verifica se o agente encontrou o ouro
                    ouro_encontrado = True
                    caverna[pos_casa_pegar_ouro[0]][pos_casa_pegar_ouro[1]] = 0
                    # tira os brilhos: 
                    for l in range(tm_caverna):
                        for c in range(tm_caverna):
                            if str(caverna[l][c]).find(brilho) != -1: # Verifica se a posição tem fedor
                                caverna[l][c] = caverna[l][c].replace(brilho,'')
                    print(" ") # grito
                    print("Pegou o ouro")
                    print(" ")
                    # break
                else:
                    agente_pos = pos_casa_pegar_ouro
                    tentaiva_pegar_ouro += 1
                    print(" ")
                    print("---- Não pegou o ouro, na casa:", pos_casa_pegar_ouro)
                    print("---- Posição do agente", agente_pos)
                    print(" ")
                    break

            agente_pos = nova_pos_agente
            break
            
    # !Laço para volta do agente depois de ter pego o ouro.


# Loop principal do agente
parada_segurança = 500
contador = 0
while (not ouro_encontrado) and (contador < parada_segurança): 
    mover_agente()
    # print("Posição do agente:", agente_pos)
    contador += 1

if ouro_encontrado:
    print(" ")
    print("⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱")
    print("Ouro encontrado!")
    print("  (づ￣ 3￣)づ   ")
    print("⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰")
    print(" ")
    print("Numero de iterações = ",contador)
else:
    print(" ")
    print("⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱")
    print("           (●__●)  ")
    print("Limite de iterações atingido.")
    print("⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰")
    print(" ")

print("Morte pelo poço: ",morte_pelo_poço)
print("Morte pelo Wumpus: ",morte_pelo_wumpus)
print("Morte do Wumpus: ", morte_do_wumpus)
print("Tentaivas de pegar o ouro: ", tentaiva_pegar_ouro)

# # Printado a caverna com Percepções:
# print("__________")
# print("Caverna com Elementos e Percepções:")
# for linha in caverna:
#     for celula in linha:
#         print(celula, end="\t")
#     print()
