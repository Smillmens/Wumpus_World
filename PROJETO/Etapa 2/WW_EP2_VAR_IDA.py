'''
WUMPUS WORLD - ETAPA 2

Objetivo: Criar o ambiente da caverna e fazer o agente andar por ela.
Missão do agente: Partir da entrada, pegar o ouro e voltar para a entrada sem morrer.

O ambiente é gerado usando a mesma lógica da etapa 1 para distribuir os elementos.
    
Inicialmente a idéia aqui é fazer o agente ir até o ouro sem morrer. Ele pode matar o 
Wumpus com base na quantidade de flechas e se o Wumpus morrer, ele e os fedores são 
apagados do mapa. A mesma idéia vale para o ouro, se o agente o pegar, ele e os brilhos
somem do mata. Porém esse dinâmica deve ser repensada para que a cada morte do agente,
o ambiente resete.
'''

import random

'''
////////////////////// CRIAÇÃO DO AMBIENTE //////////////////////
'''
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


'''
////////////////////// DISTRIBUIÇÃO DE PERCEPÇÕES //////////////////////
'''
# Percepções dos Elementos:
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
    for direc in direcoes:      # Adiciona as Percepções no Ambiente
        if direc != 0:
            ll, cc = direc
            if caverna[ll][cc] == 0 or caverna[ll][cc] == percepcao:
                caverna[ll][cc] = percepcao
            elif caverna[ll][cc] == poço:
                caverna[ll][cc] = poço
            else:
                caverna[ll][cc] += percepcao

# Distribuição das percepções:
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
agente_pos = (0, 0)     # Posição inicial do agente
ouro_encontrado = False # Variável para controlar se o ouro foi encontrado
direc_cardinais = [(-1, 0), (1, 0), (0, 1), (0, -1)] # Movimentos possíveis: norte, sul, leste, oeste
morte_pelo_poço = 0     # Variável para contagem de mortes do agente pelo poço
morte_pelo_wumpus = 0   # Variável para contagem de mortes do agente pelo poço
morte_do_wumpus = 0     # Variável para contagem de mortes do wumpus
tentaiva_pegar_ouro =0  # Variável para contagem das tentativas de pegar o ouro
flechas = 5             # Quantidade de flechas

def posicao_in_caverna(linha, coluna): # Função para verificar se uma posição está dentro dos limites da caverna
    return 0 <= linha < tm_caverna and 0 <= coluna < tm_caverna

def escolher_prox_casa(pos_atual_agente): # Função para escolher uma próxima casa
    direc_sorteada = random.choice(direc_cardinais) # Escolhe um movimento aleatório
    nova_pos = (pos_atual_agente[0] + direc_sorteada[0], pos_atual_agente[1] + direc_sorteada[1]) # Calcula a nova posição do agente
    return nova_pos

