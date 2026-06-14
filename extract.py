import kagglehub
import shutil
import os
import pandas as pd
import sqlite3

# Baixa os arquivos csv do Kaggle e move para a pasta 'data/'
def get_dataset(): 
    path = kagglehub.dataset_download(
        "rohanrao/formula-1-world-championship-1950-2020"
    )
    print("✓ Dataset baixado")
    
    os.makedirs("data/", exist_ok=True)
    
    shutil.copytree(path, "data/", dirs_exist_ok=True)
    print("✓ Dataset movido para data/")


# Lista dos arquivos csv do dataset para serem processados, somente os arquivos que usaremos nas analises. 
# O dataset tem mais arquivos, mas esses são os principais para o nosso projeto.
ARQUIVOS = [
    "circuits", "races", "results", "drivers",
    "constructors", "qualifying", "driver_standings"
]


# Extrai os dados dos arquivos csv e grava no banco de dados staging.db, atribuindo null pra os valores \N.
def extract_data():
    os.makedirs("databases/", exist_ok=True)
    
    conn = sqlite3.connect("databases/staging.db")
    
    for arquivo in ARQUIVOS:
        df = pd.read_csv(f"data/{arquivo}.csv", na_values="\\N")
        df.to_sql(arquivo, conn, if_exists="replace", index=False)
        print(f"✓ {arquivo}: {df.shape[0]} linhas e {df.shape[1]} colunas gravadas no staging")
    
    conn.close()
    print("\n✓ Staging concluído!")