# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Cap', 'Plate']
e = [10, 100, ['Pen', 'Cap', 'Plate']]

# 인덱싱
print(type(d), d) # <class 'list'> [10, 100, 'Pen', 'Cap', 'Plate']
print(d[1]) # 100
print(d[-4]) # 100
print(d[0] + d[1] + d[1]) # 210
print(d[-1]) # Plate
print(e[2][1]) # Cap
print(e[-1][1]) # Cap
print(e[-1][1][0]) # C
print(list(e[-1][1])) # ['C', 'a', 'p']

# 슬라이싱
print(d[0:3]) # [10, 100, 'Pen']
print(d[2:]) # ['Pen', 'Cap', 'Plate']
print(e[2][1:3]) # ['Cap', 'Plate']

print()

# 리스트 연산
print(c + d) # [1, 2, 3, 4, 10, 100, 'Pen', 'Cap', 'Plate']
print(c * 3) # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# print(c[0] + 'hi') # TypeError: unsupported operand type(s) for +: 'int' and 'str
print('hi' + str(c[0])) # hi1

# 리스트 수정, 삭제
c[0] = 4
print(c) # [4, 2, 3, 4]
c[1:2] = ['a', 'b', 'c']
print(c) # [4, 'a', 'b', 'c', 3, 4]
c[1] = ['a', 'b', 'c']
print(c) # [4, ['a', 'b', 'c'], 'b', 'c', 3, 4]
c[1:3] = [] # 삭제
print(c) # [4, 'c', 3, 4]
del c[3] # 삭제 (idx)
print(c) # [4, 'c', 3]

# 리스트 함수
a = [5, 2, 3, 1, 4]

print(a) # [5, 2, 3, 1, 4]
a.append(6) # 삽입 (맨끝)
print(a) # [5, 2, 3, 1, 4, 6]
a.sort() # 정렬
print(a) # [1, 2, 3, 4, 5, 6]
a.reverse() # 반대로
print(a) # [6, 5, 4, 3, 2, 1]
print(a.index(5)) # 1
a.insert(2, 7) # 삽입 (idx, 값)
print(a) # [6, 5, 7, 4, 3, 2, 1]
a.reverse() # [1, 2, 3, 4, 7, 5, 6]
a.remove(1) # 삭제 (값)
print(a) # [2, 3, 4, 7, 5, 6]
print(a.pop()) # 원소 꺼내기 (맨끝)
print(a.pop()) # 원소 꺼내기 (맨끝)
print(a) # [2, 3, 4, 7]
print(a.count(4)) # 1 (해당 값을 갖는 원소 수)
ex = [8, 9]
a.extend(ex) # 연장 (여러개의 값을 추가)
print(a) # [2, 3, 4, 7, 8, 9]

# 삭제 remove, pop, del

print()

# # 반복문 활용
# while a:
#     l = a.pop()
#     print(2 is l)

# 튜플 자료형(순서O, 중복O, 수정X,삭제X)

# 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, 'Pen', 'Cap', 'Plate')
e = (10, 100, ('Pen', 'Cap', 'Plate'))

# del c[0] # TypeError: 'tuple' object doesn't support item deletion

# 인덱싱
print(type(d), d) # <class 'tuple'> (10, 100, 'Pen', 'Cap', 'Plate')
print(d[1]) # 100
print(d[0] + d[1] + d[1]) # 210
print(d[-1]) # Plate
print(e[-1][1]) # Cap
# print(e[-1][1][3]) # IndexError: string index out of range
print(list(e[-1][1])) # ['C', 'a', 'p']

# 슬라이싱
print(d[0:3]) # (10, 100, 'Pen')
print(e[2:]) # (('Pen', 'Cap', 'Plate'),)
print(e[2][1:3]) # ('Cap', 'Plate')

# 튜플 연산
print(c + d) # (1, 2, 3, 4, 10, 100, 'Pen', 'Cap', 'Plate')
print(c * 3) # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
# print("c[0] + 'hi' - ",c[0] + 'hi') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('hi' + str(c[0])) # hi1

# 튜플 함수
a = (5, 2, 3, 1, 4)

print(a) # (5, 2, 3, 1, 4)
print(3 in a) # True
print(a.index(5)) # 0 (해당 값을 갖는 원소의 인덱스값을 반환)
print(a.count(4)) # 1 (해당 값을 갖는 원소 수)