from Day2_module import *

def main():
    process_menu = {1:List, 2:Print_list, 3:Search_name}
    while True:
        if Menu() == 4:
            break
        Menu()

if __name__ == '__main__':
    main()        