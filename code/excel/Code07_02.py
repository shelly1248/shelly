import xlrd

workbook = xlrd.open_workbook('C:\\sqlite\\mysql\\code\\excel\\singer.xls')
sheetCount = workbook.nsheets
print(sheetCount)

wsheetList = workbook.sheets()
# print(wsheetList)

for worksheet in wsheetList:
    print(f'** 워크시트의 이름 : {worksheet.name}')
    for row in range(worksheet.nrows):
        # print(worksheet.nrows)
        for col in range(worksheet.ncols):
            #print(worksheet.ncols)
            print('%s' % worksheet.cell_value(row, col), end = '\t')
        print()
    print()