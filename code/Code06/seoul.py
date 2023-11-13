import csv
max_temp = -999
max_data = ''
f = open('C:\\sqlite\\mysql\\code\\Code06\\seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data:
    if row[-1] =='':
        row[-1] =-999
    row[-1] = float(row[-1])

    if max_temp < row[-1]:
        max_date = row[0]
        max_temp = row[-1]

f.close()
print(f'기상 관측 이래 서울의 최고 기온이 가장 높았던 날은 {max_date}로 ,{max_temp}도 였습니다')