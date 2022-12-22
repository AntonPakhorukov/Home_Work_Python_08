import csv

def export_data_csv():
    with open('data.csv', 'a', newline='', encoding='utf-8') as d:
        write = csv.writer(d)
        write.writerow(input('Введите данные: ').split(', '))
        
def export_data_txt():
    info = input('Введите данные: ')
    with open('file.txt', 'a', encoding='utf-8') as data:
        data.writelines(info + '\n')
        