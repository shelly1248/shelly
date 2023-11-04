import bs4

webPage = open('C:\\sqlite\\mysql\\code\\HTML\\Sample03.html', 'rt', encoding='utf-8')
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

a_list = bsObject.findAll('a')
print(a_list)
for aTag in a_list:
    print(aTag['href'])