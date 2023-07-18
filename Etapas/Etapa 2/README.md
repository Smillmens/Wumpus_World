# Etapa 2 - Agente Reativo (versão 1)
Nesta etapa o agente será adicionado ao ambiente e deve interagir com os elementos presentes seguindo um conjunto de regras. Essas regras são especificadas por meio de uma tabela que descreve as movimentações, ações e mapeamento do agente e dos elementos. Deve-se levar em consideração que as ações e a movimentação do agente devem decisões tomadas aleatoriamente. Tambem, para que o agente tenha uma defesa contra o wumpus, o agente tem o porte de uma flecha que pode ser usada para matar o monstro.

<br>

## 💠 Elementos
O ambiente deve conter os mesmos elementos da etapa 1.

## 💠 Percepções
As percepções se mantem as mesmas com adição do Grito:
- **Grito** - Percepção gerada pelo wumpus ao morrer.

## 💠 Ações
A penas o agente pode realizar ações que são:
- Andar.
- Atirar a flecha;
- Pegar o ouro;

## 💠 Lógicas
### Lógicas gerais
- O agente sempre começa na entrada da caverna, posição (0,0);
- O agente se movimenta pelas casas adjacentes a sua casa atual. Uma casa por vez;
- Não pode haver elementos nocivos que bloqueiem a passagem do agente ao ouro. Por exemplo: se o agente começar na casa (0,0) não pode haver poços e wumpus ao mesmo tempo nas casas (0,1) e (1,0). O mesmo vale para o ouro e sua região;
- O agente sente a percepção, mas não sabe de onde está vindo;
- Para pegar o ouro, o agente precisa sentir brilho e escolher uma casa aleatória, dentro região da sua posição;
- Se o agente pegar o ouro, o ouro e os brilhos somem da caverna; 
- Para atirar, o agente precisa sentir o Fedor;
- A flecha funciona apenas em uma das cadas na região da casa atual do agente, desde que esteja dentro dos limites da caverna. O agente decide se atira para a norte, sul, leste, oeste;
- Se a flecha acertar o wumpus, ele morre, gera grito e os fedores e o wumpus somem da caverna.

### Lógicas para achar o ouro
Enquanto não acha ouro:
- anda uma casa
- if nova casa tá dentro da matriz:
- - verifica se tem brilho:
- - - escolhe a "proxima casa"
- - - if "proxima casa" está dentro dos limites
- - - - if a "aproxima casa tem ouro?
- - - - - ACHOU O OURO!!!
- - - - - retira ouro
- - - - - retira os brilhos	
- - - - - "proxima casa" = "casa atual"
- - - - break
- - - escolhe outra casa até achar uma casa dentro dos limites
<br>

- - verifica se é poço:
- - - agente morre
- - - "casa atual" = (0,0)
- - - break

- - verifica se tem fedor:
- - - if tem flechas:
- - - - escolhe proxima casa
- - - - if "proxima casa" está dentro dos limites
- - - - - if proxima casa tem um Wumpus
- - - - - - wumpus morre
- - - - - - tira o wumpus
- - - - - - tira os fedores
- - - - - - subtrai uma flecha
- - - - escolhe outra casa até achar uma casa dentro dos limites
- - verifica se é wumpus:
- - - agente morre
- - - "casa atual" = (0,0)
- - - break
<br>

### Lógicas para voltar com o ouro (❗Não aplicado❗)
o ponto aqui é mudar a variável "ouro encontrado" para uma lógica que faça:
- ir até o ouro sem morrer
- pegar o ouro
- voltar com o ouro para a entrada sem morrer

toda vez q ele morre ele volta pra entrada
- se ele morrer:
- - ouro encontrado = false:
- - ouro volta pro lugar
- - brilho volta pro lugar
- - wumpus volta pro lugar
- - fedor volta pro lugar

adicionar uma quantidade de vida ao agente, quando morre perde uma vida?
- while "ouro não encontrado" e "para de segurança" e "vida < 0":
- - código para pegar ouro
- if vidas == 0:
- - game over
 
<br>

# Navegação
* `WW_EP2_FIXO_IDA.py`: Arquivo contendo código para criação de um ambiente fixo e movimentação do agente até pegar o ouro.
* `WW_EP2_VAR_IDA.py`: Arquivo contendo código para criação de um ambiente e movimentação do agente, até pegar o ouro, de forma aleatória.
