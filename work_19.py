import csv
with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as new_file:
    my_files = new_file.readlines()
    for line in my_files:
        homework_files = line.strip().split(';')

        if homework_files[5] == 'UA':

            print(homework_files)
