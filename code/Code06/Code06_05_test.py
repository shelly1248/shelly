with open('C:\\sqlite\\mysql\\code\\Code06\\singer1.csv', 'r') as inFp:
    with open('C:\\sqlite\\mysql\\code\\Code06\\newsinger3.csv', 'w') as outFp:
        header = inFp.readline()
        header = header.strip() # \n 제거
        header_list = header.split(',') # , 제거
        idx1 = header_list.index('이름') #index(위치)-> 아이디0번째 이름1번째 키6번째 
        # print('idx1', idx1)
        idx2 = header_list.index('국번') #index(위치)-> 아이디0번째 이름1번째 키6번째 
        # print('idx2', idx2)
        idx3 = header_list.index('전화 번호') #index(위치)-> 아이디0번째 이름1번째 키6번째 
        # print('idx3', idx3)
        header_list = [header_list[idx1], header_list[idx2], header_list[idx3]] 
        # header_list리스트형태로 header_list리스트 만들기
        header_str = ','.join(map(str, header_list))
        # header_list를 str 형태로 만들기
        # ,로 join
        outFp.write(header_str + '\n')
        # outFp에 쓰고 \n 다시넣기
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            if row_list[idx3] != '': # idx3(키)가 165와 같거나 작으면 True
                row_list = [row_list[idx1], row_list[idx2], row_list[idx3]] 
                # idx1(아이디), idx2(이름), idx3(평균 키)를 row_list에 리스트 형태로 저장
                row_str = ','.join(map(str, row_list))
                # row_list를 str형태로 변환 후 ','로 join
                outFp.write(row_str + '\n')
                #outFp에 쓰고 \n 다시넣기

print('save')