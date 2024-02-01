import csv
import matplotlib.pyplot as plt

f = open('../../CSV_files/1일차-기온데이터/daegu-utf8.csv', encoding='utf-8-sig')
data  = csv.reader(f)

header = next(data)
result = []

for row in data:
    if row[4] != '':
        result.append(float(row[4]))

print(len(result))
f.close()

plt.figure(figsize=(25, 3))
plt.plot(result, c='r')
plt.show()