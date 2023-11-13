from random import randint

class Ball:
    def __init__(self):
        pass

    def generate_numbers(self):

        numbers = []
        i = 0
        new_number = 0
        while i < 3:
            new_number = randint(0, 9)
            if new_number not in numbers:
                numbers.append(new_number)
                i += 1
        print('0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.')
        return numbers


    def take_guess(self):
        print('숫자 3개를 하나씩 차례대로 입력하세요.')
        i = 0
        new_guess = []
        while i < 3:
            gue_number = int(input(f'{(i + 1)}번째 숫자를 입력하세요: '))
            if gue_number > 9:
                print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
                continue
            if gue_number in new_guess:
                print('중복되는 숫자입니다. 다시 입력하세요.')
            else:
                new_guess.append(gue_number)
                i += 1

        return new_guess


    def get_score(self, guess, solution):
        self.guess = guess
        self.solution = solution

        strike_count = 0
        ball_count = 0
        i = 0

        while i < len(self.guess):
            if self.guess[i] == self.solution[i]:
                strike_count += 1
                i += 1
            elif self.guess[i] in self.solution:
                ball_count += 1
                i += 1
            else:
                i += 1

        return strike_count, ball_count


    # 게임 시작
    def gamerun(self):
        
    
        ANSWER = self.generate_numbers()
        tries = 0

        while 1:
            GUESS = self.take_guess()
            strike, ball = self.get_score(GUESS, ANSWER)
            print(f'{strike}S {ball}B ')

            if strike == 3:
                tries += 1
                break
            else:
                tries += 1

        print(f'{tries}번 만에 맞추셨습니다.')
        replay = input('계속하시겠습니까? (y/n) : ')
        for i in replay:
            if replay == 'y':
                self.gamerun()
            if replay == 'n':
                print('종료')
                exit()

    # 게임종료
    def gameexit(self):
        print('종료')

    def start(self):
        while True:
            print('1.게임시작 2.종료')
            input_menu = int(input("번호를 입력하세요:"))
            if input_menu == 2:
                self.gameexit()
                break
            else:
                self.gamerun()

if __name__ == '__main__':
    game = Ball()
    game.start()


        
                
