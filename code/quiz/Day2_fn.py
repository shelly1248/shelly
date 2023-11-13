import pymysql
con, cur = None, None
name, age, eng, math = "", "", "", ""
sql = ""

Person = []


# 1.입력 2.보기 3. 삭제 4. 수정 5. 검색 6.정렬 7.종료
# ===============================================================
def basic_form():
    print("출력")
    print("="* 20 )               
    print("%10s%10s%10s" %("이름","나이","주소"))
    print("="* 20 ) 

# 메뉴===============================================================
    
def menu():
    print("main 메뉴")
    print("1.입력")
    print("2.보기")
    print("3.삭제")
    print("4.수정")
    print("5.검색")
    print("6.정렬")
    print("7.종료")

# 1.입력=================================================================

def menu_input():
    print("1.입력")
    name = input("이름:")
    age = int(input("나이:"))
    addr = input("주소:")
    Person.append(({"name":name, "age":age, "eng":eng, "math":math}))

# 2.보기=================================================================

def look():
    print('2.보기')
    cur.execute('SELECT * FROM gradetbl')
    print('이름        나이       영어        수학')
    print('-' * 20)
    row = cur.fetchone
    name = row[0]
    age = age[1]
    eng = eng[2]
    math = math[3]
    print(f'{name}             {age}         {eng}    {math}')


# 출력=================================================================

def menu_output():
    basic_form()
    print("="* 20 )
    for dt in Person:
        print("%(name)10s%(age)10d%(eng)10s%(math)10s" %dt)
        

# 검색=================================================================

def menu_search():
    print("검색")
    flag_for_search = False
    input_value  = input("검색할 이름을 입력하세요:")
    for dt in Person:
        temp_name = ("%(name)s" %dt)
        if input_value==temp_name :
            basic_form()
            print("%(name)10s%(age)10d%(eng)10s%(math)10s" %dt)
            flag_for_search = True
            break
    if flag_for_search == False:
        print("찾는사람이 없습니다")
        
# 종료=================================================================

def menu_exit():
    print("종료")

