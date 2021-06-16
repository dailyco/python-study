# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class ClassName:
#   function1
#   function2
#   ...

# 예제1
class UserInfo:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("Name: " + self.name)

    def __del__(self):
        print("Instance removed!")


user1 = UserInfo("dailyco")
user2 = UserInfo("Park")

print(id(user1))  # 140376259077552 (id: 실행할 때마다 매번 바뀌는 값)
print(id(user2))  # 140376259076928

user1.print_info()  # Name: dailyco
user2.print_info()  # Name: Park

# 클래스 네임스페이스 확인
print('user1 :', user1.__dict__)  # user1 : {'name': 'dailyco'}
print('user2 :', user2.__dict__)  # user2 : {'name': 'Park'}

print(user1.name)  # dailyco

print()


# self의 이해
# 예제2
class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")


f = SelfTest()
# print(dir(f))
print(id(f))  # 139666136877568
# f.function1() # TypeError: function1() takes 0 positional arguments but 1 was given (self 인자가 넘어간 상황)
f.function2()  # 139666136877568\n function2 called!
SelfTest.function1()  # function1 called!
# print(SelfTest.function2()) # TypeError: function2() missing 1 required positional argument: 'self' (클래스는 self 인자가 없기 때문에 인자가 부족한 상황)

print()


# 클래스 변수 , 인스턴스 변수
# 예제3
class Warehouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('dailyco')
user2 = Warehouse('Park')

print(user1.name)  # dailyco
print(user2.name)  # Park
print(user1.__dict__)  # {'name': 'dailyco'}
print(user2.__dict__)  # {'name': 'Park'}
# {..., 'stock_num': 2, '__init__': <function Warehouse.__init__ at 0x7f5f5235bee0>, ...} (클래스 네임스페이스 , 클래스 변수 (공유))
print(Warehouse.__dict__)

# Warehouse.stock_num = 50 # 직접 접근 가능
# 자신의 네임스페이스에 없으면 클래스 네임스페이스에서 검색! -> 그래도 없으면 에러
print(user1.stock_num)  # 2
print(user2.stock_num)  # 2
