"""
판다스 자료형
"""


### 08-1 자료형 다루기
import pandas as pd
import seaborn as sns

# seaborn의 데이터 집합
tips = sns.load_dataset("tips")

# 여러 가지 자료형을 문자열로 변환하기 - astype(str)
tips['sex_str'] = tips['sex'].astype(str)
print(tips.dtypes)

tips['total_bill'] = tips['total_bill'].astype(str)
print(tips.dtypes)

tips['total_bill'] = tips['total_bill'].astype(float)
print(tips.dtypes)

# 잘못 입력한 문자열 처리하기 ─ to_numeric 메서드
tips_sub_miss = tips.head(10)
tips_sub_miss.loc[[1, 3, 5, 7], 'total_bill'] = 'missing'

print(tips_sub_miss)
print(tips_sub_miss.dtypes)

#tips_sub_miss['total_bill'].astype(float)
#pd.to_numeric(tips_sub_miss['total_bill'])
"""
errors=
 - raise 숫자로 변환할 수 없는 값이 있으면 오류
 - coerce 숫자로 변환할 수 없는 값을 누락값으로 지정
 - ingnore 무시(변경되지 않음)
"""
tips_sub_miss['total_bill'] = pd.to_numeric(tips_sub_miss['total_bill'], errors='ignore')
print(tips_sub_miss.dtypes)

tips_sub_miss['total_bill'] = pd.to_numeric( tips_sub_miss['total_bill'], errors='coerce')
print(tips_sub_miss.dtypes)

tips_sub_miss['total_bill'] = pd.to_numeric( tips_sub_miss['total_bill'], errors='coerce', downcast='float')
print(tips_sub_miss.dtypes)



### 08-2 카테고리 자료형 : 동일한 문자열이 반복되어 데이터를 구성

# 문자열을 카테고리로 변환하기
tips['sex'] = tips['sex'].astype('str')
print(tips.info())

tips['sex'] = tips['sex'].astype('category')
print(tips.info())



