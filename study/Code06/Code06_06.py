with open('C:\\sqlite\\mysql\\code\\Code06\\singer2.csv','r') as inFp:
    header = inFp.readline()
    header = header.strip()
    print(header)
    header_list = header.split(',')
    print(header_list[1], header_list[6])
    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        print(row_list[6])
        # youtube = int(row_list[6])
        # youtube = int(youtube/10000)
        # print(row_list[0], str(youtube+'만'))