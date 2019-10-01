"""
apply 메서드 활용
: 사용자가 작성한 함수를 한 번에 데이터프레임의 각 행과 열에 적용
"""


### 10-1 제곱 함수와 n 제곱 함수 만들기
def square(x):
    return x ** 2

def exponential(x, n):
    return x ** n

print(square(4))
print(exponential(2, 4))



### 10-2 시리즈와 데이터프레임에 apply 메서드 사용하기
import pandas as pd

# 시리즈와 apply 메서드
df = pd.DataFrame({'a': [10, 20, 30], 'b': [20, 30, 40]})
print(df)

print(df['a'] ** 2)

sq = df['a'].apply(square)
print(sq)

ex = df['a'].apply(exponential, n=2)
print(ex)


# 데이터 프레임과 apply 메서드
df = pd.DataFrame({'a': [10, 20, 30], 'b': [20, 30, 40]})
def print_me(x):
    print(x)

print(df.apply(print_me, axis=0))
print(df['a'])
print(df['b'])

def avg_3(x, y, z):
    return (x + y + z) / 3

#print(df.apply(avg_3))                     # TypeError

def avg_3_apply(col):
    x = col[0]
    y = col[1]
    z = col[2]
    return (x + y + z) / 3

print(df.apply(avg_3_apply))

def avg_3_apply(col):
    """
    열 단위로 데이터를 처리하는 함수
    """
    sum = 0
    for item in col:
         sum += item
    return sum / df.shape[0]

print(df.apply(avg_3_apply))

def avg_2_apply(row):
    """
    행 단위로 데이터를 처리하는 함수
    """
    sum = 0
    for item in row:
        sum += item
    return sum / df.shape[1]

print(df.apply(avg_2_apply, axis = 1))



### 10-3 데이터프레임의 누락값을 처리한 다음 apply 메서드 사용하기

# 데이터프레임의 누락값 처리하기 ― 열 방향
import seaborn as sns

titanic = sns.load_dataset("titanic")           # 타이타닉 침놀 시 생존자에 대한 데이터
print(titanic.info())

import numpy as np

def count_missing(vec):
    """
    누락값의 갯수를 반환하는 함수
    """
    null_vec = pd.isnull(vec)
    null_count = np.sum(null_vec)
    return null_count

cmis_col = titanic.apply(count_missing)
print(cmis_col)


def prop_missing(vec):
    """
    누락값의 비율을 구하는 함수
    """
    num = count_missing(vec)
    dem = vec.size
    return num / dem

pmis_col = titanic.apply(prop_missing)
print(pmis_col)


def prop_complete(vec):
    """
    데이터의 비율을 구하는 함수
    """
    return 1 - prop_missing(vec)

pcom_col = titanic.apply(prop_complete)
print(pcom_col)



### 10-4 데이터프레임의 누락값을 처리하기 ― 행 방뱡
cmis_row = titanic.apply(count_missing, axis=1)
pmis_row = titanic.apply(prop_missing, axis=1)
pcom_row = titanic.apply(prop_complete, axis=1)

print(cmis_row.head())
print(pmis_row.head())
print(pcom_row.head())

titanic['num_missing'] = titanic.apply(count_missing, axis=1)   # 누락값 갯수를 수하여 데이터프레임에 추가
print(titanic.head())

print(titanic.loc[titanic.num_missing > 1, :].sample(10))       # 누락값이 2개 이상인 데이터를 추출








