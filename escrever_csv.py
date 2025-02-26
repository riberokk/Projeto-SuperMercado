import csv

data = [
    ['Nome', 'Idade', 'Cidade'],
    ['Pedro', '17', 'Jundiai'],
    ['Marcos', '17', 'Barretos']
]

file_path = 'dados.csv'

with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)