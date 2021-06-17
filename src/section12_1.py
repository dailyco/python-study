# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import datetime
import sqlite3

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('now Datetime', nowDatetime)

# sqlite3 버전
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version', sqlite3.sqlite_version)

print()


# DB생성 & Autocommit & Rollback
# Commit : DB에 변경사항을 반영하는 명령어
# Autocommit : 변경사항을 바로바로 DB에 반영
# Rollback : 변경사항 되돌리기

# 본인 DB 파일 경로
conn = sqlite3.connect('database/database.db', isolation_level=None)

# DB생성(메모리)
# conn = sqlite3.connect(":memory:")

# Cursor연결
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Datatype : TEXT NUMERIC INTEGER REAL BLOB)
c.execute(
    "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")  # AUTOINCREMENT

# 데이터 삽입
c.execute("INSERT INTO users VALUES (1 ,'Kim','Kim@naver.com', '010-0000-0000', 'Kim.com', ?)", (nowDatetime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)",
          (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)
c.executemany(
    "INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

print()


# 테이블 데이터 삭제
print("users db deleted :", conn.execute("delete from users").rowcount, "rows")

# 커밋 : isolation_level=None 일 경우 Auto Commit(자동 반영)
# conn.commit() # 자동 반영이 아닐 경우 반영 시켜주기위한 명령어

# 롤백
# conn.rollback() # Auto Commit 시에는 사용 불가

# 접속 해제
conn.close()
