import xlrd
import csv 

workbook = xlrd.open_workbook('C:\\sqlite\\mysql\\code\\excel\\singer.xls') # 엑셀 -> csv 변환

wsheetList = workbook.sheets() # 시트 변수에 저장
# print(wsheetList)
for worksheet in wsheetList: # siniro, junior
    with open('C:\\sqlite\\mysql\\code\\excel\\singer_'+ worksheet.name + '.csv', 'w', newline='') as outFp:
        csvWriter = csv.writer(outFp) # outFp를 csv형식 list형식으로 저장
        print(csvWriter)
        for row in range(worksheet.nrows): #worksheet 행을 차례대로 row에 저장
            print('r',row)
            row_list = worksheet.row_values(row)
            print(row_list)
            csvWriter.writerow(row_list)

print('save')