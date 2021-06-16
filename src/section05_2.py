# Section05-2
# 파이썬 흐름제어(제어문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 사용(while, for)
v1 = 1

while v1 < 11:
    print(v1, end=' ')
    v1 += 1
print()
# 1 2 3 4 5 6 7 8 9 10

for v2 in range(10):
    print(v2, end=' ')
print()
# 0 1 2 3 4 5 6 7 8 9

for v3 in range(1, 11):
    print(v3, end=' ')
print()
# 1 2 3 4 5 6 7 8 9 10

for v4 in range(1, 11, 2):
    print(v4, end=' ')
print()
# 1 3 5 7 9

# 예제 1) 1 ~ 100합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 합 :', sum1)  # 1 ~ 100 합 : 5050
print('1 ~ 100 합 :', sum(range(1, 101)))  # 1 ~ 100 합 : 5050 (sum(리스트) 함수 사용)
# 1 ~ 100 안에 3의 배수의 합 : 1683
print('1 ~ 100 안에 3의 배수의 합 :', sum(range(3, 101, 3)))

print()

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

print("You are", end=' ')
for name in names:
    print(name, end=' ')
print()
# You are Kim Park Cho Lee Choi Yoo

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

print("Your number", end=' ')
for number in lotto_numbers:
    print(number, end=' ')
print()
# Your number 11 19 21 28 36 37

# 예제3
word = 'dreams'

print('word :', end=' ')
for s in word:
    print(s, end=' ')
print()
# word : d r e a m s

# 예제4
my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}

for key in my_info:  # 기본은 key를 가지고 옴
    print(key, ":", my_info[key])
"""
name : Kim
age : 33
city : Seoul
"""

for val in my_info.values():  # 값
    print(val)
"""
Kim
33
Seoul
"""

for k, v in my_info.items():  # 아이템
    print(k, ":", v)
"""
name : Kim
age : 33
city : Seoul
"""

# 예제5
name = 'KennRY'

for n in name:
    if n.isupper():
        print(n, end='')
    else:
        print(n.upper(), end='')
print()
# KENNRY

print()


# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : ", num)
"""
not found :  14
not found :  3
not found :  4
not found :  7
not found :  10
not found :  24
not found :  17
not found :  2
found : 33!
"""

# flag 사용
f = True
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

while f:
    for v in numbers:
        if v == 33:
            print("found : 33!")
            f = False
        print("not found : ", v)
"""
not found :  14
not found :  3
not found :  4
not found :  7
not found :  10
not found :  24
not found :  17
not found :  2
found : 33!
"""

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue

    print("type:", type(v))
    print("multiply by 2:", v * 3)
"""
type: <class 'str'>
multiply by 2: 111
type: <class 'int'>
multiply by 2: 6
type: <class 'int'>
multiply by 2: 15
type: <class 'bool'>
multiply by 2: 3
type: <class 'complex'>
multiply by 2: (12+0j)
"""

print()

# for-else (반복문이 break를 만나지 않고 정상적으로 수행했을 경우 else 블럭 수행)
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 39:
        print("found : 39!")
        break
    else:
        print("not found : ", num)
else:
    print("Not Found 39...")
"""
not found :  14
not found :  3
not found :  4
not found :  7
not found :  10
not found :  24
not found :  17
not found :  2
not found :  33
not found :  15
not found :  34
not found :  36
not found :  38
Not Found 39...
"""

# else 구문 정리(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
# 예제1
i = 1
while i <= 10:
    print(i, end=' ')
    if i == 6:
        break
    i += 1
else:
    print('else block run!')
print()
# 1 2 3 4 5 6

# 예제2
j = 1
while j <= 10:
    print(j, end=' ')
    if j == 11:
        break
    j += 1
else:
    print('else block run!')
# 1 2 3 4 5 6 7 8 9 10 else block run!

print()

# 중첩 for 문 구구단 출력
for i in range(1, 11):
    for j in range(1, 11):
        print('{:4d}'.format(i * j), end='')
    print()
"""
   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
   4   8  12  16  20  24  28  32  36  40
   5  10  15  20  25  30  35  40  45  50
   6  12  18  24  30  36  42  48  54  60
   7  14  21  28  35  42  49  56  63  70
   8  16  24  32  40  48  56  64  72  80
   9  18  27  36  45  54  63  72  81  90
  10  20  30  40  50  60  70  80  90 100
"""

print()

# 자료 구조 변환 예제
name = 'Niceman'
print(reversed(name))  # <reversed object at 0x7fdb0c57f550>
print(list(reversed(name)))  # ['n', 'a', 'm', 'e', 'c', 'i', 'N']
print(tuple(reversed(name)))  # ('n', 'a', 'm', 'e', 'c', 'i', 'N')
print(set(reversed(name)))  # {'c', 'n', 'm', 'e', 'i', 'N', 'a'} (순서 X)
print()

# 리스트 컴프리헨션
# 일반적인 방법
numbers = []
for n in range(1, 101):
    numbers.append(n)
print(numbers)

# 리스트 컴프리헨션
numbers2 = [x for x in range(1, 101)]
print(numbers2)

# 예제 1) "정"이 아닌 값들로만 리스트 생성
q3 = ["갑", "정", "병", "을"]
q5 = [x for x in q3 if x != '정']
print(q5)  # ['갑', '병', '을']

# 예제 2) 1부터 100까지 자연수중 홀수값들을 갖는 리스트 생성
q6 = [e for e in range(1, 101, 2)]
print(q6)
