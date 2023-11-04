parking = []
top = 0
carname = "A"
out = ''

while True:
    cargame = int(input('<1>자동차 넣기 <2>자동차 빼기 <3>끝 : '))

    if cargame == 1:
        if top > 5:
            print('만차')
        else:
            parking.append(carname)
            print(f"{parking[top]} 자동차가 입차됩니다. 주차장 상태 {parking}")
            top += 1
            carname=chr(ord(carname)+1)
    elif cargame == 2:
        if top == 0:
            print('빠져나갈 자동차가 없음')
        else:
            out = parking.pop()
            print(f'{out}가 나감. 주차장 상태{parking}')
            top -= 1
            carname=chr(ord(carname)-1)
    elif cargame == 3:
        print('종료')
        print(f'현재 주차장에 {top}대 있습니다.')
        exit()
    else:
        print('잘못 입력 하셨습니다.')
