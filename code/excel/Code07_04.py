import xlrd
import xlwt

workbook = xlrd.open_workbook('C:\\sqlite\\mysql\\code\\excel\\singer.xls')
outWorkbook = xlwt.Workbook()

wsheetList = workbook.sheets()
for worksheet in wsheetList:
    outSheet = outWorkbook.add_sheet(worksheet.name)
    for row in range(worksheet.nrows):
        for col in range(worksheet.ncols):
            outSheet.write(row, col, worksheet.cell_value(row, col))

outWorkbook.save('C:\\sqlite\\mysql\\code\\excel\\outSinger1.xls')
print('save')