"""
Python Data Analysis Library
https://pandas.pydata.org
"""


### 02-1 갭마인더 데이터 집합 불러오기
"""
갭마인더(Gapminder)의 데이터 집합 - country,continent,year,lifeExp, pop, gdpPercap
.read_csv(파일명) - 데이터를 읽어서 데이터프레임 자료형으로 반환
"""

import pandas as pd
path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'
df = pd.read_csv(path + 'data/gapminder.tsv', sep='\t')


# 불러온 데이터 집합 살펴보기
print(df.head())                # 가장 앞에 있는 5개 형을 출력
print(type(df))                 # 자료형
print(df.shape)                 # 데이터의 행과 열의 크기
print(df.columns)               # 열 이름
print(df.dtypes)                # 데이터프레임을 구성하는 값의 자료형
print(df.info())


### 02-2 데이터 추출하기
country_df = df['country']                      # 1개 열 단위로 데이터 추출하기
print(type(country_df))
print(country_df.head())
print(country_df.tail())

subset = df[['country', 'continent', 'year']]   # 여러 개 열 단위로 데이터 추출하기
print(type(subset))
print(subset.head())
print(subset.tail())

"""
# 행 단위 데이터 추출하기
.loc[] - 인덱스 기준, 0 부터 시작하지만 데이터의 추가, 삭제에 의해 변경 가능 문자열도 사용
.iloc[] - 행 번호(데이터의 순서) 기준
"""
print(df.loc[0])                                # 인덱스가 0인 행
print(df.loc[99])
#print(df.loc[-1])                               # KeyError: 'the label [-1] is not in the [index]'

number_of_rows = df.shape[0]                    # 행의 크기
last_row_index = number_of_rows - 1             # 마지막 행의 인덱스 구하기
print(df.loc[last_row_index])                   # 마지막 행의 데이터 추출{시리즈}

print(df.tail(n=1))                             # 마지막 행의 데이터 추출{데이터프레임}

print(df.loc[[0, 99, 999]])                     # 여러 인덱스(리스트)의 데이터를 추출


print(df.iloc[1])                               # # 행 번호가 1인 행
print(df.iloc[99])
print(df.iloc[-1])                              # 마지막 행의 데이터 추출{시리즈}
#print(df.iloc[1710])                            # IndexError: single positional indexer is out-of-bounds

"""
# 슬라이싱 구문으로 데이터 추출하기 - loc, iloc 속성
# range 메서드로 원하는 데이터 추출하기 - iloc 속성
"""
slicing_1 = df.loc[:, ['year', 'pop']]          #
print(slicing_1.head())

slicing_2 = df.iloc[:, [2, 4, -1]]              #
print(slicing_2.head())

small_range = list(range(0, 6, 2))
slicing_3 = df.iloc[:, small_range]             # range 메서드는 제너레이터를 반환
print(slicing_3.head())

slicing_4 = df.iloc[:, 0:6:2]
print(slicing_4.head())

print(df.iloc[[0, 99, 999], [0, 3, 5]])
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])


### 02-3 기초적인 통계 계산하기
"""
DataFrame.groupby("기준이 될 컬럼명")
"""
print(df.head(n=10))

# lifeExp 열을 연도별로 그룹화하여 평균 계산하기
grouped_year_df = df.groupby('year')            # 연도별로 그룹화하기
print(type(grouped_year_df))

lifeExp = grouped_year_df['lifeExp']            # 그룹화한 데이터프레임에서 lifeExp 열 추출
print(type(lifeExp))

mean_lifeExp = lifeExp.mean()                   # 연도별로 그룹화한 lifeExp 열의 평균값 계산하기
print(mean_lifeExp)

print(df.groupby('year')['lifeExp'].mean())


# lifeExp, gdpPercap 열의 평균값을 연도, 지역별로 그룹화하여 한 번에 계산하기
multi_groupby = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(multi_groupby)

# continent 열을 그룹화하여 데이터의 개수 세기
print(df.groupby('continent')['country'].nunique())


### 02-4 그래프 그리기
"""
%matplotlib --list
%matplotlib inline   [in a GUI console, like Jupyter QTConsole]
"""

import matplotlib.pyplot as plt

yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(yearly_life_expectancy.plot())
plt.show()





