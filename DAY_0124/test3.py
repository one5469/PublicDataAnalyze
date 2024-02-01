import csv

fin = open('../../CSV_files/1일차-기온데이터/daegu.csv', 'r', encoding='utf-8-sig')
data = csv.reader(fin, delimiter=',')

fout = open('../../CSV_files/1일차-기온데이터/daegu-utf8.csv', 'w', newline='', encoding='utf-8-sig')
wr = csv.writer(fout)

for row in data:
    for i in range(len(row)):
        row[i] = row[i].replace('\t', '')
    print(row)
    wr.writerow(row)

fin.close()
fout.close()