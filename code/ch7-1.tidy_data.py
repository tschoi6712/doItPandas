"""
깔끔한 데이터
: melt 메서드 - 지정한 열의 데이터를 모두 행으로 정리
: pivot_table 메서드 - (인덱스= 유지할 열, 칼럼=피벗할 열, 밸류=새로운 열의 데이터)
"""


### 07-1 열과 피벗

from numpy import NaN, NAN, nan
import numpy as np
import pandas as pd

path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'

# 1개의 열만 고정하고 나머지 열을 행으로 바꾸기
pew = pd.read_csv(path + 'data/pew.csv')                    # 퓨 리서치센터의 '미국의 소득과 종교' 데이터집합

print(pew.head())
print(pew.shape)

print(pew.iloc[:, 0:6])

pew_long = pd.melt(pew, id_vars='religion')                 # id_vars=고정한 열로  피벗)
print(pew_long.head())

pew_long = pd.melt(pew, id_vars='religion',
                   var_name='income', value_name='count')   # var_name='', value_name=''  열 이름 변경)
print(pew_long.head())


# 2개 이상의 열을 고정하고 나머지 열을 행으로 바꾸기
billboard = pd.read_csv(path + 'data/billboard.csv')        # 빌보드 차트 데이터
print(billboard.iloc[0:5, 0:16])

billboard_long = pd.melt(billboard,
                         id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                         var_name='week', value_name='rating')
                                                            #
print(billboard_long.head())


### 07-2 열 이름 관리하기

path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'

# 에볼라 데이터 집합 살펴보기
ebola = pd.read_csv(path + 'data/country_timeseries.csv')
print(ebola.columns)

print(ebola.iloc[:5, [0, 1, 2, 3, 10, 11]])

ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])        # 두 개 열 고정하여 피벗
print(ebola_long.head())

#1. split 메서드로 열 이름 분리하기
variable_split = ebola_long.variable.str.split('_')
print(variable_split[:5])
print(type(variable_split))
print(type(variable_split[0]))                              # 시리즈에 저장된 값은 리스트

status_values = variable_split.str.get(0)                   # 0번째 인덱스에 담긴 문자열
country_values = variable_split.str.get(1)                  # 1번째 인덱스에 담긴 문자열
print(status_values[:5])
print(status_values[-5:])
print(country_values[:5])
print(country_values[-5:])

#2. 분리한 문자열을 데이터프레임에 열 이름으로 추가
ebola_long['status'] = status_values
ebola_long['country'] = country_values
print(ebola_long.head())


# concat 메서드를 응용하여 데이터프레임에 열 추가하기
variable_split = ebola_long.variable.str.split('_', expand=True)
variable_split.columns = ['status', 'country']
ebola_parsed = pd.concat([ebola_long, variable_split], axis=1)
print(ebola_parsed.head())



### 07-3 여러 열을 하나로 정리하기

path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'

# 기상 데이터 집합
weather = pd.read_csv(path + 'data/weather.csv')
print(weather.iloc[:5, :11])
print(weather.shape)

weather_melt = pd.melt(weather, id_vars=['id', 'year', 'month', 'element'], var_name='day', value_name='temp')
print(weather_melt.head())

weather_tidy = weather_melt.pivot_table(
                            index=['id', 'year', 'month', 'day'],
                            columns='element',
                            values='temp'
                            )                                   # 행과 열의 위치를 다시 바꾼다다

print(weather_tidy)

weather_tidy_flat = weather_tidy.reset_index()                  # 인덱스 재 지정
print(weather_tidy_flat.head())




### 07-4 중복 데이터 처리하기

path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'

# 빌보드 차트 데이터 집합
billboard = pd.read_csv(path + 'data/billboard.csv')
billboard_long = pd.melt(billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                                    var_name='week', value_name='rating')

print(billboard_long.shape)
print(billboard_long.head())

print(billboard_long[billboard_long.track == 'Loser'].head())

# 중복 데이터를 가지고 있는 열
billboard_songs = billboard_long[['year', 'artist', 'track', 'time']]
print(billboard_songs.shape)

# 중복 데이터 제거: .drop_duplicates()
billboard_songs = billboard_songs.drop_duplicates()
print(billboard_songs.shape)

# 데이터프레임에 id 추가
billboard_songs['id'] = range(len(billboard_songs))
print(billboard_songs.head(n=10))


billboard_ratings = billboard_long.merge(billboard_songs, on=['year', 'artist', 'track', 'time'])
print(billboard_ratings.shape)
print(billboard_ratings.head())



### 07-5 대용량 데이터 처리하기 : 여러 개로 나누어진 데이터 불러오기

import os
import urllib.request


path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'

# 파일로 저장: urllib.request.urlretrieve() | 메모리로 저장 : urlopen()
with open(path + 'data/raw_data_urls.txt', 'r') as data_urls:
    for line, url in enumerate(data_urls):
        if line == 5:
            break
        fn = url.split('/')[-1].strip()
        fp = os.path.join('', '../data', fn)
        print(url)
        print(fp)
        urllib.request.urlretrieve(url, fp)


import glob

# 특정한 패턴 이름을 가진 파일을 한번에 불러오기:  glob.glob()
nyc_taxi_data = glob.glob(path + 'data/fhv_*')
print(nyc_taxi_data)

# 불러온 파일을 데이터프레임으로 저장
taxi1 = pd.read_csv(nyc_taxi_data[0])
taxi2 = pd.read_csv(nyc_taxi_data[1])
taxi3 = pd.read_csv(nyc_taxi_data[2])
taxi4 = pd.read_csv(nyc_taxi_data[3])
taxi5 = pd.read_csv(nyc_taxi_data[4])

# 데이터 불러오기 확인
print(taxi1.head(n=2))
print(taxi2.head(n=2))
print(taxi3.head(n=2))
print(taxi4.head(n=2))
print(taxi5.head(n=2))

# 각 데이터의 구조 확인
print(taxi1.shape)
print(taxi2.shape)
print(taxi3.shape)
print(taxi4.shape)
print(taxi5.shape)

# 각 데이터프레임을 연결
taxi = pd.concat([taxi1, taxi2, taxi3, taxi4, taxi5])
print(taxi.shape)



## 반복문으로 데이터 준비하기
list_taxi_df = []

for csv_filename in nyc_taxi_data:
    # print(csv_filename)
    df = pd.read_csv(csv_filename)
    list_taxi_df.append(df)

print(len(list_taxi_df))
print(type(list_taxi_df[0]))
print(list_taxi_df[0].head())

taxi_loop_concat = pd.concat(list_taxi_df)
print(taxi_loop_concat.shape)

print(taxi.equals(taxi_loop_concat))


