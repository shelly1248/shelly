import csv

with open('C:\\sqlite\\mysql\\code\\Code06\\singerA.csv','r') as inFpA:
    with open('C:\\sqlite\\mysql\\code\\Code06\\singerB.csv', 'r') as inFpB:
        with open('C:\\sqlite\\mysql\\code\\Code06\\singerSum.csv', 'w', newline='') as outFp:
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)
            header_list = next(csvReaderA) # next 한줄씩 리스트로 변환
            header_list = next(csvReaderB) # next 한줄씩 리스트로 변환
            print(header_list)
            csvWriter.writerow(header_list)


            for row_list in csvReaderA:
                print(row_list)
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                print(row_list)
                csvWriter.writerow(row_list)

            