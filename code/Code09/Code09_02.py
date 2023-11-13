import urllib.request
import bs4 #

nateUrl = 'https://www.nate.com'
htmlObject = urllib.request.urlopen(nateUrl) 
print(htmlObject)
bsObject = bs4.BeautifulSoup(htmlObject, 'html.parser') # 정보를 해석

print(bsObject)