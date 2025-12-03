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

## Etapa 2:
Nesta etapa, implementamos a leitura do arquivo results.csv e a criação dos objetos Match e Team a partir de cada linha válida do dataset. O objetivo principal foi transformar os dados brutos em estruturas de dados organizadas, prontas para serem utilizadas nas etapas posteriores (BST, AVL, Ordenação etc.).

# Tratamento do CSV
Utilizamos o módulo csv para abrir e iterar sobre o arquivo localizado em data/results.csv.
Cada linha é lida como um dicionário e passa por uma função de validação (linha_valida) que verifica:
Presença de todos os campos obrigatórios
Ausência de valores vazios
Conversão correta dos placares para inteiros
Conversão da data para datetime

Linhas que não atendiam a esses requisitos foram descartadas para evitar erros durante o processamento.

#-+ Estrutura de Dados Utilizada

A estrutura escolhida para armazenar os jogos foi uma lista Python.
Cada item da lista é um objeto Match, construído a partir:

da data convertida,

dos times (Team),

do placar,

e das demais informações da partida.

A escolha da lista foi feita por oferecer inserção eficiente e permitir percursos simples nas etapas seguintes.

✔ Saída da Etapa

Ao final da execução, o programa imprime:

<img width="696" height="29" alt="image" src="https://github.com/user-attachments/assets/24cf7101-085f-497b-8522-36340a939d4a" />

Esse número representa o total de partidas corretamente processadas e armazenadas na estrutura escolhida.

# Complexidade (Big O)

Leitura do CSV: O(n), onde n é o número de linhas do arquivo.

Validação: O(1) por linha, já que os campos são sempre os mesmos.

Criação dos objetos e inserção na lista: O(1) por partida.

Complexidade total da etapa: O(n).
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

## Etapa 4: 

## Etapa 5: 

## Etapa 6: 
