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
Nesta etapa será criado um ambiente da Caverna com tamanho a ser definido antes da inicialização. O ambiente deve ser de tamanho mínimo 3x3 e os elementos devem ser distribuídos de forma aleatória em quantidades proporcionais ao tamanho da mina. Além disso, as definição do Agente ainda não são relevantes, mas algumas regras devem ser consideradas.

### Elementos
O ambiente deve conter os seguintes elementos:
- Ouro - Objetivo do Agente, elemento neutro. 
  - Deve: Ser imóvel; gerar percepções ao seu redor (Região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade a priore um, mas pode ser definido posteriormente.
- Poço - Elemento nocivo. O Agente pode morrer ao "cair" no poço
  - Deve: Ser imóvel; gerar percepções ao seu redor (Região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade proporcional ao tamanho do ambiente.
- Wumpus - Monstro, Elemento nocivo. Pode matar o Agente e pode ser morto pelo Agente.
  - Deve: Ser imóvel; gerar percepções ao seu redor (Região); posição aleatória em cada partida, mas obedecendo uma lógica; quantidade a priore um, mas pode ser definido posteriormente.

### Percepções
Cada elemento gera um tipo de percepção em torno de sua posição (Região) que pode ser sentido pelo Agente. Essa região compreende as Casas adjacentes a posição do elemento (Norte, Sul, Leste, Oeste).
- Brilho - Percepção gerada pelo Ouro. 
- Brisa - Percepção gerada pelo poço. Cada poço gera percepções em sua região
- Fedor - Percepção gerada pelo Wumpus enquanto estiver vivo.
- Grito - Percepção gerada pelo Wumpus ao morrer.

### Lógicas
Nessa etapa o Agente ainda não existe, mas deve-se levar em consideração o seu ponto de partida e sua movimentação para concluir o objetivo. Como o Agente deve se mover em Casas adjacentes e sua posição inicial é sempre a mesma em cada Partida,
- Não pode haver elementos nocivos que bloqueiem sua passagem. Por exemplo: se o agente começar na Casa (0,0) não pode haver Poços e Wumpus ao mesmo tempo nas Casas (0,1) e (1,0).
- Não pode haver elementos nocivos na Região do Ouro.
- Dois elementos não podem ocupar a mesma Casa.

<br>

## 💠 Etapa 2 - Agente Reativo (versão 1)
Nesta etapa o Agente será adicionado ao ambiente e deve interagir com os elementos presentes.


- o comportamento do agente é definido a partir do seu conjunto de regras;
- Este conjunto de regras deve ser especificado por meio de uma tabela, aos moldes da que foi especificada, inicialmente na Aula 04;
- A partir da especificação, o proximo passo é codificar o Agente e integrar ao gerador aleatório de ambientes de forma a possibilitar a realização de testes de validação para posterior avaliação de performace;
- obs.: Serão projetadas várias versões deste agente. Nesta primeira versão, ele utiliza a apenas o conunto de regras como base de conhecimento, OU SEJA, NÃO TEM MEMÓRIA E NENHUM OUTRO MECANISMO MAIS OSFISTICADO PARA ESCOLHER QUAL DAS possíveis regras utilizar. Para isso, deve ser uma escolha aleatória. Além disso, ele tem apenas uma única flecha.



Nesta etapa será criado um ambiente da Caverna com tamanho a ser definido antes da inicialização. O ambiente deve ser de tamanho mínimo 3x3 e os elementos devem ser distribuídos de forma aleatória em quantidades proporcionais ao tamanho da mina. Além disso, as definição do Agente ainda não são relevantes, mas algumas regras devem ser consideradas.





