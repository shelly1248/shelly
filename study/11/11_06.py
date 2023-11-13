## 클래스 선언
class Car:
    color = "" # 인스턴스 변수
    speed = 0 # 인스턴스 변수
    count = 0 # 클래스 변수

    def printMessage():
        print("시험 출력입니다.")

    def __init__(self):
        self.speed = 0
        Car.count += 1

# 변수 선언
myCar1, myCar2 = None, None

# 메인 코드 부분
myCar1 = Car()
myCar1.speed = 30
print(f"자동차1의 현재 속도 는 {myCar1.speed}km, 생산된 자동차 숫자는 총 {myCar1.count}대 입니다")

myCar2 = Car()
myCar2.speed = 60
print(f"자동차2의 현재 속도 는 {myCar2.speed}km, 생산된 자동차 숫자는 총 {myCar2.count}대 입니다")