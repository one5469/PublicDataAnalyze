import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 데이터프레임 불러오기
df = pd.read_csv('../daegu_utf-8-df.csv', encoding='utf-8-sig', parse_dates=['날짜'])

# 지난 10년간의 데이터만 가져오기
df2 = df[(df['날짜'].dt.year >= 2014) & (df['날짜'].dt.year <= 2023)]
df2.set_index('날짜')

# DF 연산을 이용해 일교차 시리즈 객체 생성
gapSR = df2['최고기온'] - df2['최저기온']
# 기존의 데이터프레임과 일교차 시리즈 병합
df_gap = pd.concat([df2, gapSR], axis=1)
df_gap.columns = ['날짜', '지점', '평균기온', '최저기온', '최고기온', '일교차']
print(df_gap)

# 빈 데이터프레임 생성
max_gap_DF = pd.DataFrame()

# 일교차가 가장 큰 열 하나씩 병합하기
for y in range(2014, 2024):
    yearDF = df_gap[df_gap['날짜'].dt.year == y]
    max_row = yearDF[yearDF['일교차'] == yearDF['일교차'].max()]
    max_gap_DF = pd.concat([max_row, max_gap_DF])

print(max_gap_DF)

# 그래프 생성
max_gap_DF.sort_index(inplace=True)
xaxis = [f'{dt.year}.{dt.month}' for dt in max_gap_DF['날짜']]
plt.figure(figsize=(12, 5))
plt.bar(xaxis, max_gap_DF['일교차'])
plt.title('지난 10년간 대구의 일교차가 가장 큰 달')
plt.ylabel('일교차')
plt.xlabel('Year/Month')
plt.show()