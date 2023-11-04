import random # 모듈 선언

class BaseballGame: # 클래스 선언
    def selectNumbers(self): #함수 선언
        samples = [n for n in range(1, 10)] # 1~9까지 samples에 저장
        random.shuffle(samples) # 랜덤 셔플
        self._data = samples[0:3] # 슬라이싱 0~2
       

    def verifyinput(self, value):
        if value < 1 or value > 9: # value 값이 1보다 크거나 9보다 작은것
            raise Exception("Wrong number entered. Please, try again") # if문이 True가 되면 에러메시지 작동
        
    def getNumbers(self):
        print("Enter 3 numbers (1 ~ 9)(input exam:3 6 9):", end="")
        try:
            s1 = input("")
            n1 = int( s1[0] ) #값 정수로 저장
            n2 = int( s1[2] )
            n3 = int( s1[4] )
            self.verifyinput(n1) # verifyinput 확인 후 조건 충족 확인
            self.verifyinput(n2)
            self.verifyinput(n3)
        except Exception as ex: # 예외 처리 에러발생 list 데이터 반환
            print("error",ex)
            return list()
        else:
            return [n1, n2, n3] # n1~3 반환

    def judge(self, numbers):
        strikes = 0
        balls = 0
        for i in range(3): 
            if self._data[i] == numbers[i]: # 데이터값 맞출때마다 스트라이크1씩 증가
                strikes += 1
            elif numbers[i] in self._data: # 데이터 값이 안에있으면 볼 1씩 증가
                balls += 1
        return strikes, balls # 스트라이크,볼 반환

    def playball(self):
        self.selectNumbers() # selectNumbers 호출
        is3Strikes = False 
        count = 0
        while is3Strikes == False: 
            numbers = self.getNumbers() 
            if len(numbers) < 3: # 넘버즈 길이가 3보다 작으면 건너뛰기
                continue
            judgeResult = self.judge(numbers)  
            is3Strikes = (judgeResult[0] == 3)
            if is3Strikes == False:
                print("Result: %d stike(s) and %d ball(s)" % judgeResult)
            count += 1
        print("You got the game in %d times" % count)

    def startGame(self):
        while True: # 게임이 시작됨
            print("Baseball Game")
            print("-" * 30)
            print("1. Playball~")
            print("2. Quit game")
            
            menu = int(input("select Num:")) 
            if menu == 2: # int 2가 입력되면 게임 종료
                break
            self.playball()

if __name__ == '__main__': 
    game = BaseballGame() # 인스턴스화 이소스는 생성자 생략
    game.startGame() # 객체변수 game을 사용해서 클래스 메소드 함수 호출