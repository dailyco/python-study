# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습


print(type(True)) # <class 'bool'>
print(type(False)) # <class 'bool'>

# 기본 형식

# 예1
if True:
  # 출력됨.
  print("Yes")  # 들여쓰기 중요

if False:
  # 출력되지 않음.
  print("No")

# 예2
if False:
  # 여기는 실행되지 않음.
  print("You can't reach here")
else:
  # 여기가 실행된다.
  print("Oh, you are here")

print()


# 관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

# == 양 변이 같을 때 참.
print(a == b) # False

# != 양 변이 다를 때 참.
print(a != b) # True

# > 왼쪽이 클때 참.
print(a > b) # True

# >= 왼쪽이 크거나 같을 때 참.
print(a >= b) # True

# < 오른쪽이 클 때 참.
print(a < b) # False

# <= 오른쪽이 크거나 같을 때 참.
print(a <= b) # False

# 참 거짓 종류
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0, None

city = ""
if city:
  print("You are in:", city)
else:
  # 이쪽이 출력된다.
  print("Please enter your city")

city = "Seoul"
if city:
  # 이쪽이 출력된다.
  print("You are in:", city)
else:
  print("Please enter your city")

print()

# 논리연산자
# and, or, not

a = 100
b = 60
c = 15

print(a > b and b > c)  # True
print(a > b or b > c) # True
print(not a > b) # False
print(not b > c) # False
print(not True) # False
print(not False) # True

print()

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서로 적용

print(3 + 12 > 7 + 3) # True
print(5 + 10 * 3 > 7 + 3 * 20) # False
print(5 + 10 > 3 and 7 + 3 == 10) # True
print(5 + 10 > 0 and not 7 + 3 == 10) # False

# 예제 1
score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행.
if score1 >= 90 and score2 == 'A':
  # 여기가 출력
  print("합격하셨습니다.")
else:
  print("불합격입니다.")

# 예제 2
id1 = "gold"
id2 = "admin"
grade = 'super'

if id1 == "gold" or id2 == "admin":
  # 출력 O
  print("관리자 로그인 성공")

if id2 == "admin" and grade == "super":
  # 출력 O
  print("최고 관리자 로그인 성공")

# 예제 3
is_work = False

if not is_work:
  # 출력 O
  print("is work!")

print()

# 다중 조건문
num = 90

if num >= 70:
  # 여기가 출력
  print("등급 A :", num)
elif num >= 60:
  print("등급 B :", num)
else:
  print("등급 C")

# 중첩 조건문
age = 27
height = 175

if age >= 20:
  if height >= 170:
    # 여기가 출력
    print("A지망 지원 가능")
  elif height >= 160:
    print("B지망 지원 가능")
  else:
    print("지원 불가")
else:
  print("20세 이상 지원가능")

print()

# in, not in
q = [1, 2, 3]
w = {7, 8, 9, 9}
e = {"name": 'Kim', "city": "seoul", "grade": "B"}
r = (10, 12, 14)

print(1 in q) # True
print(6 in w) # False
print(12 not in r) # False
print("name" in e)  # True (key 검색)
print("seoul" in e.values())  # True (value 검색)