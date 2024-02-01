import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def checkDecimal(msg):
    if not msg.isdecimal():
        print('숫자를 입력해야 합니다.')
        exit(1)

# 데이터프레임 불러오기
df = pd.read_csv('../daegu_utf-8-df.csv', encoding='utf-8-sig', parse_dates=['날짜'])

# 표준 입력 받기
start_year = input('시작 연도를 입력하세요: ')
checkDecimal(start_year)
end_year = input('마지막 연도를 입력하세요: ')
checkDecimal(end_year)
month = input('기온 변화를 측정할 달을 입력하세요: ')
checkDecimal(month)

# 입력값들을 int형으로 형변환
start_year, end_year, month = map(int, [start_year, end_year, month])

# 최저기온 평균과 최고기온 평균의 리스트 생성
mean_max = []
mean_min = []

for y in range(start_year, end_year+1):
    yearDF = df[(df['날짜'].dt.year == y) & (df['날짜'].dt.month == month)]     # 해당 년도와 해당 달에 해당하는 데이터프레임 추출
    mean_min.append(round(yearDF['최저기온'].mean(), 1))     # 최저기온의 평균 저장
    mean_max.append(round(yearDF['최고기온'].mean(), 1))     # 최고기온의 평균 저장

# 출력하기
print(f'{start_year} 년부터 {end_year} 년까지 {month} 월의 기온 변화')
print(f'{month} 월 최저기온 평균:')
for i in mean_min:
    print(i, end=' ')
print()

print(f'{month} 월 최고기온 평균:')
for i in mean_max:
    print(i, end=' ')

# 그래프 그리기
plt.figure(figsize=(16, 4))
plt.plot(range(start_year, end_year+1), mean_max, color='r', marker='s')
plt.plot(range(start_year, end_year+1), mean_min, color='b', marker='s')
plt.title(f'{start_year}년부터 {end_year}년까지 {month}월의 기온 변화')
plt.legend(['최고기온', '최저기온'], loc=2)
plt.show()