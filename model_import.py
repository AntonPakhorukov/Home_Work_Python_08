import csv

def import_data_csv(any_name: str):
    result = []
    count = 0
    with open('data.csv', 'r', encoding='utf-8') as d:
        reader = csv.DictReader(d, delimiter = ' ')
        for row in reader:
            result.append(row)
        for find in result:
            if find['Фамилия'] == any_name:
                print(find['Фамилия'] + ' ' + find['Имя'] + ' ' + find['Отчество'] + ' ' + find['Телефон'] + ' ' + find['Примечание'])
                count += 1               
        else:
            if count == 0:
                print('Нет таких данных')

def import_data_txt(any_name: str):
    index = 0
    with open('file.txt', 'r', encoding='utf-8') as data:
        reader = data.readlines()
        for row in reader:
            if any_name in row:
                print(row, end='')
                index += 1
        else:
            if index == 0:
                print('Нет таких данных')