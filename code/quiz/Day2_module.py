class addr:
    def __init__(self):
        addr_list = []

class Menu:
    def get_menu_num(self, menu_num):
            self.menu_num = menu_num
            print("메인메뉴)","1.입력","2.출력","3.검색","4.종료", sep="\n\t")
            self.menu_num = int(input("번호를 입력하세요:"))
            return menu_num

class List:
    def input_list(self, name, age, addr_list, keep_going):
        self.name = name
        self.age = age
        self.addr_list = addr_list
        self.keep_goging = keep_going

        while True:
            self.name = input("이름:")
            self.age = input("나이:")
            self.addr = input("주소:")
            self.addr_list.append({"name":self.name, "age":self.age, "addr":self.addr})
            self.keep_going = input("계속 입력하시겠습니까(y/n)?")
            if self.keep_going == "n":
                break



class Print_list:
    def print_list(self):
        print("-"*40)
        print("\t이름\t나이\t주소")
        print("-"*40)
        for n in self.addr_list:
            print("\t%(name)s\t%(age)s\t%(addr)s"%n)
class Search_name:       
    def search_name(self, name):
        self.name = name
        name = input("검색할 이름을 입력하세요:")
        for n in self.addr_list:
            if n["name"] == name:
                print("-"*40)
                print("\t이름\t나이\t주소")
                print("-"*40)
                print("\t%(name)s\t%(age)s\t%(addr)s"%n)
                break

