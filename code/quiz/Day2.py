from mysql.code.Day2_fn import *
import pymysql


# 메인 코드 부분
con = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='shopDB', charset='utf8')
cur = con.cursor()

    


def createTable(cur):
    try :
        q = "create table if not exists scores(name text, korean int, english int, math int)"
        cur.execute(q)
    except Exception as err:
        print("err:", err)

def main():
    # menu_exec= {1:menu_input, 2:menu_output, 3:menu_search, 4:menu_exit}
    menu_exec = {1:menu_input, 2:look }
    
    while True:
        menu()
        input_menu = int(input("번호를 입력하세요:"))
        if input_menu == 4:
            menu_exit()
            break
        else:
            if 0< input_menu < 4:
                menu_exec[input_menu]()
            else:
                print("1,2,3,4중에 입력하세요")
if __name__ == '__main__':
    createTable()
    main()
    