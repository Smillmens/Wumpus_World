# Etapa 1 - Gerador aleatório de ambiente
Nesta etapa será criado um ambiente da caverna com tamanho a ser definido antes da inicialização. O ambiente deve ser de tamanho mínimo 3x3 e os elementos devem ser distribuídos de forma aleatória em quantidades proporcionais ao tamanho da mina. 

## 💠 Elementos
O ambiente deve conter os seguintes elementos:
- **Ouro** - Objetivo do agente, elemento neutro. 
  - Deve: Ser imóvel; gerar percepções ao seu redor (região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade a priore um, mas pode ser definido posteriormente.
- **Poço** - Elemento nocivo. O agente pode morrer ao "cair" no poço
  - Deve: Ser imóvel; gerar percepções ao seu redor (região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade proporcional ao tamanho do ambiente.
- **Wumpus** - Monstro, elemento nocivo. Pode matar o rgente e pode ser morto pelo Agente.
  - Deve: Ser imóvel; gerar percepções ao seu redor (região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade a priore um, mas pode ser definido posteriormente.

## 💠 Percepções
Cada elemento gera um tipo de percepção em torno de sua posição (região) que pode ser sentido pelo agente. Essa região compreende as casas adjacentes a posição do elemento (Norte, Sul, Leste, Oeste).
- **Brilho** - Percepção gerada pelo ouro. 
- **Brisa** - Percepção gerada pelo poço. Cada poço gera percepções em sua região
- **Fedor** - Percepção gerada pelo wumpus enquanto estiver vivo.

## 💠 Lógicas
- Dois elementos não podem ocupar a mesma casa;
- Duas ou mais percepções iguais podem ocupar a mesma casa;
- Na casa do poço não pode ter nenhuma percepçõa;
- Na casa do ouro e do Wumpus pode ter percepção.

# Navegação
* `WW_EP1_FIXO.py`: Arquivo contendo código para elaboração e teste de lógicas da Etapa 1.
* `WW_EP1_VAR.py`: Arquivo contendo código final da Etapa 1.
