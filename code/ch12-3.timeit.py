"""
성능 향상시키기 - cython, numba 라이브러리
"""


# 코드 성능 향상 시켜 실행시간 측정하기 - timeit
import timeit
import pandas as pd
import numpy as np

df = pd.DataFrame({'a': [10, 20, 30], 'b': [20, 30, 40]})       # 판다스 데이터프레임 ― 실행 시간 측정
def avg_2_apply(row):
    x = row[0]
    y = row[1]
    if(x == 20):
        return np.nan
    else:
        return (x + y)/2

#%%timeit
df.apply(avg_2_apply, axis=1)


@np.vectorize                                                   # 넘파이로 벡터화한 함수 사용하기 ― 실행 시간 측정
def v_avg_2mod(x, y):
    if(x == 20):
        return (np.NaN)
    else:
        return (x + y) / 2

#%%timeit
v_avg_2mod(df['a'], df['b'])


import numba

@numba.vectorize                                                # numba 라이브러리로 벡터화한 함수 사용하기 ― 실행 시간 측정
def v_avg_2_numba(x, y):
    if(x == 20):
        return (np.NaN)
    else:
        return (x + y) / 2

#%%timeit
v_avg_2_numba(df['a'].values, df['b'].values)

