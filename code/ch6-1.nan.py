"""
누락값 처리하기
: NaN, NAN, nan
: 데이터 자체가 없다. '같다'라는 개념도 없다. 비교 대상도 없다
"""


### 06-1 누락값이란?

from numpy import NaN, NAN, nan
import numpy as np
import pandas as pd

path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'

# 누락값과 누락값 확인하기
print(NaN == True, NaN == False, NaN == 0, NaN == '',  NaN == NaN)

print(pd.isnull(NaN))                                   # 누락값 검사
print(pd.notnull(NaN))
print(pd.notnull(42))
print(pd.notnull('missing'))


# 누락값이 생기는 이유 알아보기
survey = pd.read_csv(path + 'data/survey_survey.csv')
visited = pd.read_csv(path + 'data/survey_visited.csv')

print(visited)
print(survey)

#1. 누락값이 있는 데이터 집합을 연결할 때 누락값이 생기는 경우
v2s = visited.merge(survey, left_on='ident', right_on='taken')
print(v2s)

#2. 데이터프레임에 없는 열과 행 데이터를 입력할 때 누락값이 생기는 경우
nan_series = pd.Series({'goat': 4, 'amoeba': nan})
print(nan_series)
print(type(nan_series))

nan_df = pd.DataFrame({
    'Name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'missing': [NaN, nan]})
print(nan_df)
print(type(nan_df))

#3. 범위를 지정하여 데이터를 추출할 때 누락값이 생기는 경우
gapminder = pd.read_csv(path + 'data/gapminder.tsv', sep='\t')

life_exp = gapminder.groupby(['year'])['lifeExp'].mean()
print(life_exp)

print(life_exp.loc[range(2000, 2010), ])

y2000 = life_exp[life_exp.index > 2000]             # 불린을 이용한 추출
print(y2000)



# 누락값의 개수 구하기
ebola = pd.read_csv(path + 'data/country_timeseries.csv')

print(ebola.count())                                # 누락값이 아닌 값의 개수
num_rows = ebola.shape[0]                           # 전체 행의 개수
num_missing = num_rows - ebola.count()              # 누락값 개수
print(num_missing)

print(np.count_nonzero(ebola.isnull()))                        # count_nonzero() 0이 아닌 값의 개수
print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))

print(ebola.Cases_Guinea.value_counts(dropna=False).head())    # value_counts() 지정한 열의 빈도 수


# 누락값 변경하기
print(ebola.fillna(0).iloc[0:10, 0:5])                  # 누락값 0으로 변경하기
print(ebola.fillna(method='ffill').iloc[0:10, 0:5])     # 누락값이 나타나기 전 값으로 변경하기
print(ebola.fillna(method='bfill').iloc[0:10, 0:5])     # 누락값이 나타난 후 첫번째 값으로 변경하기
print(ebola.interpolate().iloc[0:10, 0:5])              # 누락값이 나타나기 전 후 중간값으로 변경하기


# 누락값 삭제하기
print(ebola.shape)

ebola_dropna = ebola.dropna()                           # 누락값 삭제하기
print(ebola_dropna.shape)
print(ebola_dropna)


# 누락값이 포함된 데이터 계산하기
ebola['Cases_multiple'] = ebola['Cases_Guinea'] + ebola['Cases_Liberia'] + ebola['Cases_SierraLeone']
ebola_subset = ebola.loc[:, ['Cases_Guinea', 'Cases_Liberia', 'Cases_SierraLeone', 'Cases_multiple']]
print(ebola_subset.head(n=10))

print(ebola.Cases_Guinea.sum(skipna = True))            # 누락값을 무시하고 계산
print(ebola.Cases_Guinea.sum(skipna = False))           # 누락값이 포함되어 계산하면 누락값



