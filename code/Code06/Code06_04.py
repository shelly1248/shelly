with open("C:\\sqlite\\mysql\\code\\Code06\\singer1.csv", 'r') as inFp: # 읽기
    with open('C:\\sqlite\\mysql\\code\\Code06\\singer2.csv', 'w') as outFp: # 쓰기
        header = inFp.readline() # 한줄 헤더에 저장

        outFp.write(header) #헤더 쓰기
        for inStr in inFp: 
            inStr = inStr.strip()
            row_list = inStr.split(',')
            row_list[-1] = row_list[-1].replace('.', '/') # 리스트 가장 뒤에 값(데뷔일자)를 .에서/로 변경
            height_str = "{0:.2f}".format(int(row_list[-2])) # 끝에서 2번째 소숫점 2째자리까지 나타내라
            row_list[-2] = height_str #  row_list[-2]에 다시 저장
            row_str = ','.join(map(str, row_list)) 
            # ','<- 다시 넣기 jojn<- 테이블과 테이블을 엮어서 하나의 테이블 제작
            # map <-리스트를 str형으로 모두 변환
            outFp.write(row_str + '\n') # outFp에 다시 쓰기
print('save')