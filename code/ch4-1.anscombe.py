"""
그래프 그리기
: 앤스콤 4분할그래프(Anscomb's quartet)
"""


### 04-1 데이터 시각화가 필요한 이유

# 앤스콤 데이터 집합 불러오기
import seaborn as sns

anscombe = sns.load_dataset("anscombe")
print(anscombe)
print(type(anscombe))

# 그래프 그리기
#%matplotlib inline
import matplotlib.pyplot as plt

dataset_1 = anscombe[anscombe['dataset'] == 'I']

plt.plot(dataset_1['x'], dataset_1['y'])
plt.show()
plt.plot(dataset_1['x'], dataset_1['y'], 'o')
plt.show()

"""
1) 그래프 격자가 위치할 기본 틀 - plt.figure()
2) 그래프를 그려 넣을 그래프 격자를 생성 - .add_subplot(행, 열, 순서)
3) 격자가 추가되는 순서 - 왼쪽에서 오른쪽
4) 그래프 그리기 - .plot()
5) 그래프 격자 제목 - .set_title()
6) 기본 틀(fig) 제목 - .suptitle()
7) 각 그래프의 레이아웃 조절 - .tight_layout()
"""

dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')
print(fig)
plt.show()

axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")
print(fig)
plt.show()

fig.suptitle("Anscombe Data")
print(fig)

fig.tight_layout()
print(fig)
plt.show()







