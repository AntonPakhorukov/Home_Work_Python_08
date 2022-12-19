import csv

def export_data():
    with open('data.csv', 'a', newline='', encoding='utf-8') as d:
        write = csv.writer(d)
        write.writerow(input('Введите данные: ').split(', '))
        