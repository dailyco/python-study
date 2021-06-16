# Section08
# 파이썬 모듈과 패키지

# 패키지 예제1
# 상대 경로 패키지
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)
import builtins  # 파이썬 기본 제공 함수
import pkg.prints as p
from pkg.calculations import div as d
import pkg.calculations as c
from pkg.fibonacci import Fibonacci as fb
from pkg.fibonacci import *
from pkg.fibonacci import Fibonacci

Fibonacci.fib(100)  # 0 1 1 2 3 5 8 13 21 34 55 89
print(Fibonacci.fib2(200))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
print(Fibonacci().title)  # fibonacci

print()

# 사용2(클래스) 권장 X

Fibonacci.fib(300)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
print(Fibonacci.fib2(400))
print(Fibonacci().title)  # fibonacci

print()

# 사용3(클래스) 클래스 별명(Alias) 부여

fb.fib(500)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
print(fb.fib2(600))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
print(fb().title)  # fibonacci

print()

# 사용4(함수) : 파일 Alias

print(c.add(10, 10))  # 20
print(c.mul(10, 4))  # 40


# 사용5(함수) 함수 Alias

print(int(d(100, 10)))  # 10

print()

# 사용6

p.prt1()  # I'm NiceBoy!
p.prt2()  # I'm Goodboy!
print(dir(p))
print(dir(builtins))
