import xlrd # 읽기
import xlwt # 쓰기

workbook = xlrd.open_workbook('C:\\sqlite\\mysql\\code\\excel\\singer.xls') # 열기
outWorkbook = xlwt.Workbook() # 쓰기
print(outWorkbook)
idx = 2 # 평균 키의 인덱스

wsheetList = workbook.sheets()
# print(wsheetList)
outSheet = outWorkbook.add_sheet('singer')
# print(outSheet)
worksheet = wsheetList[0] # 0:<senior>, 1:<junior>
# print(worksheet)
for col in range(worksheet.ncols): # 헤더
    outSheet.write(0, col, worksheet.cell_value(0, col))

totalRow = 0
for worksheet in wsheetList:
    for row in range(1, worksheet.nrows):
        height = worksheet.cell_value(row, idx)
        if int(height) >= 6:
            totalRow += 1 #행위치를 누적시키면서 내려옴
            for col in range(worksheet.ncols):
                outSheet.write(totalRow, col, worksheet.cell_value(row, col))

outWorkbook.save('C:\\sqlite\\mysql\\code\\excel\\outsinger3.xls')
print('save')
