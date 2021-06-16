# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스 및 서브클래스 -> 모든 속성, 메소드 사용 가능

# 슈퍼클래스
class Car:
    """Parent Class"""

    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        # print('Car Class "Show" Method!')
        return 'Car Class "Show" Method!'

# 서브클래스


class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name

# 서브클래스


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show(self):
        print(super().show())  # super() 메소드로 부모에 접근 가능
        return 'Car Info : %s %s %s' % (self.car_name, self.color, self.type)

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)  # red (Super)
print(model1.type)  # sedan (Super)
print(model1.car_name)  # 520d (Sub)
print(model1.show())  # Car Class "Show" Method! (Super)
print(model1.show_model())  # Your Car Name : 520d (Sub)

# Method Overriding (부모의 메소드를 재구성)
model2 = BenzCar("220d", 'suv', 'black')
print(model2.show())  # Car Info : 220d black suv (Sub)

# Inheritance Info (상속 정보)
# [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]
print(BmwCar.mro())
# [<class '__main__.BenzCar'>, <class '__main__.Car'>, <class 'object'>]
print(BenzCar.mro())

print()


# 예제2
# 다중 상속
class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):  # X, Y 상속
    pass


class B(Y, Z):  # Y, Z 상속
    pass


class M(B, A, Z):  # B, A, Z 상속
    pass


# [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
print(M.mro())
# [<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>]
print(A.mro())
