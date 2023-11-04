import bs4

webPage = open('C:\\sqlite\\mysql\\code\\HTML\\Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

print(bsObject)