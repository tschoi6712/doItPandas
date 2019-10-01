"""
시계열 데이터
"""


### 12-2 사례별 시계열 데이터 계산하기

path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'
# 테슬라 주식 데이터로 시간 계산하기
"""
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as pdr

tesla = pdr.get_data_quandl('TSLA')                         # tesla에는 데이터프레임이 저장
tesla.to_csv(path + 'data/tesla_stock_quandl.csv')          # tesla에 저장된 데이터프레임을 파일로 저장
print(tesla.head())
"""
import pandas as pd
import quandl

quandl.ApiConfig.api_key = "bZR-h4f5e4JLo3Zk6Ub2"           # quandl에서 api_key로 인증
tesla = quandl.get("WIKI/TSLA")                             # tesla에는 데이터프레임이 저장
tesla.to_csv(path + 'data/tesla_stock_quandl.csv')          # tesla에 저장된 데이터프레임을 파일로 저장
print(tesla.shape)
print(tesla.head())

tesla = pd.read_csv(path + 'data/tesla_stock_quandl.csv', parse_dates=[0])
print(tesla.info())

print(tesla.loc[(tesla.Date.dt.year == 2010) & (tesla.Date.dt.month == 6)])


# datetime 오브젝트를 인덱스로 설정하여 데이터 추출하기
tesla.index = tesla['Date']
print(tesla.index)

print(tesla['2015'].iloc[:5, :5])
print(tesla['2010-06'].iloc[:, :5])


# 시간 간격을 인덱스로 설정하여 데이터 추출하기
tesla['ref_date'] = tesla['Date'] - tesla['Date'].min()
print(tesla.head())

tesla.index = tesla['ref_date']
print(tesla.iloc[:5, :5])
print(tesla['5 days':].iloc[:5, :5])


# 시간 범위 생성하여 인덱스로 지정하기
ebola = pd.read_csv(path + 'data/country_timeseries.csv', parse_dates=[0])
print(ebola.iloc[:5, :5])
print(ebola.iloc[-5:, :5])

head_range = pd.date_range(start='2014-12-31', end='2015-01-05')
print(head_range)

ebola_5 = ebola.head()
ebola_5.index = ebola_5['Date']
ebola_5.reindex(head_range)
print(ebola_5.iloc[:5, :5])


# 시간 범위의 주기 설정하기
print(pd.date_range('2017-01-01', '2017-01-07', freq='B'))


# 에볼라의 확산 속도 비교하기
import matplotlib.pyplot as plt

ebola.index = ebola['Date']
fig, ax = plt.subplots()
ax = ebola.iloc[0:, 1:].plot(ax=ax)
ax.legend(fontsize=7, loc=2, borderaxespad=0.)
plt.show()

ebola_sub = ebola[['Day', 'Cases_Guinea', 'Cases_Liberia']]
print(ebola_sub.tail(10))

ebola = pd.read_csv(path + 'data/country_timeseries.csv',  parse_dates=['Date'])
print(ebola.head().iloc[:, :5])

ebola.index = ebola['Date']
new_idx = pd.date_range(ebola.index.min(), ebola.index.max())
print(new_idx)

new_idx = reversed(new_idx)
ebola = ebola.reindex(new_idx)
print(ebola.head().iloc[:, :5])
print(ebola.tail().iloc[:, :5])

last_valid = ebola.apply(pd.Series.last_valid_index)            # 각 나라의 에볼라 발병일 옮기기
print(last_valid)

first_valid = ebola.apply(pd.Series.first_valid_index)
print(first_valid)

earliest_date = ebola.index.min()
print(earliest_date)

shift_values = last_valid - earliest_date
print(shift_values)


ebola_dict = {}
for idx, col in enumerate(ebola):
    d = shift_values[idx].days
    shifted = ebola[col].shift(d)
    ebola_dict[col] = shifted

ebola_shift = pd.DataFrame(ebola_dict)
print(ebola_shift.tail())

ebola_shift.index = ebola_shift['Day']
ebola_shift = ebola_shift.drop(['Date', 'Day'], axis=1)
print(ebola_shift.tail())

fig, ax = plt.subplots()
ax = ebola_shift.iloc[:, :].plot(ax=ax)
ax.legend(fontsize=7, loc=2, borderaxespad=0.)
plt.show()





