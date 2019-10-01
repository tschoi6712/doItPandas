"""
Series([data, index, dtype, name, copy, …])	One-dimensional ndarray with axis labels (including time series)
DataFrame([data, index, columns, dtype, copy])	Two-dimensional size-mutable, potentially heterogeneous tabular data
                                                structure with labeled axes (rows and columns).
"""


### 03-1 나만의 데이터 만들기

import pandas as pd

#시리즈 만들기: .Series(리스트)
series_1 = pd.Series(['banana', 42])
print(series_1)

series_2 = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(series_2)


# 데이터프레임 만들기: .DataFrame(딕셔너리)
df_1 = pd.DataFrame({
    'Name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]})
print(df_1)

df_2 = pd.DataFrame(
        data={'Occupation': ['Chemist', 'Statistician'],
            'Born': ['1920-07-25', '1876-06-13'],
            'Died': ['1958-04-16', '1937-10-16'],
            'Age': [37, 61]},
        index=['Rosaline Franklin', 'William Gosset'],
        columns=['Occupation', 'Born', 'Age', 'Died'])
print(df_2)


from collections import OrderedDict                 # 순서가 보장된 딕셔너리를 반환

df_3 = pd.DataFrame(OrderedDict({
    'Name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, 61]}))
print(df_3)




