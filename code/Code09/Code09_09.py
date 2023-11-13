import bs4

webPage = open('C:\\sqlite\\mysql\\code\\HTML\\Sample02.html', 'rt', encoding='utf-8')
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag_li_all = bsObject.findAll('li')
for tag_li in tag_li_all:
    print(tag_li)
# print()
for i in range(len(tag_li_all)):
    print(tag_li_all[i].text)