import xlrd #라이브러리

workbook = xlrd.open_workbook('C:\\sqlite\\mysql\\code\\excel\\singer.xls')
print(workbook)
sheetCount = workbook.nsheets
print(f'워크시트는 {sheetCount}개 입니다')

wsheetList = workbook.sheets()
print(wsheetList)
for worksheet in wsheetList:
    print(f'** 워크시트의 이름: {worksheet.name}')
    print(f'행 수 는 {worksheet.nrows}, 열 개수는 {worksheet.ncols}') # nrows 행 ncols 열