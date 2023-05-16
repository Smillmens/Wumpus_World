## 🔰 Objetivo
Entrar na mina, pegar o ouro e sair da mina.

 <br>

## 🔰 Regras do Jogo
- O Agente começa na Entrada da Mina.
- Um elemento pode estar disposto na mesma região que outro.
- Não pode ter 2 elementos que matam o Agente na região próxima a Entrada.
- O ouro não pode estar próximo a Entrada.
- O Agente não pode se mover diagonalmente.
- O Agente só anda uma casa por vez.
- O Agente se move aleatoriamente.
 
 <br>

## 🔰 1ª Etapa
Criar um ambiente da Mina com tamanho a ser definido. O ambiente deve ser de tamanho mínimo 4x4 e os elementos devem ser distribuídos de forma aleatória em quantidades proporcionais ao tamanho da mina.

* Primeiro criar um ambiente fixo depois um com elementos aleatórios.

<br>

## 🔰 Agente
Personagem principal.
	Pode se mover horizontalmente e verticalmente;
	Pode coletar o ouro;
	Pode matar o Wumpus;
	Percebe Brisa, Brilho, Fedor e Grito.

<br>

## 🔰 Elementos
- Wumpus = Monstro que mata o Agente.
  - Não se move;
  - Tem Fedor perceptível ao seu redor;
  - Pode morrer;
  - Grita ao morrer;
  - Posição aleatória;
  - * Um por ambiente. (Proporção: 1/16 = 6,23%)

- Ouro = Objetivo do Agente.
  - Não se move; Tem Brilho perceptível ao seu redor.
	- Posição aleatória;
	- * Um por ambiente. (Proporção: 1/16 = 6,23%)
	- 
- Poço = Região onde o Agente pode cair e morrer.
  - Não se move; Tem Brisa perceptível ao seu redor.
  - Posição aleatória;
  - *21,43% do tamanho do Mina. (Proporção: 3/16)

<br>

## 🔰 Percepções
Devem estar ao redor do elemento. Uma forma de generalizar a disposição das percepções é:

### Posição das percepções
se:
linha_atual - 1 >= 0 			#verifica para Cima 
linha_atual + 1 < Tamanho_da_Mina	#verifica para Baixo 
coluna_atual - 1 >= 0			#verifica para Esquerda 
coluna_atual + 1 < Tamanho_da_Mina	#verifica para Direita

<br>

## 🔰 Movimentação
Pra Cima, Baixo, Esquerda, Direita. A mesma lógica da posição das percepções pode ser usada para a movimentação.
Deve-se levar em conta que:
	- O Agente não pode atravessar as paredes, logo seu movimento e restrito
	- O Fedor e a Brisa devem "limitar" a movimentação do Agente, uma vez que ele pode morrer.
