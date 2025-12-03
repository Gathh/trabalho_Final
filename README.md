# Trabalho Final – Estrutura de Dados
Projeto desenvolvido para a unidade curricular Estrutura de Dados, utilizando o dataset Global Football – *results.csv*.

## Estrutura do Projeto
project/ <br>
├─ data/<br>
│  └─ results.csv<br>
├─ output/<br>
│  └─ matches_summary.csv        ← gerado automaticamente<br>
├─ src/<br>
│  ├─ data_structs.py            ← Etapa 1: Team e Match<br>
│  ├─ bst.py                     ← Etapa 3: Árvores BST<br>
│  ├─ avl.py                     ← Etapa 5: Árvore AVL<br>
│  ├─ sorting.py                 ← Etapa 4: Merge Sort e Insertion Sort<br>
│  ├─ search.py                  ← Busca Linear e Binária<br>
│  └─ main.py                    ← Executa etapas 2–6<br>
└─ report.md                     ← Relatório do trabalho<br>

## Objetivo do Projeto
Processar o dataset de resultados de partidas internacionais de futebol, aplicando:<br>
. Estruturas heterogêneas (Team e Match)<br>
. Manipulação de arquivos CSV<br>
. BST (por nome e por gols)<br>
. AVL por pontuação<br>
. Ordenação (Merge Sort e Insertion Sort)<br>
. Métodos de busca (Linear e Binária)<br>
. Geração de um resumo CSV final<br>

Todas as implementações seguem rigorosamente as especificações do trabalho.

## Como Executar
1. Pré-requisitos

Python 3.8+

Nenhuma biblioteca externa é necessária

2. Estrutura Recomendada

Garanta que a pasta esteja organizada como:

project/
  src/
  data/
  output/

3. Executar o projeto principal

Dentro da pasta src/, execute:
python main.py

Isso irá:<br>
Ler o arquivo results.csv<br>
Criar objetos Team e Match<br>
Construir as BSTs<br>
Calcular pontos e ordenar seleções<br>
Construir a árvore AVL <br>
Gerar output/matches_summary.csv<br>

## Etapas Implementadas
Etapa 1 – Modelagem

Classes:
Team(name, score)<br>
Match(date, home_team, away_team, tournament, city, country, neutral)

Métodos:<br>
total_goals()<br>
to_list()

Etapa 2 – Leitura do CSV<br>
Implementada em main.py.<br>
Cada linha válida do CSV gera:<br>
. objeto Team (mandante)<br>
. objeto Team (visitante)<br>
. objeto Match (completo)<br>
Validação de linhas incluída.<br>

Etapa 3 – BST<br>
Duas árvores:<br>
. BST ordenada por nome<br>
. BST ordenada por gols<br>

Método utilizado: percurso inorder para ordenar.

Etapa 4 – Ordenação<br>
Dois algoritmos obrigatórios:<br>
. Merge Sort (O(n log n))<br>
. Insertion Sort (O(n²))<br>

Aplicados em uma lista de seleções e pontos.<br>

Saídas:<br>
. Top 10 mais pontuados<br>
. Bottom 10 menos pontuados

Etapa 5 – AVL<br>
Árvore AVL completa com:<br>
. rotações LL, RR, LR e RL<br>
. atualização de altura<br>
. balanceamento automático<br>

Inserção baseada nos pontos da seleção.

Etapa 6 – Geração do CSV
Arquivo gerado:<br>
output/matches_summary.csv<br>

Formato:<br>
year,country,home_team,away_team,score<br>

Etapa 7 – Relatório Final<br>
Incluído no arquivo report.md na raiz do projeto.<br>

## Integração das Estruturas
O programa combina todas as etapas em main.py, funcionando como pipeline:<br>
Ler dados<br>
Criar objetos<br>
Processar gols e pontos<br>
Ordenar<br>
Inserir nas árvores<br>
Gerar arquivo final<br>

## Integrantes e Contribuições
João Paulo – Modelagem das classes (Etapa 1)<br>
Matheus – Leitura do CSV e filtragem (Etapa 2)<br>
Rafagath – BSTs de nome e gols (Etapa 3)<br>
Guilherme – Merge Sort e Insertion Sort (Etapa 4)<br>
Samuel – Árvore AVL (Etapa 5)<br>
Nicolas – CSV final (Etapa 6)<br>
Todos – Revisão, testes e documentação<br>

## Observações Importantes
. O projeto utiliza apenas o arquivo results.csv, conforme o enunciado oficial.<br>
. Nenhuma biblioteca externa foi usada (somente Python padrão).<br>
. A arquitetura segue exatamente a estrutura recomendada pelo professor.<br>
