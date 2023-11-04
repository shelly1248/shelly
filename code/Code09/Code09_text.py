import urllib.request
import bs4 #

nateUrl = 'https://www.nate.com'
htmlObject = urllib.request.urlopen(nateUrl) 
# webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(htmlObject, 'html.parser')


tag = bsObject.find('div', {'id' : 'NateBi'}) 
# print(tag)


a_tag = tag.find("a")
# print(a_tag)


href = a_tag['href']
print(href, '\n')

# text = a_tag.text
# print(text)
    