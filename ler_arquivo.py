import csv

# Localização do arquivo
file_path = 'dados.csv'

# Ler o Arquivo CSV
with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)