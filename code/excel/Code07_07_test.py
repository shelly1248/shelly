import xlrd # xls 만 가능
import csv

workbook = xlrd.open_workbook('C:\\sqlite\\mysql\\code\\excel\\singer.xls')
findcolumn = ['이름', '주소', '유튜브 조회수'] # 리스트
findindex = []
wsheetList = workbook.sheets()
worksheet = wsheetList[0]
header_list = worksheet.row_values(0)
for name in findcolumn:
    findindex.append(header_list.index(name))

wsheetList = workbook.sheets()
with open('C:\\sqlite\\mysql\\code\\excel\\singer_youtube.xls', 'w', newline='') as outFp:
    csvWriter = csv.writer(outFp)
    csvWriter.writerow(findcolumn) # 한행씩 써달라
    for worksheet in wsheetList:
        for row in range(1, worksheet.nrows): # 헤더때문에 1부터 시작
            findList = []
            for col in range(worksheet.ncols):
                if col in findindex:
                    findList.append(worksheet.row_values(row)[col])
            csvWriter.writerow(findList)

print('save')