import csv

import pandas as pd
pd.options.display.width = None

first_letter = input('Введите первую букву имени и нажмите Enter:')
def write_holiday_cities(first_letter):
    list_cities = []
    with open('travel_notes.csv', 'r') as file:
        reader = csv.reader(file)
        #reader1 = sort(reader,  key=lambda row: row[1])
        for row in reader:
            if first_letter in row[0]:
                return row
    return None

result = list(write_holiday_cities(first_letter))

if result:
    result_1 = [
        f'{first_letter}\n'
        f'Посетили: {sorted(result[1].split(';'))}\n'
        f'Хотят посетить: {sorted(result[2].split(';'))}\n'
        f'Никогда не были в: {sorted(result[2].split(';'))}\n'
        f'Следующим городом будет: {result[2].split(';')[0]}'
    ]
    with open('holiday.csv', 'w', encoding='utf8', newline='') as file:

        writer = csv.writer(file)

        writer.writerows([result_1])


else:
    print('Нет имени начинающегося с этой буквы.')






