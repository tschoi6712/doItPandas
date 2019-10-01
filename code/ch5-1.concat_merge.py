"""
데이터 연결하기
: tidy data - table, row(측정한 값), column(변수)
: pd.concat()
"""

### 05-2 데이터 연결 기초

import pandas as pd

# concat 메서드로 데이터 연결하기: 위에서 아래 방향으로
path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'

df1 = pd.read_csv(path + 'data/concat_1.csv')
df2 = pd.read_csv(path + 'data/concat_2.csv')
df3 = pd.read_csv(path + 'data/concat_3.csv')

row_concat = pd.concat([df1, df2, df3])
print(row_concat)

print(row_concat.iloc[3, ])


# 데이터프레임에 시리즈 연결하기
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])            # 리스트를 시리즈로 변환
print(pd.concat([df1, new_row_series]))                         # 새로운 열 추가가


# 행 1개로 구성된 데이터프레임(시리즈) 생성하여 연결하기
new_row_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']], columns=['A', 'B', 'C', 'D'])
print(new_row_df)
print(pd.concat([df1, new_row_df]))
print(df1.append(new_row_df))

data_dict = {'A': 'n1', 'B': 'n2', 'C': 'n3', 'D': 'n4'}        # .append(딕셔너리)
print(df1.append(data_dict, ignore_index=True))                 # 인덱스를 0부터 다시 지정


# 다양한 방법으로 데이터 연결하기
row_concat_i = pd.concat([df1, df2, df3], ignore_index=True)    # ignore_index 인자 사용하기
print(row_concat_i)

col_concat = pd.concat([df1, df2, df3], axis=1)                 # 열 방향으로 데이터 연결하기
print(col_concat)

print(col_concat['A'])                                          # 열 이름으로 데이터 추출

col_concat['new_col_list'] = ['n1', 'n2', 'n3', 'n4']           # 새로운 열 추가
print(col_concat)

print(pd.concat([df1, df2, df3], axis=1, ignore_index=True))    # 열 이름 다시 지정


# 공통 열과 공통 인덱스만 연결하기
df1.columns = ['A', 'B', 'C', 'D']                              # 열 이름 재 지정
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

print(df1)
print(type(df1))
print(df2)
print(type(df2))
print(df3)
print(type(df3))

row_concat = pd.concat([df1, df2, df3])                         # 데이터프레임에 없는 열 이름은 NaN 발생
print(row_concat)

print(pd.concat([df1, df2, df3], join='inner'))                 # 공통 열만 골라서 연결 : join='inner'
print(pd.concat([df1,df3], ignore_index=False, join='inner'))


df1.index = [0, 1, 2, 3]                                        # 인덱스 재 지정
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]

print(df1)
print(df2)
print(df3)

col_concat = pd.concat([df1, df2, df3], axis=1)                 # 행 방향을 연결 : 누락값 발생
print(col_concat)

print(pd.concat([df1, df3], axis=1, join='inner'))              # 공통 행만 골라서 연결 : join='inner'















