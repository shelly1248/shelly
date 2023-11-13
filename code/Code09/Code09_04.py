import bs4

webPage = open('C:\\sqlite\\mysql\\code\\HTML\\Sample02.html', 'rt', encoding='utf-8').read() # 'rt' readtext
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
# print(bsObject)
tag_div = bsObject.find('div') # 중요
# print(tag_div)
print(tag_div.text)