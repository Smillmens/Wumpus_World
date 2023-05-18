# Etapa 1 - Gerador aleatório de ambiente
Nesta etapa será criado um ambiente da Caverna com tamanho a ser definido antes da inicialização. O ambiente deve ser de tamanho mínimo 3x3 e os elementos devem ser distribuídos de forma aleatória em quantidades proporcionais ao tamanho da mina. 

## 💠 Elementos
O ambiente deve conter os seguintes elementos:
- **Ouro** - Objetivo do Agente, elemento neutro. 
  - Deve: Ser imóvel; gerar percepções ao seu redor (Região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade a priore um, mas pode ser definido posteriormente.
- **Poço** - Elemento nocivo. O Agente pode morrer ao "cair" no poço
  - Deve: Ser imóvel; gerar percepções ao seu redor (Região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade proporcional ao tamanho do ambiente.
- **Wumpus** - Monstro, Elemento nocivo. Pode matar o Agente e pode ser morto pelo Agente.
  - Deve: Ser imóvel; gerar percepções ao seu redor (Região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade a priore um, mas pode ser definido posteriormente.

## 💠 Percepções
Cada elemento gera um tipo de percepção em torno de sua posição (Região) que pode ser sentido pelo Agente. Essa região compreende as Casas adjacentes a posição do elemento (Norte, Sul, Leste, Oeste).
- **Brilho** - Percepção gerada pelo Ouro. 
- **Brisa** - Percepção gerada pelo poço. Cada poço gera percepções em sua região
- **Fedor** - Percepção gerada pelo Wumpus enquanto estiver vivo.

## 💠 Lógicas
- Dois elementos não podem ocupar a mesma Casa.
- Duas ou mais Percepções podem ocupar a mesma Casa.

# Links
