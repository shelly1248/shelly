import urllib.request
import bs4 #

nateUrl = 'https://www.hanbit.co.kr/'
htmlObject = urllib.request.urlopen(nateUrl) 
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'id' : 'wrap_nav'}) 
# print(tag)

a_tag = tag.findAll("a")
# print(a_tag)

for i in range(len(a_tag)):
    print(a_tag[i].text,end=" ")