def mover_agente(): # Função para realizar o movimento do agente
    global agente_pos, ouro_encontrado, morte_pelo_poço, morte_pelo_wumpus, morte_do_wumpus, tentaiva_pegar_ouro, flechas 
    # print("começou a andar") # Informar quando o loop começa
    # Laço para pegar o ouro:
    while True:
        nova_pos_agente = escolher_prox_casa(agente_pos)               # Chama a função para escolher a próxima casa para o agente
        if posicao_in_caverna(nova_pos_agente[0], nova_pos_agente[1]): # Verifica se ta nos limites da matriz
            # Caso seja um poço:
            if caverna[nova_pos_agente[0]][nova_pos_agente[1]] == poço:  # Verifica se a nova posição contém um poço
                agente_pos = (0, 0)  # Agente morre e volta para a posição inicial
                morte_pelo_poço += 1
                print("Agente caiu no poço: ",nova_pos_agente)
                break # Reinicia o loop com o agente na entrada da caverna

            # Caso seja fedor:
            if str(caverna[nova_pos_agente[0]][nova_pos_agente[1]]).find(fedor) != -1: # Verifica se a posição tem fedor
                if flechas >= 1: # Verifica se ainda tiver flechas
                    flechas -= 1
                    pos_casa_tiro = None  # Inicializa a variável antes do loop
                    # Escolher uma casa para atirar:
                    while True:
                        if pos_casa_tiro is None or not posicao_in_caverna(pos_casa_tiro[0], pos_casa_tiro[1]): # Verifica se a posição tá dentro dos limites da caverna
                            pos_casa_tiro = escolher_prox_casa(nova_pos_agente)                # Atualiza a posição da casa
                            print("$$$$$$ Posição onde o agente sentiu fedor",nova_pos_agente) # Informar a posição do agente
                            print("$$$$$$ casa selecionada para atirar",pos_casa_tiro)         # Informar a casa selecionada para atirar
                        else:
                            break  # Sai do loop quando acha uma casa dentro dos limites da caverna
                    
                    if caverna[pos_casa_tiro[0]][pos_casa_tiro[1]] == wumpus: # Se a casa escolhida para atirar tiver um wumpus:
                        morte_do_wumpus += 1
                        print(" ")
                        print("Ahhhhhhhhh!!!! ") # Grito do wumpus
                        print("(Agente matou o Wumpus)")
                        print(" ")
                        caverna[pos_casa_tiro[0]][pos_casa_tiro[1]] = 0 # Retira o wumpus do mapa
                        for l in range(tm_caverna):                     # Retira os fedores:
                            for c in range(tm_caverna):
                                if str(caverna[l][c]).find(fedor) != -1: 
                                    caverna[l][c] = caverna[l][c].replace(fedor,'')
                    else: # Se a casa escolhida não tiver o wumpus:
                        print("O agente não matou o Wumpus, Restam ", flechas," flechas")
                        break      # Reinicia o loop
                elif flechas == 0: # Caso as flechas tenham acabado
                    print("As flechas acabaram ಥ_ಥ") 
                    break # Reinicia o loop
                 

            # Caso seja wumpus:
            elif caverna[nova_pos_agente[0]][nova_pos_agente[1]] == wumpus:  # Verifica se a nova posição contém O Wumpus
                agente_pos = (0, 0)  # Agente morre e volta para a posição inicial
                morte_pelo_wumpus += 1
                print("Agente morreu Wumpus: ",nova_pos_agente)
                break # Reinicia o loop
            
            # Caso seja brilho:
            elif str(caverna[nova_pos_agente[0]][nova_pos_agente[1]]).find(brilho) != -1: # Verifica se a posição tem brilho
                pos_casa_pegar_ouro = None  # Inicializa a variável antes do loop
                # Escolher uma casa para pegar:
                while True:
                    if pos_casa_pegar_ouro is None or not posicao_in_caverna(pos_casa_pegar_ouro[0], pos_casa_pegar_ouro[1]): # verifica se a posição tá dentro dos limites da caverna
                        pos_casa_pegar_ouro = escolher_prox_casa(nova_pos_agente)                 # Atualiza a posição da casa
                        print("--------- Posição onde o agente sentiu brilho",nova_pos_agente)    # Informar a posição do agente
                        print("--------- casa selecionada para pegar o ouro",pos_casa_pegar_ouro) # Informar a posição para pegar
                    else:
                        break  # Sai do loop se a posição estiver dentro dos limites da caverna

                if caverna[pos_casa_pegar_ouro[0]][pos_casa_pegar_ouro[1]] == ouro: # Se a casa escolhida para pegar tiver o ouro:
                    ouro_encontrado = True
                    agente_pos = pos_casa_pegar_ouro                            # Agente vai para a posição
                    caverna[pos_casa_pegar_ouro[0]][pos_casa_pegar_ouro[1]] = 0 # Retira o ouro da caverna
                    for l in range(tm_caverna):                                 # Retira os brilhos
                        for c in range(tm_caverna):
                            if str(caverna[l][c]).find(brilho) != -1:
                                caverna[l][c] = caverna[l][c].replace(brilho,'')
                    print(" ")
                    print("Pegou o ouro") # Informa que o ouro foi pego
                    print(" ")
                else: # Caso não tenha ouro
                    agente_pos = pos_casa_pegar_ouro # Agente vai para a posição
                    tentaiva_pegar_ouro += 1
                    print(" ")
                    print("---- Não pegou o ouro, na casa:", pos_casa_pegar_ouro) # Informa que não pegou na casa()
                    print("---- Posição do agente", agente_pos)                   # Informa a posiçõa do agente
                    print(" ")
                    break # Reinicia o loop

            
            agente_pos = nova_pos_agente # Nova a posição do agente
            break # Reinicia o loop

       
# Loop principal do agente:
parada_segurança = 500 # Variável para parar o loop de pois de N iterações
contador = 0           # Variável para contar o numero de iterações
while (not ouro_encontrado) and (contador < parada_segurança): # Laço para fazer o agente andar enquanto não pega o ouro e não atinge a parada
    mover_agente()
    print("Posição do agente:", agente_pos)
    contador += 1

if ouro_encontrado: # Se o ouro for encontrado ao final do laço while:
    print(" ")
    print("⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱")
    print("Ouro encontrado!")
    print("  (づ￣ 3￣)づ   ")
    print("⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰⋱⋰")
    print(" ")
    print("Numero de iterações = ",contador)
else: # Se o numero de iterações limite for alcançado:
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
