import sqlite3
import pandas as pd

def create_tables():
    conn = sqlite3.connect("databases/datawarehouse.db")
    
    # Lê e executa a migration
    with open("migration.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    
    conn.close()
    print("✓ Migration executada — tabelas criadas com PKs e FKs!")


def insert_data(dados: dict):
    conn = sqlite3.connect("databases/datawarehouse.db")
    
    dados["dim_era"].to_sql("dim_era", conn, if_exists="append", index=False)
    print(f"✓ dim_era: {len(dados['dim_era'])} linhas carregadas")
    
    dados["circuits"].to_sql("dim_circuito", conn, if_exists="append", index=False)
    print(f"✓ dim_circuito: {len(dados['circuits'])} linhas carregadas")
    
    dados["drivers"].to_sql("dim_piloto", conn, if_exists="append", index=False)
    print(f"✓ dim_piloto: {len(dados['drivers'])} linhas carregadas")
    
    dados["constructors"].to_sql("dim_equipe", conn, if_exists="append", index=False)
    print(f"✓ dim_equipe: {len(dados['constructors'])} linhas carregadas")
    
    dados["races"].to_sql("dim_temporada", conn, if_exists="append", index=False)
    print(f"✓ dim_temporada: {len(dados['races'])} linhas carregadas")
    
    dados["results"].to_sql("fato_resultado", conn, if_exists="append", index=False)
    print(f"✓ fato_resultado: {len(dados['results'])} linhas carregadas")
    
    dados["driver_standings"].to_sql("fato_standings", conn, if_exists="append", index=False)
    print(f"✓ fato_standings: {len(dados['driver_standings'])} linhas carregadas")
    
    conn.close()
    print("\n✓ Datawarehouse carregado!")