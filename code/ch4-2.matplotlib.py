"""
Matplotlib is a Python 2D plotting library
: https://matplotlib.org
"""


### 04-2 Matplotlib 라이브러리 자유자재로 사용하기

# 기초 그래프 그리기 ― 히스토그램, 산점도, 박스 그래프
import seaborn as sns
import matplotlib.pyplot as plt

"""
tips 데이터 집합 - 식당에서 팁을 지불한 손님의 정보
               - total_bill, tip, sex, smoker, day, time, size(인원수)
"""
tips = sns.load_dataset("tips")
print(tips.head())
print(type(tips))

histogram = plt.figure()
axes1 = histogram.add_subplot(1, 1, 1)

# 히스토그램(일변량그래프): 데이터프레임의 열 데이터 분포와 빈도
axes1.hist(tips['total_bill'], bins=10)                 # bins=x축 간격
axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel('Frequency')
axes1.set_ylabel('Total Bill')
plt.show()

# 산점도(이변량그래프)
scatterplot = plt.figure()
axes1 = scatterplot.add_subplot(1, 1, 1)
axes1.scatter(tips['total_bill'], tips['tip'])
axes1.set_title('Scatterplot of Total Bill vs Tip')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')
plt.show()

# 박스 그래프: 이산형 변수와 연속형 변수를 함께 사용
boxplot = plt.figure()
axes1 = boxplot.add_subplot(1, 1, 1)
axes1.boxplot(
            [tips[tips['sex'] == 'Female']['tip'],
             tips[tips['sex'] == 'Male']['tip']],
             labels=['Female', 'Male'])

axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Sex')
plt.show()


# 다변량 데이터로 다변량 그래프 그리기 ─ 산점도 그래프
def recode_sex(sex):
    """
    각 문자열을 정수로 치횐하는 함수
    """
    if sex == 'Female':
        return 0
    else:
        return 1

tips['sex_color'] = tips['sex'].apply(recode_sex)       # .apply(반환한 값) 데이터프레임에 추가

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(
    x=tips['total_bill'],
    y=tips['tip'],
    s=tips['size'] * 10,
    c=tips['sex_color'],
    alpha=0.5)
"""
s=점의 크기, c=점의 색상, alpha=점의 투명도, 
"""
axes1.set_title('Total Bill vs Tip Colored by Sex and Sized by Size')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')
plt.show()


