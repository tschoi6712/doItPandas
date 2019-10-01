"""
문자열 처리하기
"""


### 09-1 문자열 다루기
import pandas as pd


# 인덱스로 문자열 추출하기
word = 'grail'
sent = 'a scratch'

print(sent[2:len(sent)])            # 전체 문자열을 추출
print(sent[2: ])
print(sent[ : ])                    # 왼쪽이나 오른쪽 범위를 지정하지 않고 문자열 추출
print(sent[::2])



### 09-2 문자열 메서드
"""
count, find, lower, upper, strip, split, center, zfill, isalpha, isdecimal, isalnum
"""
# join 메서드 - 문자열을 연결하여 새로운 문자열을 반환
d1 = '40°'
m1 = "46'"
s1 = '52.837"'
u1 = 'N'

d2 = '73°'
m2 = "58'"
s2 = '26.302"'
u2 = 'W'
coords = ' '.join([d1, m1, s1, u1, d2, m2, s2, u2])
print(coords)

# splitlines 메서드 - 여러 행을 가진 문자열을 분리한 다음 리스트로 반환
multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together. 
"""
print(multi_str)
multi_str_split = multi_str.splitlines()
print(multi_str_split)

guard = multi_str_split[::2]
print(guard)

# replace 메서드 - 문자열을 치환
guard = multi_str.replace("Guard: ", "").splitlines()[::2]
print(guard)



### 09-3 문자열 포매팅

# 문자열 포매팅하기
var = 'flesh wound'
s = "It's just a {}!"
print(s.format(var))            # {} 플레이스 홀더

s = """Black Knight: 'Tis but a {0}.
King Arthur: A {0}? Your arm's off!
"""
print(s.format('scratch'))

s = 'Hayden Planetarium Coordinates: {lat}, {lon}'
print(s.format(lat='40.7815° N', lon='73.9733° W'))


# 숫자 데이터 포매팅하기
print('Some digits of pi: {}'.format(3.14159265359))
print("In 2005, Lu Chao of China recited {:,} digits of pi".format(67890))
print("I remember {0:.4} or {0:.4%} of what Lu Chao recited".format(7/67890))
print("My ID number is {0:05d}".format(42))


# % 연산자로 포매팅하기
print('I only know %d digits of pi' % 7)
print('Some digits of %(cont)s: %(value).2f' % {'cont': 'e', 'value': 2.718})


# f-strings로 포매팅 사용하기
var = 'flesh wound'
s = f"It's just a {var}!"
print(s)

lat='40.7815°N'
lon='73.9733°W'
s = f'Hayden Planetarium Coordinates: {lat}, {lon}'
print(s)



### 09-4 정규식으로 문자열 처리에 날개 달기


# 정규식으로 전화번호 패턴 찾기
import re

# match 메서드 - 문자열을 처음부터 검색하여 찾아낸 패턴의 양 끝 인덱스를 반환
tele_num = '1234567890'
m = re.match(pattern='\d\d\d\d\d\d\d\d\d\d', string=tele_num)
print(type(m))
print(m)

print(bool(m))
if m:
    print('match')
else:
    print('no match')

print(m.start())                    # 첫번째 인덱스
print(m.end())                      # 마지막 인덱스
print(m.span())                     # (첫번째 인덱스,마지막 인덱스)
print(m.group())                    # 찾아낸 패턴


tele_num_spaces = '123 456 7890'
m = re.match(pattern='\d{10}', string=tele_num_spaces)
print(m)

if m:
    print('match')
else:
    print('no match')


tele_num_space_paren_dash = '(123) 456-7890'
p = '\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=tele_num_space_paren_dash)
print(m)

cnty_tele_num_space_paren_dash = '+1 (123) 456-7890'
p = '\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m)


# compile 메서드로 정규식 메서드 사용하기
p = re.compile('\d{10}')
s = '1234567890'
m = p.match(s)
print(m)


