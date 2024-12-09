



import pandas as pd
import os

# Definir o caminho do arquivo CSV de entrada
input_csv = r"C:\Users\matheus.weinert\Downloads\CDR_VIVO\TELECALL_DADOS_20231229\TELECALL_DADOS_20231229.csv"

# Definir o diretório de saída e o nome do arquivo Parquet
output_dir = r"C:\Users\matheus.weinert\Downloads\CDR_VIVO\TELECALL_DADOS_20231229"
output_file = "CDR_VIVO.parquet"

# Criar o diretório de saída, se não existir
os.makedirs(output_dir, exist_ok=True)

# Ler o arquivo CSV
df = pd.read_csv(input_csv)

# Salvar como Parquet na pasta especificada
output_path = os.path.join(output_dir, output_file)
df.to_parquet(output_path, engine="pyarrow", compression="snappy")

print(f"Arquivo Parquet salvo em: {output_path}")
