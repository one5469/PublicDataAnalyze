import csv

def get_minmax_temp(data):

    header = next(data)

    min_temp = 1000
    min_date = ''

    max_temp = -999
    max_date = ''

    for row in data:
        if row[3] == '':
            row[3] = 1000
        row[3] = float(row[3])

        if row[4] == '':
            row[4] = -999
        row[4] = float(row[4])

        if row[3] < min_temp:
            min_temp = row[3]
            min_date = row[0]

        if row[4] > max_temp:
            max_temp = row[4]
            max_date = row[0]

    print('---')
    print(f'대구 최저 기온 날짜: {min_date}, 온도: {min_temp}')
    print(f'대구 최고 기온 날짜: {max_date}, 온도: {max_temp}')


def main():
    f = open('../../CSV_files/1일차-기온데이터/daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    get_minmax_temp(data)
    print()
    f.close()


main()