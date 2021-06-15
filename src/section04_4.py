# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리 자료형(순서X, 중복X, 수정O, 삭제O)

# 선언
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]}

print(type(a), a) # <class 'dict'> {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
print(type(b), b) # <class 'dict'> {0: 'Hello python!'}
print(type(c), c) # <class 'dict'> {'arr': [1, 2, 3, 4]}

# 출력
print(a['name'])  # Kim (존재X -> 에러 발생)
# print(a['name1'])  # KeyError: 'name1'
print(a.get('name'))  # Kim (존재X -> None 처리)
print(a.get('name1'))  # None
print(b[0]) # Hello python!
print(b.get(0)) # Hello python!
print(c['arr']) # [1, 2, 3, 4]
print(c['arr'][3]) # 4
print(c.get('arr')) # [1, 2, 3, 4]

print()

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a) # {'name': 'Kim', 'phone': '01012345678', 'birth': '870124', 'address': 'Seoul'}
a['rank'] = [1, 2, 3]
print(a) # {'name': 'Kim', 'phone': '01012345678', 'birth': '870124', 'address': 'Seoul', 'rank': [1, 2, 3]}
a['rank2'] = (1, 2, 3, )
print(a) # {'name': 'Kim', 'phone': '01012345678', 'birth': '870124', 'address': 'Seoul', 'rank': [1, 2, 3], 'rank2': (1, 2, 3)}

print()

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
print(a.keys()) # dict_keys(['name', 'phone', 'birth', 'address', 'rank', 'rank2'])
print(b.keys()) # dict_keys([0])
print(c.keys()) # dict_keys(['arr'])

print(list(a.keys())) # ['name', 'phone', 'birth', 'address', 'rank']
print(list(b.keys())) # [0]
print(list(c.keys())) # ['arr']

print(a.values()) # dict_values(['Kim', '01012345678', '870124', 'Seoul', [1, 2, 3], (1, 2, 3)])
print(b.values()) # dict_values(['Hello python!'])
print(c.values()) # dict_values([[1, 2, 3, 4]])

print(list(a.values())) # ['Kim', '01012345678', '870124', 'Seoul', [1, 2, 3], (1, 2, 3)]
print(list(b.values())) # ['Hello python!']
print(list(c.values())) # [[1, 2, 3, 4]]

print(a.items()) # dict_items([('name', 'Kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'Seoul'), ('rank', [1, 2, 3]), ('rank2', (1, 2, 3))])
print(b.items()) # dict_items([(0, 'Hello python!')])
print(c.items()) # dict_items([('arr', [1, 2, 3, 4])])

print(list(a.items())) # [('name', 'Kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'Seoul'), ('rank', [1, 2, 3]), ('rank2', (1, 2, 3))]
print(list(b.items())) # [(0, 'Hello python!')]
print(list(c.items())) # [('arr', [1, 2, 3, 4])]

print('name' in a) # True
print('addr' in a) # False

print()

# 집합(Sets) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = set([1, 4, 5, 6, 6])

# 출력
print(type(a), a) # <class 'set'> set()
print(type(b), b) # <class 'set'> {1, 2, 3, 4}
print(type(c), c) # <class 'set'> {1, 4, 5, 6}
print(type(d), d) # <class 'set'> {1, 2, 'Plate', 'Pen', 'Cap'}
print(type(e), e) # <class 'set'> {1, 4, 5, 6} (중복 허용 X)

# 튜플 변환
t = tuple(b)
print(type(t), t) # <class 'tuple'> (1, 2, 3, 4)
print(t[0], t[1:3]) # 1 (2, 3)

# 리스트 변환
l = list(c)
print(type(l), l) # <class 'list'> [1, 4, 5, 6]
print(l[0], l[1:3]) # 1 [4, 5]

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2) # {4, 5, 6} (교집합)
print(s1.intersection(s2)) # {4, 5, 6} (교집합)

print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9} (합집합)
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9} (합집합)

print(s1 - s2) # {1, 2, 3} (차집합)
print(s1.difference(s2)) # {1, 2, 3} (차집합)

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print(s1) # {1, 2, 3, 4, 5}

s1.remove(2)
print(s1) # {1, 3, 4, 5}