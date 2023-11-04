# 모듈을 가져옵니다.
import math

# 클래스 선언
class Circle:
    def __init__ (self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
#원의둘레와넓이를 구합니다
circle = Circle(10)
print("원의둘레와 넓이를 구합니다")
print("원의 둘레", circle.get_circumference())
print("원의넓이", circle.get_area())

# __radius에 접근합니다.
print("__radius에 접근합니다")
print(circle.__radius)