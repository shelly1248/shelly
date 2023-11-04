def printList(pList): 
    for data in pList:
        print(data, end='\t')
    print()

with open("C:\\sqlite\\mysql\\code\\Code06\\singer1.csv", 'r') as inFp:
    header = inFp.readline()
    # print('!!', header)
    header = header.strip() # 앞뒤 공백제거 /<-라인 제거
    header_list = header.split(',') # ',' <-제거
    printList(header_list) # 함수
    

    # for inStr in inFp:
    #     inStr = inStr.strip()
        
    #     row_list = inStr.split(',')
        
    #     printList(row_list)