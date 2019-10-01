"""
그룹연산
: 데이터 집계, 변환, 필터링, 그룹오브젝트
"""


### 11-1 데이터 집계


# groupby 메서드로 평균값 구하기
import pandas as pd

path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'
df = pd.read_csv(path + 'data/gapminder.tsv', sep='\t')

avg_life_exp_by_year = df.groupby('year').lifeExp.mean()            # lifeExp 열의 연도별 평균
print(avg_life_exp_by_year)

avg_life_exp_by_year = df.groupby('year')['lifeExp'].mean()
print(avg_life_exp_by_year)


# 분할-반영-결합 과정 살펴보기
years = df.year.unique()                                            # 연도별 '분할' 작업
print(years)

y1952 = df.loc[df.year == 1952, :]                                  # 각 연도별로 데이터를 추출하는 '반영' 작업
print(y1952.head())

y1952_mean = y1952.lifeExp.mean()                                   # lifeExp 열의 평균값 계산
print(y1952_mean)

y1957 = df.loc[df.year == 1957, :]
y1957_mean = y1957.lifeExp.mean( )
print(y1957_mean)

y1962 = df.loc[df.year == 1962, :]
y1962_mean = y1962.lifeExp.mean( )
print(y1962_mean)

y2007 = df.loc[df.year == 2007, :]
y2007_mean = y2007.lifeExp.mean( )
print(y2007_mean)

df2 = pd.DataFrame({"year":[1952, 1957, 1962, 2007],
                    "":[y1952_mean, y1957_mean,y1962_mean,y2007_mean]})
print(df2)                                                          # 연도별로 계산한 lifeExp의 평균값을 합치는 '결합'


# 평균값을 구하는 사용자 함수와 groupby 메서드
def mean(values):
    """
    입력받은 열의 평균값을 구하는 함수
    """
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    return sum / n

agg_mean = df.groupby('year').lifeExp.agg(mean)
print(agg_mean)


# 두 개의 인잣값을 받아 처리하는 사용자 함수와 groupby 메서드
def mean_diff(values, diff_value):
    """
    두 개의 인잣값을 받아 처리하는 함수
    """
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    mean = sum / n
    return mean - diff_value

global_mean = df.lifeExp.mean()
print(global_mean)

agg_mean_diff = df.groupby('year').lifeExp.agg(mean_diff, diff_value=global_mean)
print(agg_mean_diff)


# 집계 메서드를 리스트, 딕셔너리에 담아 전달하기
import numpy as np

gdf = df.groupby('year').lifeExp.agg([np.count_nonzero, np.mean, np.std])
print(gdf)

gdf_dict = df.groupby('year').agg({'lifeExp': 'mean', 'pop': 'median', 'gdpPercap': 'median'})
print(gdf_dict)



# 11-2 데이터 변환

# 표준점수 계산하기
def zscore(x):
    """
    데이터의 평균값 = 0, 표준편차 = 1
    """
    return (x - x.mean()) / x.std()

transform_z = df.groupby('year').lifeExp.transform(zscore)
print(transform_z.head())
print(df.shape)
print(transform_z.shape)



# 누락값을 평균값으로 처리하기
import seaborn as sns
import numpy as np

np.random.seed(42)
tips_10 = sns.load_dataset('tips').sample(10)
tips_10.loc[np.random.permutation(tips_10.index)[:4], 'total_bill'] = np.NaN
print(tips_10)


count_sex = tips_10.groupby('sex').count()
print(count_sex)


def fill_na_mean(x):
    """
    성별을 구분하여 평균값을 계산
    """
    avg = x.mean()
    return x.fillna(avg)

total_bill_group_mean = tips_10.groupby('sex').total_bill.transform(fill_na_mean)
tips_10['fill_total_bill'] = total_bill_group_mean
print(tips_10)



### 11-3 데이터 필터링

# 데이터 필터링 사용하기 ─ filter 메서드
tips = sns.load_dataset('tips')
print(tips.shape)
print(tips['size'].value_counts())                              # 데이터 수 확인

tips_filtered = tips.groupby('size').filter(lambda x: x['size'].count() >= 30)
print(tips_filtered.shape)
print(tips_filtered['size'].value_counts())



### 그룹 오브젝트

# 그룹 오브젝트 저장하여 살펴보기
tips_10 = sns.load_dataset('tips').sample(10, random_state=42)
print(tips_10)

grouped = tips_10.groupby('sex')
print(grouped)

print(grouped.groups)


# 그룹 오브젝트의 평균 구하기
avgs = grouped.mean()
print(avgs)

print(tips_10.columns)


# 그룹 오브젝트에서 데이터 추출하고 반복하기
female = grouped.get_group('Female')
print(female)

for sex_group in grouped:
    print(sex_group)

for sex_group in grouped:
    print('the type is: {}\n'.format(type(sex_group)))
    print('the length is: {}\n'.format(len(sex_group)))

    first_element = sex_group[0]
    print('the first element is: {}\n'.format(first_element))
    print('it has a type of: {}\n'.format(type(sex_group[0])))

    second_element = sex_group[1]
    print('the second element is:\n{}\n'.format(second_element))
    print('it has a type of: {}\n'.format(type(second_element)))

    print('what we have:')
    print(sex_group)

    break


# 여러 열을 사용해 그룹 오브젝트 만들고 계산하기
bill_sex_time = tips_10.groupby(['sex', 'time'])
group_avg = bill_sex_time.mean()

print(group_avg)
print(type(group_avg))
print(group_avg.columns)
print(group_avg.index)

group_method = tips_10.groupby(['sex', 'time']).mean().reset_index()
print(group_method)

group_param = tips_10.groupby(['sex', 'time'], as_index=False).mean( )
print(group_param)



