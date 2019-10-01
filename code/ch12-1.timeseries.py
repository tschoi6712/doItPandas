"""
시계열 데이터
"""


### 12-1 datetime 오브젝트


# datetime 오브젝트 사용하기
from datetime import datetime

now1 = datetime.now()                   # 현재 시간
print(now1)
now2 = datetime.today()
print(now2)

t1 = datetime.now()
t2 = datetime(1970, 1, 1)
t3 = datetime(1970, 12, 12, 13, 24, 34)
print(t1)
print(t2)
print(t3)

diff1 = t1 - t2                         # 시간계산
print(diff1)
print(type(diff1))

diff2 = t2 - t1
print(diff2)
print(type(diff2))


# 문자열을 datetime 오브젝트로 변환하기 - to_datetime 메서드
import pandas as pd
import os

path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'
ebola = pd.read_csv(path + 'data/country_timeseries.csv')
print(ebola.info())

ebola['date_dt'] = pd.to_datetime(ebola['Date'])
print(ebola.info())

test_df1 = pd.DataFrame({'order_day':['01/01/15', '02/01/15', '03/01/15']})

test_df1['date_dt1'] = pd.to_datetime(test_df1['order_day'], format='%d/%m/%y')
test_df1['date_dt2'] = pd.to_datetime(test_df1['order_day'], format='%m/%d/%y')
test_df1['date_dt3'] = pd.to_datetime(test_df1['order_day'], format='%y/%m/%d')
print(test_df1)

test_df2 = pd.DataFrame({'order_day':['01-01-15', '02-01-15', '03-01-15']})
test_df2['date_dt'] = pd.to_datetime(test_df2['order_day'], format='%d-%m-%y')
print(test_df2)


# 시계열 데이터를 구분해서 추출
now = datetime.now()
print(now)

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)

nowTime = now.strftime('%H:%M:%S')
print(nowTime)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)


# datetime 오브젝트로 변환하려는 열을 지정하여 데이터 집합 불러오기 - read_csv메서드
path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'
ebola1 = pd.read_csv(path + 'data/country_timeseries.csv', parse_dates=['Date'])
print(ebola1.info())


# datetime 오브젝트에서 날짜 정보 추출하기
date_series = pd.Series(['2018-05-16', '2018-05-17', '2018-05-18'])
d1 = pd.to_datetime(date_series)
print(d1)

print(d1[0].year)
print(d1[0].month)
print(d1[0].day)


# dt 접근자로 시계열 데이터 정리하기
path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'
ebola = pd.read_csv(path + 'data/country_timeseries.csv')

ebola['date_dt'] = pd.to_datetime(ebola['Date'])
print(ebola[['Date', 'date_dt']].head())

print(ebola['date_dt'][3].year)
print(ebola['date_dt'][3].month)
print(ebola['date_dt'][3].day)


ebola['year'] = ebola['date_dt'].dt.year
print(ebola[['Date', 'date_dt', 'year']].head())

ebola['month'], ebola['day'] = (ebola['date_dt'].dt.month, ebola['date_dt'].dt.day)
print(ebola[['Date', 'date_dt', 'year', 'month', 'day']].head())

print(ebola.info())



### 12-2 사례별 시계열 데이터 계산하기

# 에볼라 최초 발병일 계산하기
print(ebola.iloc[-5:, :5])

print(ebola['date_dt'].min())
print(type(ebola['date_dt'].min()))

ebola['outbreak_d'] = ebola['date_dt'] - ebola['date_dt'].min()
print(ebola[['Date', 'Day', 'outbreak_d']].head())


# 파산한 은행의 개수 계산하기
banks = pd.read_csv(path + 'data/banklist.csv')
print(banks.head())
print(banks.info())

banks = pd.read_csv(path + 'data/banklist.csv', parse_dates=[5, 6])
print(banks.info())

banks['closing_quarter'], banks['closing_year'] = (banks['Closing Date'].dt.quarter, banks['Closing Date'].dt.year)
print(banks.head())

closing_year = banks.groupby(['closing_year']).size()
print(closing_year)

closing_year_q = banks.groupby(['closing_year', 'closing_quarter']).size()
print(closing_year_q)


import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax = closing_year.plot()
plt.show()

fig, ax = plt.subplots()
ax = closing_year_q.plot()
plt.show()









