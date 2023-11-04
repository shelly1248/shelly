## 클래스 선언
class Car :
    speed = 0

    def upSpeed(self, value):
        self.speed = self.speed + value

    def downSpeed(self, value):
        self.speed = self.speed - value

class Sedan(Car):
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum
    
class Truck(Car):
    capacity = 0

    def getCapacity(self):
        return self.capacity
    
# 변수 선언
sedan1, truck1 = None, None

# 메인 코드 부분
sedan1 = Sedan()
truck1 = Truck()

sedan1.upSpeed(100)
truck1.upSpeed(80)

sedan1.seatNum = 5
truck1.capacity = 50

print(f'승용차의 속도는 {sedan1.speed} km, 좌석수는 {sedan1.getSeatNum()}개 입니다.')
print(f'트럭의 속도는 {truck1.speed} km, 총중량은 {truck1.getCapacity()}톤입니다.')