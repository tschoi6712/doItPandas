"""
Seaborn is a Python data visualization library based on matplotlib
: https://seaborn.pydata.org
"""


### 04-3 seaborn 라이브러리 자유자재로 사용하기

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# 단변량 그래프 그리기 ― 히스토그램
"""
sns.distplot(데이터집합, kde=밀집도, hist=히스토그램, rug=양탄자그래프)
"""
ax = plt.subplots()
ax = sns.distplot(tips['total_bill'])
ax.set_title('Total Bill Histogram with Density Plot')
plt.show()

ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], kde=False)
ax.set_title('Total Bill Histogram')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Frequency')
plt.show()

ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], hist=False)
ax.set_title('Total Bill Density')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Unit Probability')
plt.show()

hist_den_rug, ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], rug=True)
ax.set_title('Total Bill Histogram with Density and Rug Plot')
ax.set_xlabel('Total Bill')
plt.show()

"""
sns.countplot(열 데이터, data=데이터프레임) 각 카테고리 값별로 데이터가 얼마나 있는지 표시
"""
ax = plt.subplots()
ax = sns.countplot('day', data=tips)
ax.set_title('Count of days')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Frequency')
plt.show()


# 다양한 종류의 이변량 그래프 그리기
"""
1)산점도 그래프 그리기
sns.regplot(x='열', y='열', data=데이터프레임, fit_reg=회귀선) 
"""
ax = plt.subplots()
ax = sns.regplot(x='total_bill', y='tip', data=tips)
ax.set_title('Scatterplot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
plt.show()

ax = plt.subplots()
ax = sns.regplot(x='total_bill', y='tip', data=tips, fit_reg=False)
ax.set_title('Scatterplot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
plt.show()
"""
sns.jointplot(x='열', y='열', data=데이터프레임, kind=점 모양) 산점도와 히스토그램 그래프
"""
joint = sns.jointplot(x='total_bill', y='tip', data=tips)
joint.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
joint.fig.suptitle('Joint Plot of Total Bill and Tip', fontsize=10, y=1.03)
plt.show()

hexbin = sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
hexbin.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip', fontsize=10, y=1.03)
plt.show()


"""
2)이차원 밀집도 그리기
sns.kdeplot(data=데이터프레임[],data2=데이터프레임[], shade=음영효과)
"""
kde, ax = plt.subplots()
ax = sns.kdeplot(data=tips['total_bill'],
                 data2=tips['tip'],
                 shade=True)
ax.set_title('Kernel Density Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
plt.show()


"""
3)바 그래프 그리기
sns.barplot(x='열', y='열', data=데이터프레임)
"""
ax = plt.subplots()
ax = sns.barplot(x='time', y='total_bill', data=tips)
ax.set_title('Bar plot of average total bill for time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Average total bill')
plt.show()


"""
4)박스 그래프 그리기
sns.boxplot(x='열', y='열', data=데이터프레임)
"""
ax = plt.subplots()
ax = sns.boxplot(x='time', y='total_bill', data=tips)
ax.set_title('Boxplot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')
plt.show()

"""
박스 그래프 + 커널 밀도
sns.violinplot(x='열', y='열', data=데이터프레임)
"""
ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', data=tips)
ax.set_title('Violin plot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')
plt.show()

"""
5)관계 그래프 그리기
sns.boxplot(x='열', y='열', data=데이터프레임)
"""
fig = sns.pairplot(tips)

pair_grid = sns.PairGrid(tips)
pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.distplot, rug=True)
plt.show()



# 다변량 그래프 그리기
"""
색상 추가 - hue=샛상에 사용할 열
"""
violin, ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)
plt.show()

scatter = sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', fit_reg=False)
plt.show()

fig = sns.pairplot(tips, hue='sex')


"""
크기 조절 - scatter_kws=딕셔너리
모양 조절 - markers=리스트
"""
scatter = sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=False, hue='sex', scatter_kws={'s': tips['size']*10})
plt.show()

scatter = sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=False, hue='sex', markers=['o', 'x'], scatter_kws={'s': tips['size']*10})
plt.show()

"""
4개의 데이터 그룹에 대한 그래프 한 번에 그리기
sns.lmplot()
"""
anscombe = sns.load_dataset("anscombe")

anscombe_plot = sns.lmplot(x='x', y='y', data=anscombe, fit_reg=False)
plt.show()

anscombe_plot = sns.lmplot(x='x', y='y', data=anscombe, fit_reg=False, col='dataset', col_wrap=2)
plt.show()

"""
그룹별 그래프
sns.FacetGrid()
"""
facet = sns.FacetGrid(tips, col='time')
facet.map(sns.distplot, 'total_bill', rug=True)
plt.show()

facet = sns.FacetGrid(tips, col='day', hue='sex')
facet = facet.map(plt.scatter, 'total_bill', 'tip')
facet = facet.add_legend()
plt.show()

facet = sns.FacetGrid(tips, col='time', row='smoker', hue='sex')
facet.map(plt.scatter, 'total_bill', 'tip')
plt.show()


### 04-4 데이터프레임과 시리즈로 그래프 그리기
fig, ax = plt.subplots()
ax = tips['total_bill'].plot.hist()
plt.show()

fig, ax = plt.subplots()
ax = tips[['total_bill', 'tip']].plot.hist(alpha=0.5, bins=20, ax=ax)
plt.show()

fig, ax = plt.subplots()
ax = tips['tip'].plot.kde()
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.scatter(x='total_bill', y='tip', ax=ax)
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.hexbin(x='total_bill', y='tip', ax=ax)
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.hexbin(x='total_bill', y='tip', gridsize=10, ax=ax)
plt.show()

fig, ax = plt.subplots()
ax = tips.plot.box(ax=ax)
plt.show()



### 04-5 그래프에 스타일 적용하기
fig, ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)
plt.show()


sns.set_style('whitegrid')
fig, ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)
plt.show()


fig = plt.figure()
seaborn_styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
for idx, style in enumerate(seaborn_styles):
    plot_position = idx + 1
    with sns.axes_style(style):
        ax = fig.add_subplot(2, 3, plot_position)
        violin = sns.violinplot(x='time', y='total_bill', data=tips, ax=ax)
        violin.set_title(style)

fig.tight_layout()