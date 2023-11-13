import bs4

webPage = open('C:\\sqlite\\mysql\\code\\HTML\\Sample03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'id' : 'myId1'}) # 'div' 태그명 'id'속성명 'myId1' 속성값
print(tag.text)

tag = bsObject.find('div', {'class' : 'myClass1'})
print(tag.text)

# tag = bsObject.findAll('div', {'class' : 'myClass1'}) # 리스트 변환
# print(tag)

tag = bsObject.findAll('div', {'class' : 'myClass1'}) # 'div' 태그명 'id'속성명 'myId1' 속성값
for t in tag:
    print(t.text)