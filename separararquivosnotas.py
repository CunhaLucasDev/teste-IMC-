import os
import re
import pandas as pd

# Caminho para a pasta onde os arquivos já estão descompactados
folder_path = r"C:\Users\cunha\Downloads\ADDILIFE NOTAS ENTRADAS (1).rar\ADDILIFE NOTAS ENTRADAS"

# Verificar se a pasta existe
if not os.path.exists(folder_path):
    raise FileNotFoundError(f"A pasta especificada não foi encontrada: {folder_path}")
print(f"Pasta encontrada: {folder_path}")

# Verificar se a pasta contém arquivos
arquivos = os.listdir(folder_path)
if not arquivos:
    raise FileNotFoundError(f"A pasta especificada está vazia: {folder_path}")
print(f"Arquivos encontrados na pasta: {arquivos}")

# Lista para armazenar os números extraídos
numbers = []

# Iterar pelos arquivos na pasta
for file_name in arquivos:
    print(f"Processando arquivo: {file_name}")
    # Extrair números do nome do arquivo
    match = re.findall(r'\d+', file_name)
    if match:
        print(f"Números encontrados no arquivo '{file_name}': {match}")
        numbers.extend(match)

# Verificar se números foram encontrados
if not numbers:
    raise ValueError("Nenhum número foi encontrado nos nomes dos arquivos.")
print(f"Números extraídos: {numbers}")

# Remover duplicados e ordenar os números
numbers = sorted(set(numbers))
print(f"Números únicos e ordenados: {numbers}")

# Criar um DataFrame do pandas
df = pd.DataFrame(numbers, columns=["Números"])

# Salvar em uma planilha Excel
output_excel_path = r"C:\Users\cunha\Downloads\numeros_notas.xlsx"
df.to_excel(output_excel_path, index=False)

print(f"Planilha criada com sucesso em: {output_excel_path}")