# Trabalho de Estrutura de Dados

Grupo:
Rafagath, Nicolas, João Paulo, Samuel, Matheus e Guilherme da Silva Anselmo


## Etapa 1: Modelagem das Estruturas Team e Match
Objetivo: Criar estruturas de dados heterogêneas para representar cada partida de futebol, utilizando classes em Python.

### Estruturas Implementadas
Classe Team
Atributos:name (string), score (int)

Classe Match
Atributos: date (datetime), home_team (Team), away_team (Team), tournament (string), city (string), country (string), neutral (bool)
Métodos: total_goals() → retorna a soma dos gols da partida, to_list() → retorna uma lista no formato: 

-- Integrante responsável: João Paulo Araujo Cappeletti

## Etapa 2: Leitura do CSV e População das Estruturas
Nesta etapa, implementamos a leitura do arquivo results.csv e a criação dos objetos Match e Team a partir de cada linha válida do dataset. O objetivo principal foi transformar os dados brutos em estruturas de dados organizadas, prontas para serem utilizadas nas etapas posteriores (BST, AVL, Ordenação etc.).
Tratamento do CSV: Utilizamos o módulo csv para abrir e iterar sobre o arquivo localizado em data/results.csv.
Cada linha é lida como um dicionário e passa por uma função de validação (linha_valida) que verifica:
- Presença de todos os campos obrigatórios
- Ausência de valores vazios
- Conversão correta dos placares para inteiros
- Conversão da data para datetime

Linhas que não atendiam a esses requisitos foram descartadas para evitar erros durante o processamento.

Estrutura de Dados Utilizada: A estrutura escolhida para armazenar os jogos foi uma lista Python.
Cada item da lista é um objeto Match, construído a partir: da data convertida, dos times (Team), do placar, e das demais informações da partida.

A escolha da lista foi feita por oferecer inserção eficiente e permitir percursos simples nas etapas seguintes.

Ao final da execução, o programa imprime:

<img width="696" height="29" alt="image" src="https://github.com/user-attachments/assets/24cf7101-085f-497b-8522-36340a939d4a" />

Esse número representa o total de partidas corretamente processadas e armazenadas na estrutura escolhida.
Complexidade (Big O):
Leitura do CSV: O(n), onde n é o número de linhas do arquivo.
Validação: O(1) por linha, já que os campos são sempre os mesmos.
Criação dos objetos e inserção na lista: O(1) por partida.
Complexidade total da etapa: O(n).

-- Integrante responsável: Matheus Silva da Cruz

## Etapa 3: Implementação das Árvores BST
Objetivo: Agrupar seleções por: nome (ordem alfabética) e gols totais (ordem crescente), criando duas árvores BST distintas.
1. BST ordenada por nome (BSTTeamName)
Nó contém: team_name e goals.
Critério de inserção: ordem alfabética.
Funções implementadas:
- insert(team_name, goals)
- inorder() → retorna seleções em ordem alfabética.

2. BST ordenada por gols (BSTTeamGoals)
Mesmo nó da anterior.
Critério de inserção: menor número de gols à esquerda, maior à direita.
Funções implementadas:
- insert(team_name, goals)
- inorder() → retorna seleções ordenadas por gols.

Complexidade (Big-O): Inserção na BST
BST não balanceada
- O(log N) no melhor caso
- O(N) no pior caso
  
Construção das duas árvores:
- agrupar gols por time → O(N)
- inserir cada time → O(N²) no pior caso
- total esperado na prática → próximo de O(N log N)

Resultado da execução do programa:
<img width="1544" height="124" alt="image" src="https://github.com/user-attachments/assets/8f4d2c24-68ec-49d3-88c2-47a43153651b" />

-- Integrante responsável: Rafagath Grazziotin Miceli Klug

## Etapa 4: Ordenação das Seleções por Pontos
Na Etapa 4, reconstruímos os resultados das partidas e calculamos os pontos de cada seleção com base no placar final (3 pontos por vitória, 1 ponto por empate). Em seguida, aplicamos dois algoritmos de ordenação distintos com o objetivo de comparar desempenho e comportamento:

Merge Sort (O(n log n)) — algoritmo estável, eficiente e utilizado para a ordenação principal.

Insertion Sort (O(n²)) — algoritmo simples e menos eficiente, usado para fins comparativos.

Ambos ordenam as seleções de acordo com a quantidade total de pontos. Após a ordenação, o sistema gera como saída:

Top 10 seleções mais pontuadas

Bottom 10 seleções menos pontuadas

Resultados para Merge Sort e Insertion Sort, permitindo avaliar diferenças entre os métodos.

Essa etapa mostra a aplicação prática de algoritmos de ordenação, bem como a análise da performance entre estratégias de complexidades diferentes.

Saído do algoritmo:
<img width="1520" height="225" alt="image" src="https://github.com/user-attachments/assets/f96cabf1-a226-434a-aaf1-521dee2ab957" />

-- Integrante responsável: Guilherme da Silva Anselmo

## Etapa 5: 


## Etapa 6: Geração do Arquivo matches_summary.csv

Nesta etapa foi implementada a rotina responsável por gerar o arquivo matches_summary.csv a partir de todos os objetos Match carregados previamente na leitura do dataset results.csv.

O objetivo é produzir um resumo padronizado das partidas contendo apenas os campos essenciais especificados no enunciado:

year – ano da partida

country – país onde ocorreu o jogo

home_team – seleção mandante

away_team – seleção visitante

score – placar no formato "home_score-away_score"

A função save_summary() percorre a lista de partidas e grava cada linha no arquivo de saída, garantindo também que o diretório output/ exista antes da escrita.

Decisões de Implementação:

O método Match.to_row() foi criado para padronizar o formato de saída de cada partida.

O caminho de saída definido é output/matches_summary.csv, conforme exigido no trabalho.

Foram mantidas apenas operações de escrita sequencial, sem reordenação ou filtragem adicional, garantindo fidelidade ao dataset original.

Complexidade:

Tempo: O(n) – cada objeto Match é processado uma única vez.

Espaço adicional: O(1) – apenas variáveis auxiliares são utilizadas; nenhum novo conjunto de dados é criado.


<img width="345" height="25" alt="image" src="https://github.com/user-attachments/assets/af18da9c-0a50-401d-a598-e09142518ae5" />
