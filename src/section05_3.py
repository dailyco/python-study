# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
if (q1.get("가을") != None):
    print("1.", q1["가을"])

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
if ("사과" in q1.values()):
    print("2. 사과가 포함되었습니다")
else:
    print("2. 사과가 포함되지않았습니다")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 60
if (score > 80):
    print("3. A학점")
elif (score > 60):
    print("3. B학점")
elif (score > 40):
    print("3. C학점")
elif (score > 20):
    print("3. D학점")
elif (score >= 0):
    print("3. E학점")
else:
    print("3. 올바른 점수를 입력하세요!")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
num1, num2, num3 = 12, 6, 18
if (num1 > num2):
    if (num1 > num3):
        print("4.", num1)
    else:
        print("4.", num3)
elif (num2 > num3):
    print("4.", num2)
else:
    print("4.", num3)

# 5. 다음 주민등록 번호 에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자 || 주민등록번호 : 891022-1473837)
r_number = '891022-1473837'
if (int(r_number[7]) == 1 or int(r_number[7]) == 3):
    print("5. 남자")
elif (int(r_number[7]) == 2 or int(r_number[7]) == 4):
    print("5. 여자")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
print("6.", end=' ')
for e in q3:
    if (e == "정"):
        continue
    print(e, end=' ')
print()

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
print([e for e in range(1, 101, 2)])

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
print("8.", end=' ')
for e in q4:
    if (len(e) >= 5):
        print(e, end=' ')
print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print("9.", end=' ')
for e in q5:
    if (e.islower()):
        print(e, end=' ')
print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print("10.", end=' ')
for e in q6:
    if (e.isupper()):
        print(e.lower(), end=' ')
    elif (e.islower()):
        print(e.upper(), end=' ')
print()
