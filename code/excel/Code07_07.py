import xlwt
import csv
import os

csvFileList = ['C:\\sqlite\\mysql\\code\\excel\\singerA.csv','\\sqlite\\mysql\\code\\excel\\singerB.csv']
outWorkbook = xlwt.Workbook()

for csvFileName in csvFileList: # csv 파일을 csvFileName에 저장
    rowCount = 0 
    with open(csvFileName, 'r') as inFp: # csv파일을 inFp에 저장
        csvReader = csv.reader(inFp)  # inFp 읽기
        header_list = next(csvReader) # 헤더 설정 리스트로만들어짐
        #os.path.basename(경로/파일)은 경로/파일에서 파일명만 추출
        outSheet = outWorkbook.add_sheet(os.path.basename(csvFileName)) # 파일이름을 시트이름으로 저장
        for col in range(len(header_list)): # 헤더-> 열 갯수를 col에 차례대로 저장
            outSheet.write(rowCount, col, header_list[col]) # rowCount=행, col=열, heaer_list[col]= 내용물 작성
        for row_list in csvReader:
            rowCount += 1 # 행 1개씩 증가
            for col in range(len(row_list)):
                if row_list[col].isnumeric(): # 데이터가 숫자인지 판별
                    outSheet.write(rowCount, col, float(row_list[col])) # 숫자일경우 float로 변경
                else:
                    outSheet.write(rowCount, col, row_list[col]) # 아닐경우 그래도 입력

outWorkbook.save('\\sqlite\\mysql\\code\\excel\\singerCSV.csv')
print('save')