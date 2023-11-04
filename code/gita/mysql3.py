import pymysql

#변수 선언 부분
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# 메인 코드 부분
con = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='shopDB', charset='utf8')
cur = con.cursor()


while(True):
    data1 = input("사용자 ID ==> ")
    if data1 == "":
        break
    data2 = input("사용자 이름 ==> ")
    data3 = input("사용자 이메일 ==> ")
    data4 = input("사용자 출생연도 ==> ")
    sql = "INSERT INTO num1tbl VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', " + data4 + ")"
    cur.execute(sql) # 실행 execute

# cur.execute('SELECT email, birthYear FROM studentTable WHERE birthYear >= 2000')

cur.execute('SELECT * FROM num1tbl')

print('사용자 ID        사용자이름       이메일        출생연도')
print('--------------------------------------------------------')

while(True):
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print(f'{data1}             {data2}         {data3}    {data4}')


