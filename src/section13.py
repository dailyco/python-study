import random
import pygame
import sqlite3
import time
import datetime

conn = sqlite3.connect('database/records.db', isolation_level=None)
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT,  cor_cnt INTEGER, record text, regdate text)"
)

words = []

n = 1
cor_cnt = 0

with open('src/resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

input("Ready? Press Enter Key!")
start = time.time()

pygame.mixer.init()
good_sound = pygame.mixer.Sound('src/sound/good.wav')
bad_sound = pygame.mixer.Sound('src/sound/bad.wav')
good_sound.set_volume(0.5)
bad_sound.set_volume(0.5)

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("*Question # {}".format(n))
    print(q)

    x = input()

    print()

    if str(q).strip() == str(x).strip():
        good_sound.play()
        print("Pass!")
        cor_cnt += 1
    else:
        bad_sound.play()
        print("Wrong!")

    n += 1

end = time.time()
et = end - start

et = format(et, ".3f")

if cor_cnt >= 3:
    print("결과 : 합격")
else:
    print("불합격")

cursor.execute(
    "INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)",
    (
        cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
)

print("게임 시간 :", et, "초", "정답 개수 : {}".format(cor_cnt))

if __name__ == '__main__':
    pass
