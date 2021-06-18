# Section13-2
# 업그레이드 타이핑 게임 제작
# 사운드 적용 및 DB 연동

import random
import winsound  # 사운드 출력 필요 모듈
import sqlite3
import time
import datetime

# DB생성 & Autocommit
# 본인 DB 파일 경로
conn = sqlite3.connect('database/records.db', isolation_level=None)

# Cursor연결
cursor = conn.cursor()

# 테이블 생성(Datatype : TEXT NUMERIC INTEGER REAL BLOB)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT,  cor_cnt INTEGER, record text, regdate text)"
)

words = []                                   # 영어 단어 리스트(1000개 로드)

n = 1                                        # 게임 시도 횟수
cor_cnt = 0                                  # 정답 개수

with open('src/resource/word.txt', 'r') as f:  # 문제 txt 파일 로드
    for c in f:
        words.append(c.strip())

# print(words)                                 # 단어 리스트 확인

input("Ready? Press Enter Key!")             # Enter Game Start!
start = time.time()                          # Start Time

while n <= 5:                                # 5회 반복
    random.shuffle(words)                    # List shuffle! (단어를 임의로 섞어줌)
    q = random.choice(words)                 # List -> words random extract!

    print()

    print("*Question # {}".format(n))
    print(q)                                 # 문제 출력

    x = input()                              # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip():     # 입력 확인(공백제거)
        winsound.PlaySound(                  # 정답 소리 재생
            './sound/good.wav',
            winsound.SND_FILENAME
        )
        print("Pass!")
        cor_cnt += 1                         # 정답 개수 카운트
    else:
        winsound.PlaySound(                  # 오답 소리 재생
            './sound/bad.wav',
            winsound.SND_FILENAME
        )
        print("Wrong!")

    n += 1                                  # 다음 문제 전환

end = time.time()                            # End Time
et = end - start                             # 총 게임 시간

et = format(et, ".3f")                       # 소수 셋째 자리 출력(시간)

if cor_cnt >= 3:                             # 3개 이상 합격
    print("결과 : 합격")
else:
    print("불합격")

# 기록 DB 삽입
cursor.execute(
    "INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)",
    (
        cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
)

# 수행 시간 출력
print("게임 시간 :", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작지점
if __name__ == '__main__':
    pass
