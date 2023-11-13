import csv 

with open('C:\\sqlite\\mysql\\code\\Code06\\singer2.csv', 'r') as inFp:
    csvReader = csv.reader(inFp) # csv 전용 reader
    header_list = next(csvReader) # next가 리스트로 반환
    # print(header_list)
    # print(header_list[1], header_list[6])
    for row_list in csvReader:
        youtube = int(row_list[6].replace(',','')) # ','를'' 대치 
        youtube = int(youtube/10000)
        print(row_list[1], str(youtube)+'만')