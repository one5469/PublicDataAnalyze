import csv

f = open('../../CSV_files/1일차-기온데이터/daegu-utf8.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
print(data)

count = 0
for row in data:
    if count > 5:
        break
    else:
        print(row)
        count += 1

f.close()