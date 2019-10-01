"""
데이터 연결하기
: tidy data - table, row(측정한 값), column(변수)
: 왼쪽.merge(오른쪽, left_on=일치해야 하는 열, right_on=일치해야 하는 열)
"""


### 05-3 데이터 연결 마무리

import pandas as pd

# merge 메서드 사용하기
path = 'D:/1.Workspace/1.Python/part2.data_analysis/doItPandas/'

person = pd.read_csv(path + 'data/survey_person.csv')
site = pd.read_csv(path + 'data/survey_site.csv')
survey = pd.read_csv(path + 'data/survey_survey.csv')
visited = pd.read_csv(path + 'data/survey_visited.csv')

print(person)
print(site)
print(visited)
print(survey)

visited_subset = visited.loc[[0, 2, 6], ]
print(visited_subset)
s2vs_merge = site.merge(visited_subset, left_on='name', right_on='site')     # 데이터프레임 일부 연결
print(s2vs_merge)

s2v_merge = site.merge(visited, left_on='name', right_on='site')             # 데이터프레임 전체 연결
print(s2v_merge)

p2s = person.merge(survey, left_on='ident', right_on='person')
v2s = visited.merge(survey, left_on='ident', right_on='taken')
print(p2s)
print(v2s)


ps_vs = p2s.merge(v2s, left_on=['ident', 'taken', 'quant', 'reading'],
                        right_on=['person', 'ident', 'quant', 'reading'])
print(ps_vs)
print(ps_vs.loc[0, ])









