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

## Etapa 3: Implementação das Árvores BST
Objetivo: Agrupar seleções por: nome (ordem alfabética) e gols totais (ordem crescente), criando duas árvores BST distintas.
BST ordenada pelo nome da seleção (BSTTeamName) e BST ordenada pelo total de gols marcados (BSTTeamGoals)
Cada nó armazena: team_name: nome da seleção, goals: quantidade total de gols marcados, left: filho à esquerda, right: filho à direita

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
