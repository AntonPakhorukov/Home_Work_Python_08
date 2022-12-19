import csv

def import_data(any_name: str):
    result = []
    with open('data.csv', 'r', encoding='utf-8') as d:
        reader = csv.DictReader(d, delimiter = ' ')
        for row in reader:
            result.append(row)
        for find in result:
            if find['Фамилия'] == any_name:
                print(find)
        
        