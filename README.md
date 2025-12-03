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
Processar o dataset de resultados de partidas internacionais de futebol, aplicando:
. Estruturas heterogêneas (Team e Match)
. Manipulação de arquivos CSV
. BST (por nome e por gols)
. AVL por pontuação
. Ordenação (Merge Sort e Insertion Sort)
. Métodos de busca (Linear e Binária)
. Geração de um resumo CSV final

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

Isso irá:
Ler o arquivo results.csv
Criar objetos Team e Match
Construir as BSTs
Calcular pontos e ordenar seleções
Construir a árvore AVL 
Gerar output/matches_summary.csv

## Etapas Implementadas
Etapa 1 – Modelagem

Classes:
Team(name, score)
Match(date, home_team, away_team, tournament, city, country, neutral)

Métodos:
total_goals()
to_list()

Etapa 2 – Leitura do CSV
Implementada em main.py.
Cada linha válida do CSV gera:
. objeto Team (mandante)
. objeto Team (visitante)
. objeto Match (completo)
Validação de linhas incluída.

Etapa 3 – BST
Duas árvores:
. BST ordenada por nome
. BST ordenada por gols

Método utilizado: percurso inorder para ordenar.

Etapa 4 – Ordenação
Dois algoritmos obrigatórios:
. Merge Sort (O(n log n))
. Insertion Sort (O(n²))

Aplicados em uma lista de seleções e pontos.

Saídas:
. Top 10 mais pontuados
. Bottom 10 menos pontuados

Etapa 5 – AVL
Árvore AVL completa com:
. rotações LL, RR, LR e RL
. atualização de altura
. balanceamento automático

Inserção baseada nos pontos da seleção.

Etapa 6 – Geração do CSV
Arquivo gerado:
output/matches_summary.csv

Formato:
year,country,home_team,away_team,score

Etapa 7 – Relatório Final
Incluído no arquivo report.md na raiz do projeto.

## Integração das Estruturas
O programa combina todas as etapas em main.py, funcionando como pipeline:
Ler dados
Criar objetos
Processar gols e pontos
Ordenar
Inserir nas árvores
Gerar arquivo final

## Integrantes e Contribuições
João Paulo – Modelagem das classes (Etapa 1)
Matheus – Leitura do CSV e filtragem (Etapa 2)
Rafagath – BSTs de nome e gols (Etapa 3)
Guilherme – Merge Sort e Insertion Sort (Etapa 4)
Samuel – Árvore AVL (Etapa 5)
Nicolas – CSV final (Etapa 6)
Todos – Revisão, testes e documentação

## Observações Importantes
. O projeto utiliza apenas o arquivo results.csv, conforme o enunciado oficial.
. Nenhuma biblioteca externa foi usada (somente Python padrão).
. A arquitetura segue exatamente a estrutura recomendada pelo professor.
