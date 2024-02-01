import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 데이터 프레임 불러오기
DF =  pd.read_csv('../../CSV_files/gender.csv', encoding='utf-8-sig', usecols=['행정기관', '총 인구수','남 인구수', '여 인구수'])
# 각 구별 이름 리스트
dis_list = ['  ', ' 중구 ', ' 서구 ', ' 동구 ', ' 남구 ', ' 북구 ', ' 수성구 ', ' 달서구 ' ,' 달성군 ']

# 각 구역의 정보를 담을 딕셔너리
dis_dict = {}

# 이름 리스트 순회
for dis in dis_list:
    area = '대구광역시'+dis     # 구역 이름 생성
    areaDF = DF[DF['행정기관'] == area]     # 구역 이름에 해당하는 데이터프레임 추출
    # 구역별 인구 정보를 딕셔너리에 저장
    dis_dict[area] = [areaDF.iloc[0]['총 인구수'].replace(',', ''), areaDF.iloc[0]['남 인구수'].replace(',', ''), areaDF.iloc[0]['여 인구수'].replace(',', '')]

# subplot 인덱스
subplot_idx = 1

# 구역 딕셔너리 순회
for k, v in dis_dict.items():
    plt.subplot(3, 3, subplot_idx)
    plt.pie([int(v[1]), int(v[2])], labels=['남성', '여성'], autopct='%.1f%%', startangle=90,  textprops={'fontsize': 6})
    plt.title(k, fontsize=7)

    subplot_idx += 1

plt.suptitle('대구광역시 구별 남녀 인구 비율', fontsize=14)
plt.show()