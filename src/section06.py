# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#   code

# 함수 호출
# function_name()
# 함수 선언 위치 중요


# 예제1
def hello(world):
    print("Hello,", world)


param1 = "Niceman"
hello(param1)  # Hello, Niceman
hello(7777)  # Hello, 7777

# 예제2 (리턴값)


def hello_return(world):
    value = "Hello, " + str(world)
    return value


str = hello_return("Niceman")
print(str)  # Hello, Niceman

# 예제3(다중리턴)


def func_mul1(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1, y2, y3


val1, val2, val3 = func_mul1(3)
print(val1, val2, val3)  # 6 12 18

# 튜플 리턴


def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return (y1, y2, y3)


tup = func_mul2(4)
print(type(tup), tup, list(tup))  # <class 'tuple'> (8, 16, 24) [8, 16, 24]

# 리스트 리턴


def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return [y1, y2, y3]


lis = func_mul2(6)
print(type(lis), lis, set(lis))  # <class 'list'> [12, 24, 36] {24, 12, 36}


# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return {'ret1': y1, 'ret2': y2, 'ret3': y3}


dic = func_mul3(8)
# <class 'dict'> {'ret1': 16, 'ret2': 32, 'ret3': 48} 48 dict_items([('ret1', 16), ('ret2', 32), ('ret3', 48)]) dict_keys(['ret1', 'ret2', 'ret3']) dict_values([16, 32, 48])
print(type(dic), dic, dic.get('ret3'), dic.items(), dic.keys(), dic.values())
print()


# 예제4
# *args, **kwargs 이해

# *args
def args_func(*args):  # 매개변수명 자유롭게 변경 가능
    for i, v in enumerate(args):  # enumerate : 인덱싱 가능한 이터레이터 반환 -> i : idx, v : value
        print('{}'.format(i), v, end=' ')
    print()


args_func('Kim')  # 0 Kim
args_func('Kim', 'Park')  # 0 Kim 1 Park
args_func('Kim', 'Park', 'Lee')  # 0 Kim 1 Park 2 Lee

# kwargs


def kwargs_func(**kwargs):  # 매개변수명 자유롭게 변경 가능
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v], end=' ')
    print()


kwargs_func(name1='Kim')  # name1 Kim
kwargs_func(name1='Kim', name2='Park')  # name1 Kim name2 Park
# name1 Kim name2 Park name3 Lee
kwargs_func(name1='Kim', name2='Park', name3='Lee')

# 전체 혼합


def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)


# 10 20 ('park', 'kim', 'lee') {'age1': 33, 'age2': 34, 'age3': 44}
example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)

print()


# 예제5
# 중첩함수 (클로저)
def nested_func(num):
    def func_in_func(num):
        print("In func")
        print(num)
    func_in_func(num + 100)


nested_func(1)
"""
In func
101
"""
# 실행불가
# func_in_func(1)

print()


# 예제6
# Hint
def tot_length1(word: str, num: int) -> int:
    return len(word) * num


print(tot_length1("i love you", 10))  # 100


def tot_length2(word: str, num: int) -> None:
    print(len(word) * num)


tot_length2("niceman", 10)  # 70

print()


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화

# 예제7
# def mul_10(num):
#     return num * 10

# lambda x: x * 10

# 일반적 함수 -> 변수 할당
def mul_10(num):
    return num * 10


mul_func = mul_10

print(mul_func(5))  # 50
print(mul_func(6))  # 60

# 람다 함수 -> 할당


def lambda_mul_func(x): return x * 10


def func_final(x, y, func):
    print(x * y * func(10))


func_final(10, 10, lambda_mul_func)  # 10000
