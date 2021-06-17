# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect('database/database.db')  # 본인 DB 파일 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")  # 커서 위치가 변경 된다.

# data 5개가 있는 상황

# 1개 로우 선택
print('One -> \n', c.fetchone())  # id = 1 row

# 지정 로우 선택
print('Three -> \n', c.fetchmany(size=3))  # id = 2, 3, 4 row

# 전체 로우 선택
print('All -> \n', c.fetchall())  # id = 5 row
print('All -> \n', c.fetchall())  # 없음

print()

# 순회1
rows = c.fetchall()
for row in rows:
    print('retrieve1  >', row)

# 순회2
for row in c.fetchall():
    print('retrieve2 >', row)

# 순회3
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print('retrieve3 > ', row)

print()

# WHERE Retrieve1
param1 = (1,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrieve2
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2)  # %s %d %f
print('param2', c.fetchone())
print('param2', c.fetchall())

# WHERE Retrieve3
c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 1})  # 딕셔너리는 ':'
print('param3', c.fetchone())
print('param3', c.fetchall())

# WHERE Retrieve4
param4 = (1, 4)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)  # IN은 합집합
print('param4', c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 4))
print('param5', c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2",
          {"id1": 1, "id2": 4})  # OR도 합집합
print('param6', c.fetchall())

print()


# Dump 출력 (DB 백업) (데이터베이스 백업 시 중요)
with conn:
    with open('database/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete.')
    # f.close() 이루어짐
# conn.close() 이루어짐
