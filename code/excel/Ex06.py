import csv
import glob
import os

# 파일합치기==========================================================
file_list = glob.glob(os.path.join('C:\\sqlite\\mysql\\code\\excel\\실거래가\\', '*.csv'))
# print(file_list)
firstYN = True


# 파일 합치기=============================================================
for input_file in file_list:
    # print(input_file)
    with open(input_file, 'r') as inFp:
        with open('C:\\sqlite\\mysql\\code\\excel\\실거래가\\csv병합결과체줄.csv', 'a', newline='') as outFp: # 'a' = append
            csvReader = csv.reader(inFp)
            # print(csvReader)
            csvWriter = csv.writer(outFp)
            # print(csvReader)
            header_list = next(csvReader)
            # print(header_list)

            if firstYN == True:
                csvWriter.writerow(header_list)
                firstYN = False

            for row_list in csvReader:
                csvWriter.writerow(row_list)


# 가격추출 ==============================================================
max_temp = -999
max_data = ''
f = open('C:\\sqlite\\mysql\\code\\excel\\실거래가\\csv병합결과체줄.csv')
data = csv.reader(f)
header = next(data)


# 가격추출=================================================================
for row_list in data:
        youtube = int(row_list[8].replace(',','')) # ','를'' 대치 
        row_list[8] = youtube

        if max_temp < row_list[8]:
            max_date = row_list[8]
            max_temp = row_list[8]




f.close()
print(f'{max_temp}만')
