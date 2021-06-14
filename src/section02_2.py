# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding) # utf-8
print(sys.stdout.encoding) # utf-8

# 출력문
print('My name is dailyco')

# 변수 선언
name = 'dailyco'
이름 = "dailyco"

# 조건문
if name == 'dailyco':
  print('ok') # ok

# 반복문
for i in range(1, 10):
  for j in range(1, 10):
    print('%d x %d =' % (i, j), i*j)
"""
1 x 1 = 1
1 x 2 = 2
...
9 x 8 = 72
9 x 9 = 81
"""

# 함수 선언
def 인사():
  print("안녕하세요, 반갑습니다.")
인사() # 실행

def greeting():
  print('Hello!')
greeting()

# 클래스
class Cookie:
  pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))