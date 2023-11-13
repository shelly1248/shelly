import bs4

webPage = open('C:\\sqlite\\mysql\\code\\HTML\\Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# tag_ul = bsObject.find('ul')
# print(tag_ul)

# tag_li = bsObject.find('li')
# print(tag_li)

# tag_lk = bsObject.find('li')
# print(tag_lk)

tag_li_all = bsObject.findAll('li') # 리스트에 한줄로 출력
print(tag_li_all)
