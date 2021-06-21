# Section14-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrence

import copy
print('EX1-1 -')
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print(dir())
print(__name__)  # __main__

# id vs __eq__ (==) 증명
x = {'name': 'kim', 'age': 33, 'city': 'Seoul'}
y = x  # 얕은 복사

print('EX2-1 -', id(x), id(y))  # id 같음
print(x == y)  # True
print(x is y)  # True
# {'name': 'kim', 'age': 33, 'city': 'Seoul'} {'name': 'kim', 'age': 33, 'city': 'Seoul'}
print(x, y)

x['class'] = 10
# {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10} {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10} (값이 같이 변함)
print('EX2-5 -', x, y)

print()
print()

z = {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10}

# {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10} {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10}
print('EX2-6 -', x, z)
print(x is z)  # False
print(x is not z)  # True
print(x == z)  # True (값이 같다)

# 객체 생성 후 완전 불변 -> 즉, is는 객체 주소(정체성-id)비교, ==(__eq__) 는 값 비교

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2))  # id 다름
print(tuple1 is tuple2)  # False
print(tuple1 == tuple2)  # True
print(tuple1.__eq__(tuple2))  # True

print()
print()

# Copy, Deepcopy(깊은 복사, 얕은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print(tl1 == tl2)  # True
print(tl1 is tl2)  # True
print(tl1 == tl3)  # True
print(tl1 is tl3)  # False

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)  # [10, [100], (5, 10, 15), 1000]
print('EX4-6 -', tl2)  # [10, [100], (5, 10, 15), 1000]
print('EX4-7 -', tl3)  # [10, [100], (5, 10, 15)]

print()

# print(id(tl1[2]))
tl1[1] += [110, 120]
tl1[2] += (110, 120)

print('EX4-8 -', tl1)  # [10, [100, 110, 120], (5, 10, 15, 110, 120), 1000]
# [10, [100, 110, 120], (5, 10, 15, 110, 120), 1000] (튜플 재 할당(객체 새로 생성))
print('EX4-9 -', tl2)
print('EX4-10 -', tl3)  # [10, [100, 110, 120], (5, 10, 15)]
# print(id(tl1[2]))

print()
print()

# Deep Copy

# 장바구니


class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)  # 얕은 복사
basket3 = copy.deepcopy(basket1)  # 깊은 복사

# 값이 다 다름 (객체는 다들 새로 생성되었을테니까)
print('EX5-1 -', id(basket1), id(basket2), id(basket3))
print('EX5-2 -', id(basket1._products), id(basket2._products),
      id(basket3._products))  # 1, 2가 같음 3은 다름

print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

# ['Apple', 'Bag', 'TV', 'Water', 'Orange']
print('EX5-3 -', basket1._products)
# ['Apple', 'Bag', 'TV', 'Water', 'Orange']
print('EX5-4 -', basket2._products)
print('EX5-5 -', basket3._products)  # ['Apple', 'Bag', 'TV', 'Snack', 'Water']

print()
print()

# 함수 매개변수 전달 사용법


def mul(x, y):
    x += y
    return x


x = 10
y = 5

print('EX6-1 -', mul(x, y), x, y)  # 15 10 5
print()

a = [10, 100]
b = [5, 10]

# [10, 100, 5, 10] [10, 100, 5, 10] [5, 10] (가변형 a -> 원본 데이터 변경)
print('EX6-2 -', mul(a, b), a, b)

c = (10, 100)
d = (5, 10)

# (10, 100, 5, 10) (10, 100) (5, 10) (불변형 c -> 원본 데이터 변경 안됨)
print('EX6-2 -', mul(c, d), c, d)


# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본 생성 X -> 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

# True 140686018949824 140686018949824
print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
# True 140686018949824 140686018949824
print('EX7-2 -', tt3 is tt1, id(tt3), id(tt1))

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

# True True 140686017765264 140686017765264
print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
# True True 140685994807600 140685994807600
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))
