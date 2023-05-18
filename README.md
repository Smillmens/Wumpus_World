<img src="https://github.com/Oseiasdfarias/IA_mundo_do_wumpus/blob/main/utils/logo.png?raw=true" alt="Logo UFPA" style="width:100px"> 

<strong>Universidade Federal do Pará || Campus Universitário de Tucuruí || Faculdade de Engenharia Elétrica</strong>\
<strong>Alessandro de Araújo Fonseca || Kevin Martins Medeiros || Sávio Milhomens de Sousa </strong>

<br>

# Mundo do Wumpus - Intelegência Computacional

O mundo de Wumpus é um ambiente de simulação usado para ensinar conceitos de inteligência artificial e aprendizado por reforço. Nesse ambiente, o objetivo é que o Agente, controlado pelo algoritmo de inteligência artificial, encontre o Ouro e saia da Caverna sem ser comido pelo monstro Wumpus ou cair em um Poço. Para isso, o agente precisa coletar informações sobre o ambiente e tomar decisões com base nessas informações.

A metodologia de estudo de inteligência computacional usando o mundo de Wumpus é muito útil porque permite que os alunos aprendam conceitos teóricos de IA de uma forma prática e interativa. Além disso, o mundo de Wumpus pode ser facilmente adaptado para diferentes níveis de complexidade, permitindo que os estudantes progridam em sua aprendizagem.

<br>

# Etapas do projeto
O objetivo da criação do Mundo do Wumpus é a apredizagem com o desenvolvimento de inteligência artificial, para isso, gradativamete será entregue inteligência ao Agente para que ele possa resolver os problemas de forma mais eficiente. Essa evolução do Agente será realizada nas seguintes etapas.

## 💠 Etapa 1 - Gerador aleatório de ambiente
Nesta etapa será criado um ambiente da Caverna com tamanho a ser definido antes da inicialização. O ambiente deve ser de tamanho mínimo 3x3 e os elementos devem ser distribuídos de forma aleatória em quantidades proporcionais ao tamanho da mina. 

### Elementos
O ambiente deve conter os seguintes elementos:
- **Ouro** - Objetivo do Agente, elemento neutro. 
  - Deve: Ser imóvel; gerar percepções ao seu redor (Região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade a priore um, mas pode ser definido posteriormente.
- **Poço** - Elemento nocivo. O Agente pode morrer ao "cair" no poço
  - Deve: Ser imóvel; gerar percepções ao seu redor (Região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade proporcional ao tamanho do ambiente.
- **Wumpus** - Monstro, Elemento nocivo. Pode matar o Agente e pode ser morto pelo Agente.
  - Deve: Ser imóvel; gerar percepções ao seu redor (Região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade a priore um, mas pode ser definido posteriormente.

### Percepções
Cada elemento gera um tipo de percepção em torno de sua posição (Região) que pode ser sentido pelo Agente. Essa região compreende as Casas adjacentes a posição do elemento (Norte, Sul, Leste, Oeste).
- **Brilho** - Percepção gerada pelo Ouro. 
- **Brisa** - Percepção gerada pelo poço. Cada poço gera percepções em sua região
- **Fedor** - Percepção gerada pelo Wumpus enquanto estiver vivo.

### Lógicas
- Dois elementos não podem ocupar a mesma Casa.
- Duas ou mais Percepções podem ocupar a mesma Casa.

<br>

## 💠 Etapa 2 - Agente Reativo (versão 1)
Nesta etapa o Agente será adicionado ao ambiente e deve interagir com os elementos presentes seguindo um conjunto de regras. Essas regras são especificadas por meio de uma ***tabela*** que descreve as movimentações, ações e mapeamento do Agente e dos Elementos. Deve-se levar em consideração que as ações e a movimentação do Agente devem decisões tomadas aleatoriamente. Tambem, para que o Agente tenha uma defesa contra o Wumpus, o Agente tem o porte de uma Flecha que pode ser usada para matar o monstro.

### Elementos
O ambiente deve conter os mesmos elementos da etapa 1.

### Percepções
As percepções se mantem as mesmas com adição do Grito:
- **Grito** - Percepção gerada pelo Wumpus ao morrer.

### Ações
A penas o Agente pode realizar ações que são:
- Andar.
- Atirar a Flecha;
- Pegar o Ouro;



### Lógicas
- O Agente sempre começa na Entrada da Caverna, posição (0,0).
- O Agente se movimenta pelas Casas adjacentes a sua Casa atual. Uma Casa por vez.
- Não pode haver elementos nocivos que bloqueiem a passagem do Agente ao Ouro. Por exemplo: se o agente começar na Casa (0,0) não pode haver Poços e Wumpus ao mesmo tempo nas Casas (0,1) e (1,0). O mesmo vale para o Ouro e sua região.
- O Agente sente a Percepção, mas não sabe de onde está vindo.
- Para pegar o Ouro, o Agente deve estar na Casa do Ouro e Pegar. (***REVER LÓGICA - o agente precisa estar na casa? a casa onde o ouro está emite percepção?***)
- Para atirar, o Agente precisa sentir o Fedor.
- A Flecha funciona apenas em uma das cadas na Região da Casa atual do Agente. O Agente decide se atira para a norte, sul, leste, oeste. (***As Paredes devem ser levadas em consideração?***)
- Se a Flecha acertar o Wumpus, ele morre, gera Grito e o Fedor some.

<br>

## 💠 Etapa 3 - Agente Reativo (versão 2)
***⚠ Trabalhando ⚠***











