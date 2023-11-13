import xlrd

workbook = xlrd.open_workbook('C:\\sqlite\\mysql\\code\\excel\\singer.xls')
sheetCount = workbook.nsheets

personNum = 0
personIdx = 2 # 인원이 2번째(0, 1, (2))
rowCount = 0
wsheetList = workbook.sheets()
for worksheet in wsheetList:
    # print(worksheet)
    # print('rowCount', rowCount)
    rowCount += worksheet.nrows-1 # 행에서 -1 ? 헤더 행 빼기 위해서
    print('rowCount', rowCount)
    for row in range(1, worksheet.nrows): # 1 이유 ? 헤더값 제외 반복
        personNum += int(worksheet.cell_value(row, personIdx)) # sellvalue가 personNum에 누적됨

print('전체 가수그룹 인원 합계 :', personNum)
print('가수그룹 인원 평균 : ', personNum/rowCount)