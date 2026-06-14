import pandas as pd
import numpy as np
import sqlite3


# Lê os dados do staging.db para serem transformados
def read_staging(table_name: str) -> pd.DataFrame:
    conn = sqlite3.connect("databases/staging.db")

    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    print (
        f"✓ {table_name}: {df.shape[1]} colunas"
    )
    conn.close()
    return df


# Remove colunas desnecessárias das tabelas, ou seja, colunas que não serão usadas nas análises.
def transform_circuits() -> pd.DataFrame:
    df = read_staging("circuits")
    
    drop_cols = [
        "circuitRef", 
        "alt", 
        "url"
    ]
    df = df.drop(columns=drop_cols)
    
    print(f"✓ circuits: removidas {drop_cols} → {df.shape[1]} colunas restantes")
    return df


def transform_races() -> pd.DataFrame:
    df = read_staging("races")
    
    drop_cols = [
         "url", 
        "fp1_date", 
        "fp1_time",
        "fp2_date", 
        "fp2_time",
        "fp3_date", 
        "fp3_time",
        "quali_date", 
        "quali_time",
        "sprint_date", 
        "sprint_time"
    ]
  
    df = df.drop(columns=drop_cols)

    print(f"✓ races: removidas {drop_cols} → {df.shape[1]} colunas restantes")
    return df


def transform_drivers() -> pd.DataFrame:
    df = read_staging("drivers")
    
    drop_cols = [
        "driverRef",
        "url"
    ]
    df = df.drop(columns=drop_cols)
    print(f"✓ drivers: removidas {drop_cols} → {df.shape[1]} colunas restantes")
    return df


def transform_constructors() -> pd.DataFrame:
    df = read_staging("constructors")
    drop_cols = [
        "constructorRef",
        "url"
    ]
    df = df.drop(columns=drop_cols)
    print(f"✓ constructors: removidas {drop_cols} → {df.shape[1]} colunas restantes")
    return df


def transform_results() -> pd.DataFrame:
    df = read_staging("results")
    drop_cols = [
        "positionOrder",
    ]
    df = df.drop(columns=drop_cols)
    print(f"✓ results: removidas {drop_cols} → {df.shape[1]} colunas restantes")
    return df


def transform_driver_standings() -> pd.DataFrame:
    df = read_staging("driver_standings")
    drop_cols = [
        "positionText",
    ]
    df = df.drop(columns=drop_cols)
    print(f"✓ driver_standings: removidas {drop_cols} → {df.shape[1]} colunas restantes")
    
    return df


# Cria uma tabela para identificar as eras da F1, com base nos anos das corridas. 
# Essa tabela será usada para associar cada corrida a uma era, o que permitirá análises por era posteriormente.
def create_dim_era() -> pd.DataFrame:
    conn = sqlite3.connect("databases/staging.db")
    df = pd.DataFrame({
        "eraId": [1, 2, 3, 4, 5, 6],
        "eraName": ['Era Clássica', 'Era DFV', 'Era Turbo', 'Era Aspirada', 'Era V8', 'Era Híbrida'],
        "motorType": ['Diversos', 'V8 Cosworth', 'Turbo V6', 'V8/V10/V12', 'V8', 'V6 Turbo Híbrido'],
        "startYear": [1950, 1966, 1977, 1989, 2006, 2014],
        "endYear": [1965, 1976, 1988, 2005, 2013, 2024]
    })

    df.to_sql("dim_era", conn, if_exists="replace", index=False)
    print(f"✓ dim_era criada: {df.shape[0]} linhas, {df.shape[1]} colunas")
    conn.close()
    
    return df


# Associa cada corrida a uma era, com base no ano da corrida. 
def add_era_to_races(races_df, era_df):
    conditions = [
        (races_df["year"] >= 1950) & (races_df["year"] <= 1965),
        (races_df["year"] >= 1966) & (races_df["year"] <= 1976),
        (races_df["year"] >= 1977) & (races_df["year"] <= 1988),
        (races_df["year"] >= 1989) & (races_df["year"] <= 2005),
        (races_df["year"] >= 2006) & (races_df["year"] <= 2013),
        (races_df["year"] >= 2014) & (races_df["year"] <= 2024),
    ]
    
    choices = [1, 2, 3, 4, 5, 6]
    
    races_df["eraId"] = np.select(conditions, choices, default=0)
    
    associacoes = races_df.groupby("eraId").size()
    print(f"✓ eras associadas às corridas:")
    for era_id, qtd in associacoes.items():
        era_nome = era_df[era_df["eraId"] == era_id]["eraName"].values[0]
        print(f"   {era_nome}: {qtd} corridas")
        
    return races_df


# Função principal que executa todas as transformações.
def transform_all():
    circuits = transform_circuits()
    races = transform_races()
    drivers = transform_drivers()
    constructors = transform_constructors()
    results = transform_results()
    driver_standings = transform_driver_standings()
    dim_era = create_dim_era()
    races = add_era_to_races(races, dim_era)
    
    dados = {
        "circuits": circuits,
        "races": races,
        "drivers": drivers,
        "constructors": constructors,
        "results": results,
        "driver_standings": driver_standings,
        "dim_era": dim_era
    }
    
    print("\n✓ Transform concluído!")
    for tabela, df in dados.items():
        print(f"   {tabela}: {df.shape[0]} linhas, {df.shape[1]} colunas")
        
    return dados