# Termos e definições do Mundo de Wumpus***

## Ambientação
- Agente - unidade que irá interagir com os elementos, sentir as percepções e realizar ações.
- Ambiente - Conjunto composto pela caverna, agente, elementos e percepções.
- Casa/Posição - Localização (linha, coluna) da caverna.
- Caverna - Terreno do Mundo de Wumpus. Matriz onde serão adicionados os elementos e as percepções.
- Direção/Movimentação - Direções adjacentes (norte, sul, leste e oeste).
- Entrada da caverna - Casa/Posição inicial do agente. Inicializada em (0,0) .
- Parede/limites - Faz referência ao tamanho da matriz caverna.
- Região - Casas/Posições adjacentes a casa em questão.

## Elementos e Subelementos
- Elemento - Componentes que farão parte do ambiente.
- Flecha - Item do agente capaz de matar o wumpus.
- Ouro - Elemento que emite brilho. Parte do obejtivo do agente. 
- Poço - Elemento nocivo que emite brisa. O agente pode morrer se "cair" no poço.  
- Subelemento - Itens e habilidade.
- Vidas - Subelemtento que mede a aquantidade de vezes que o agente pode morrer. Também pode sevir como variável de controle.
- Wumpus - Elemento nocivo que emite fedor. Mata o agente.

## Percepções
- Brilho - Percepção gerada pelo ouro
- Brisa - Percepção gerada pelo poço
- Fedor - Percepção gerada pelo wumpus
- Grito -  Percepção gerada pelo wumpus ao morrer

## Ações
- Andar - Ato de se movimentar pela caverna
- Atirar - Ato de usar a flecha.
- Morrer - Condição para reiniciar o jogo.
- Pegar - Ato de pegar o ouro.




