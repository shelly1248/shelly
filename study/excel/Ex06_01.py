import csv
import glob
import os

# 전역 변수부
file_list = glob.glob(os.path.join('C:\\sqlite\\mysql\\code\\excel\\', '*.csv'))
# print(file_list)
firstYN = True


# 메인 코드
for input_file in file_list:
    # print(input_file)
    with open(input_file, 'r') as inFp:
        with open('C:\\sqlite\\mysql\\code\\excel\\강원인구통합.csv', 'a', newline='') as outFp: # 'a' = append
            csvReader = csv.reader(inFp)
            # print(csvReader)
            csvWriter = csv.writer(outFp)
            # print(csvReader)
            header_list = next(csvReader)
            print(header_list)

            if firstYN == True:
                csvWriter.writerow(header_list)
                firstYN = False

            for row_list in csvReader:
                csvWriter.writerow(row_list)