# Section09
# 파일 읽기, 쓰기

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 참조 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# 파일 읽기

# 예제1
from random import randint
f = open('./resource/review.txt', 'r')
contents = f.read()
print(contents)
# print(dir(f))
# 반드시 close 리소스 반환
f.close()

print()

# 예제2 (with 문)
# close 하지 않았도 with이 끝나면 자동으로 close
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(iter(c))  # <str_iterator object at 0x7ff701afe370>
    print(list(c))
    print(c)

print()

# read : 전체 내용 읽기, read(10) : 10글자 읽기

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        # print(c) # 한줄 띄어쓰기 됨
        print(c.strip())  # 양쪽 공백 없앰

print()

# 예제4
with open('./resource/review.txt', 'r') as f:
    contents = f.read()
    print('>', contents)
    contents = f.read()
    print('>', contents)  # 내용 없음 (커서가 맨 마직막으로 간 것)
    f.seek(0, 0)  # 커서를 다시 처음으로
    contents = f.read()
    print('>', contents)

print()

# 예제5
# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()
    print()

print()

# 예제6
# readlines : 전체 읽은 후 라인 단위 리스트 저장
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    print()
    for c in contents:
        print(c, end='')
    print()

print()

# 예제7
with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)  # [95, 78, 92, 89, 100, 66]
    print('Average : {:6.3f}'.format(
        sum(score) / len(score)))  # Average : 86.667

print()
print()

# 파일 쓰기

# 예제1
with open('./resource/test.txt', 'w') as f:
    f.write('niceman!')

# 예제2
with open('./resource/test.txt', 'a') as f:
    f.write('goodman!')

# 예제3

with open('./resource/test2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(50, 100)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/test3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5
with open('./resource/test4.txt', 'w') as f:
    print('Test Contents!', file=f)
    print('Test Contents!!', file=f)
