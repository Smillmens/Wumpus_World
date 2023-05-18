# Etapa 2 - Agente Reativo (versão 1)
Nesta etapa o Agente será adicionado ao ambiente e deve interagir com os elementos presentes seguindo um conjunto de regras. Essas regras são especificadas por meio de uma ***tabela*** que descreve as movimentações, ações e mapeamento do Agente e dos Elementos. Deve-se levar em consideração que as ações e a movimentação do Agente devem decisões tomadas aleatoriamente. Tambem, para que o Agente tenha uma defesa contra o Wumpus, o Agente tem o porte de uma Flecha que pode ser usada para matar o monstro.

<br>

## 💠 Elementos
O ambiente deve conter os mesmos elementos da etapa 1.

## 💠 Percepções
As percepções se mantem as mesmas com adição do Grito:
- **Grito** - Percepção gerada pelo Wumpus ao morrer.

## 💠 Ações
A penas o Agente pode realizar ações que são:
- Andar.
- Atirar a Flecha;
- Pegar o Ouro;

## 💠 Lógicas
- O Agente sempre começa na Entrada da Caverna, posição (0,0).
- O Agente se movimenta pelas Casas adjacentes a sua Casa atual. Uma Casa por vez.
- Não pode haver elementos nocivos que bloqueiem a passagem do Agente ao Ouro. Por exemplo: se o agente começar na Casa (0,0) não pode haver Poços e Wumpus ao mesmo tempo nas Casas (0,1) e (1,0). O mesmo vale para o Ouro e sua região.
- O Agente sente a Percepção, mas não sabe de onde está vindo.
- Para pegar o Ouro, o Agente deve estar na Casa do Ouro e Pegar. (***REVER LÓGICA - o agente precisa estar na casa? a casa onde o ouro está emite percepção?***)
- Para atirar, o Agente precisa sentir o Fedor.
- A Flecha funciona apenas em uma das cadas na Região da Casa atual do Agente. O Agente decide se atira para a norte, sul, leste, oeste. (***As Paredes devem ser levadas em consideração?***)
- Se a Flecha acertar o Wumpus, ele morre, gera Grito e o Fedor some.

<br>

# Links
