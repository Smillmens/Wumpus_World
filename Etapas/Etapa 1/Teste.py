import random

TAMANHO = 5

# Criando uma matriz quadrada com tamanho TAMANHO x TAMANHO
ambiente = [[0 for _ in range(TAMANHO)] for _ in range(TAMANHO)]

# Definindo a posição do Wumpus
ambiente[1][2] = "(W)"

# Definindo a posição do ouro
ambiente[3][0] = "(O)"

# Calculando a quantidade de poços a serem adicionados
quantidade_pocos = int((TAMANHO ** 2) * 4/16)

# Adicionando os poços de forma aleatória
for i in range(quantidade_pocos):
    linha = random.randint(0, TAMANHO - 1)
    coluna = random.randint(0, TAMANHO - 1)
    while ambiente[linha][coluna] != 0:
        linha = random.randint(0, TAMANHO - 1)
        coluna = random.randint(0, TAMANHO - 1)
    ambiente[linha][coluna] = "(P)"

# Imprimindo o ambiente
for linha in ambiente:
    for celula in linha:
        print(celula, end="\t")
    print()