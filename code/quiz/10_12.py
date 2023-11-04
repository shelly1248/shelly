import csv


with open('C:\sqlite\\mysql\\code\\quiz\\아파트(매매)__실거래가_20231011083655.csv', 'r') as inFp:
    with open('C:\sqlite\\mysql\\code\\quiz\\news2.csv', 'w') as outFp:
        csvReader = csv.reader(inFp) # csv 전용 reader
        header_list = next(csvReader) # next가 리스트로 반환
        idx1 = header_list.index('시군구') #index(위치)-> 아이디0번째 이름1번째 키6번째 
        # print('idx1', idx1)
        idx2 = header_list.index('거래금액(만원)') #index(위치)-> 아이디0번째 이름1번째 키6번째 
        # print('idx2', idx2)
        header_list = [header_list[idx1], header_list[idx2]] 
        # header_list리스트형태로 header_list리스트 만들기
        header_str = ','.join(map(str, header_list))
        # header_list를 str 형태로 만들기
        # ,로 join
        outFp.write(header_str + '\n')
        # outFp에 쓰고 \n 다시넣기
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            print(row_list[8])

            # if int(inStr[idx2]) >= 30000:
            #     row_list = [row_list[idx1], row_list[idx2]] 
            #     row_str = ','.join(map(str, row_list))
            #     outFp.write(row_str + '\n')
              
# print('save')