import extract
import transform
import load
#import analyze

if __name__ == "__main__":
    # 1. Baixa e carrega no staging.db 
    extract.get_dataset()
    extract.extract_data()
    
    # 2. Transforma os dados
    dados = transform.transform_all()
    
    # 3. Carrega no datawarehouse.db
    load.create_tables()
    load.insert_data(dados)
  