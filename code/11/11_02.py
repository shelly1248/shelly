
# 클래스 정의 부분
class Car:
    color = ''
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

    # 메인 코드 부분
myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(30)
print(f'자동차1의 색상은 {myCar1.color}이며, 현재속도는 {myCar1.speed} km 입니다.')

myCar2.upSpeed(60)
print(f'자동차2의 색상은 {myCar2.color}이며, 현재속도는 {myCar2.speed} km 입니다.')

myCar3.upSpeed(0)
print(f'자동차3의 색상은 {myCar3.color}이며, 현재속도는 {myCar3.speed} km 입니다.')
