import csv

my_family = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
        ]

with open('export.csv', 'w', encoding = 'utf-8') as e:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(e, fields, delimiter=';', lineterminator='\n')
    writer.writeheader()
    for member in my_family:
        writer.writerow(member)
       
