UNIVERSIDADE DO OESTE DE SANTA CATARINA - UNOESC<br>
Curso: Ciência de Dados e Inteligência Artificial<br>
Componente curricular: Projeto de Ciência de Dados<br>
Professor: Danton Jose Bertuol<br>
Aluno: Victor Lermen

# Atividade Avaliativa 2: <br> Análise Histórica da Fórmula 1 com Data Warehouse e ETL

## Tecnologias
- Python 3.14
- Pandas
- SQLite
- DBeaver
- Plotly
- kagglehub
- NumPy

## Como executar o projeto
1. Crie o ambiente virtual python:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux ou MacOS
source .venv/bin/activate
```
2. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
3. Execute o script `etl.py` para fazer o download do dataset, transformar os dados e criar o datawarehouse
4. Para as análises gráficas, execute o script `analyze.py`

## Problema de Negócio
A Fórmula 1 é o maior campeonato de automobilismo do mundo, com dados históricos desde 1950. Ao longo de mais de 70 anos de competição, pilotos e equipes de diferentes nacionalidades disputaram corridas em circuitos ao redor do mundo, gerando um volume expressivo de dados históricos.

O desafio deste projeto é responder uma pergunta central: **quais pilotos e equipes apresentaram o melhor desempenho ao longo da história da F1?** Para isso, é necessário ir além dos números brutos comparar pilotos de eras diferentes exige contextualizar cada conquista dentro do período em que foi alcançada, considerando as diferentes tecnologias, regulamentos e níveis de competitividade de cada época.

## Requisitos de Negócio
* Coletar e centralizar dados históricos da F1 de 1950 a 2024, incluindo resultados de corridas, pilotos, equipes e circuitos.
* Criar um Data Warehouse com modelo dimensional para suportar análises comparativas entre pilotos e equipes.
* Classificar as corridas por eras históricas da F1, permitindo análises contextualizadas por período.
* Identificar os pilotos com maior número de vitórias, pódios, poles e voltas rápidas.
* Analisar o aproveitamento histórico dos pilotos (vitórias por corridas disputadas).
* Identificar Hat-Tricks (pole + vitória + volta rápida na mesma corrida) ao longo da história.

## Explicação do Projeto
Com base nos requisitos, foi utilizado o dataset da Fórmula 1 disponível no Kaggle, contendo dados históricos de 1950 a 2024 sobre pilotos, equipes, circuitos e resultados de corridas.

Como primeira etapa, os dados são baixados automaticamente via `kagglehub` e carregados em um banco de dados SQLite de staging, onde são armazenados em sua forma bruta antes de serem processados. Essa etapa garante a integridade dos dados e independência do dataset original. Todos esses itens estão no script `extract.py`.

Na segunda etapa, os dados são transformados onde colunas desnecessárias são removidas, valores nulos tratados e uma tabela derivada `dim_era` é criada do zero com base no histórico de regulamentos de motores da F1. Essa tabela classifica cada corrida em sua respectiva era histórica, permitindo comparações contextualizadas entre períodos distintos da categoria. Essas transformações estão no script `transform.py`.

Na terceira etapa, o Data Warehouse é criado via `migration.sql` com tabelas dimensão e fato com chaves primárias e estrangeiras. Os dados transformados são então carregados no banco. Essa etapa está no script `load.py`.

Com os dados processados e armazenados no Data Warehouse, foram realizadas análises gráficas interativas utilizando a biblioteca Plotly Express, respondendo às perguntas de negócio definidas. As análises estão no script `analyze.py`.

## Resultados
As análises gráficas permitiram identificar com clareza os pilotos e equipes de maior destaque na história da Fórmula 1.

Em termos absolutos, **Lewis Hamilton** se destacou como o piloto de melhor desempenho histórico em quase todas as métricas analisadas, liderando o ranking de vitórias, pódios, poles e Hat-Tricks. A única exceção foi o aproveitamento de vitórias por corridas disputadas, onde **Juan Manuel Fangio** lidera com 41.4%, evidenciando sua dominância em uma era com menos competidores e menos corridas por temporada.

No recorte por eras, cada período teve seu dominador: Fangio na Era Clássica, Jackie Stewart na Era DFV, Senna e Prost disputando a Era Turbo, Schumacher reinando na Era Aspirada, Vettel na Era V8 e Hamilton dividindo a Era Híbrida com Verstappen nos anos mais recentes. No âmbito das equipes, a **Mercedes** dominou a Era Híbrida com 116 vitórias, enquanto a **Ferrari** se destacou como a equipe mais consistente da história, presente em todas as eras.

Como análise bônus, foi apresentado um mapa interativo das vitórias de **Ayrton Senna**, mostrando os 17 circuitos ao redor do mundo onde o tricampeão brasileiro venceu — com destaque especial para Mônaco, onde conquistou 6 vitórias, consolidando sua lenda no circuito mais icônico da categoria.

## Limitações
- O dado de volta mais rápida (`rank`) só está disponível a partir de 2004, limitando as análises de Hat-Tricks e voltas rápidas ao período 2004–2024
- O Grand Chelem completo (pole + vitória + volta rápida + liderar todas as voltas) não foi implementado pois exigiria o processamento do `lap_times.csv`, arquivo com milhões de registros

## Referências
- [Dataset — Formula 1 World Championship (Kaggle)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)
- [Histórico de motores da F1](https://medium.com/formula-one-forever/the-evolution-of-formula-1-engines-from-water-pumps-to-hybrids-6a9bb59c50d6)
