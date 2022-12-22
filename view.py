def view_data(solution: int):
    print(solution)

def get_solution():
    return int(input('Выберите режим работы (1 - import, 2 - export): '))

def get_soname():
    return input('Введите фамилию: ')

def get_format():
    return int(input('Выберите формат файла (1 - csv, 2 - txt): '))
    