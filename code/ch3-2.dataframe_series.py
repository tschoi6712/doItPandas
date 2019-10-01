"""
Series([data, index, dtype, name, copy, …])	One-dimensional ndarray with axis labels (including time series)
DataFrame([data, index, columns, dtype, copy])	Two-dimensional size-mutable, potentially heterogeneous tabular data
                                                structure with labeled axes (rows and columns).
"""


### 03-2 시리즈 다루기 - 기초

import pandas as pd

# 데이터프레임에서 시리즈 선택하기
df_2 = pd.DataFrame(
        data={'Occupation': ['Chemist', 'Statistician'],
            'Born': ['1920-07-25', '1876-06-13'],
            'Died': ['1958-04-16', '1937-10-16'],
            'Age': [37, 61]},
        index=['Rosaline Franklin', 'William Gosset'],
        columns=['Occupation', 'Born', 'Age', 'Died'])
print(df_2)

first_row = df_2.loc['William Gosset']
print(type(first_row))
print(first_row)


# 시리즈 index, values 속성과 keys 메서드 사용하기
print(first_row.index)
print(first_row.values)
print(first_row.keys())

print(first_row.index[0])
print(first_row.keys()[0])


# 시리즈의 mean, min, max, std, median, sample 메서드 사용하기
ages = df_2['Age']
print(ages)

print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.sample())
"""
.append(), .describe(), .drop_duplicates(), .equals(), .get_values(), .isin(), .replace(), .sort_values(), .to_frame() 
"""


### 03-3 시리즈 다루기 - 응용

import pandas as pd

# 시리즈와 불린 추출 사용하기
path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'
scientists = pd.read_csv(path + 'data/scientists.csv')
ages = scientists['Age']

print(ages > ages.mean())
bool_values = [True, True, False, False, True, True, False, True]
print(ages[bool_values])

print(ages[ages > ages.mean()])


# 벡터와 스칼라로 브로드캐스팅 수행하기(한 번에 연산하기)
print(ages + ages)                      # 같은 길이를 가진 백터와 백터의 연산
print(ages * ages)

print(ages + 100)                       # 백터와 스칼라의 연산
print(ages * 2)

print(ages + pd.Series([1, 100]))       # 길이가 서로 다른 벡터를 연산 - 일치한 인덱스만 계산하고 나머지는 NaN 반환

rev_ages = ages.sort_index(ascending=False)
print(rev_ages)                         # 인덱스 역순으로 데이터 정렬
print(ages)

print(ages + rev_ages)                  # 백터와 백터의 연산은 일치하는 인덱스의 값끼리 수행


### 03-4 데이터프레임 다루기

# 불린 추출과 브로드캐스팅
print(scientists[scientists['Age'] > scientists['Age'].mean()])

print(scientists.loc[[True, True, False, True]])

print(scientists * 2)                   # 데이터프레임의 모든 요소에 스칼라를 적용(문자열은 숫자의 배로 증가)


### 03-5 시리즈와 데이터프레임의 데이터 처리하기

# 열의 자료형 바꾸기와 새로운 열 추가하기
print(scientists['Born'].dtype)
print(scientists['Died'].dtype)

born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
print(born_datetime)
died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
print(died_datetime)

scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
print(scientists.head())
print(scientists.shape)

# 시간 계산
scientists['age_days_dt'] = (scientists['died_dt'] - scientists['born_dt'])
print(scientists)

# 시리즈, 데이터프레임의 데이터 섞기
print(scientists['Age'])

import random

random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])

# 데이터프레임의 열 삭제하기: .drop(삭제할 열이름, axis=1)
print(scientists.columns)

scientists_dropped = scientists.drop(['Age'], axis=1)
print(scientists_dropped.columns)


### 03-6 데이터를 피클, CSV, TSV 파일로 저장하고 불러오기

# 피클로 저장하기: 데이터를 바이너리 형태로 직렬화한 오브젝트
path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'

names = scientists['Name']
names.to_pickle(path + 'output/scientists_names_series.pickle')         # 시리즈를 피클로 저장

scientists.to_pickle(path + 'output/scientists_df.pickle')              # 데이터프레임을 피클로 저장

names_from_pickle = pd.read_pickle(path + 'output/scientists_names_series.pickle')
print(names_from_pickle)

scientists_from_pickle = pd.read_pickle(path + 'output/scientists_df.pickle')
print(scientists_from_pickle)


# CSV 파일과 TSV 파일로 저장하기
names.to_csv(path + 'output/scientist_names_series.csv')
scientists.to_csv(path + 'output/scientists_df.tsv', sep='\t')
scientists.to_csv(path + 'output/scientists_df_no_index.csv', index=False)


# 엑셀 파일로 저장하기 : pip install openpyxl
import openpyxl

names_df = names.to_frame()
names_df.to_excel(path + 'output/scientists_names_series_df.xlsx')






