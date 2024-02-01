from copy import deepcopy

sq_dict = {}        # 마방진 딕셔너리 생성
reverse_dict = {}

# 입력 조건
while True:
    size = input('홀수차 배열의 크기를 입력하세요: ')
    if not size.isdecimal():
        print('숫자를 입력해야 합니다. 다시 입력하세요.')
    elif int(size) % 2 == 0:
        print('짝수를 입력하였습니다. 다시 입력하세요.')
    else:
        size = int(size)
        break

limit = size * size             # 최대 번호
loc = [0, size//2]              # 처음 위치
sq_dict[1] = deepcopy(loc)      # 1번 위치 저장

# 2번부터 순회
for i in range(2, limit+1):
    # 기본 진행 조건
    loc[0] -= 1
    loc[1] += 1

    if loc[0] < 0 and loc[1] >= size:   # 접한 행열이 없을때
        loc[0] += 2
        loc[1] -= 1
    if loc[0] < 0:                      # y축을 벗어났을 때
        loc[0] = size-1
    if loc[1] >= size:                  # x축을 벗어났을 때
        loc[1] = 0
    if loc in sq_dict.values():         # 이미 자리가 있을 때
        loc[0] += 2
        loc[1] -= 1

    sq_dict[i] = deepcopy(loc)          # 마방진 딕셔너리에 현재 번호 저장

# 출력을 위해 키와 값을 뒤집은 딕셔너리 생성
for k, v in sq_dict.items():
    reverse_dict[tuple(v)] = k

# print(sq_dict)
# print(reverse_dict)
print(f'Magic Square ({size}X{size})')

r, c = 0, 0

while r < size:
    print(f'{reverse_dict[(r, c)]:>2}', end=' ')
    # print(r,c)

    c += 1
    if c >= size:
        print()
        c = 0
        r += 1

