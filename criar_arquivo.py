import os

file_path = 'dados.csv'

# Verifica se o arquivo CSV existe
if not os.path.exists(file_path):
    # Cria o arquivo CSV
    open(file_path, mode='w').close()
else:
    print("O Arquivo ja existe!")