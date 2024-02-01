import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('../../CSV_files/1일차-기온데이터/daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data:
    month = row[0].split('-')[1]
    if row[-1] != '':
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))

f.close()
plt.hist(aug, bins=100, color='tomato')
plt.hist(jan, bins=100, color='b')
plt.xlabel("Temperature")
plt.rc("axes", unicode_minus=False)
plt.show()