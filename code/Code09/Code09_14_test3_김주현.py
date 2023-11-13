import bs4
import urllib.request

## 함수 선언부
def gettagsInfo(New_tag) :

    tags = New_tag.find("span", {"class": "text"}).text

    names = New_tag.find("small", {"class": "author"}).text

    return [tags, names]

    

NewsUrl = "https://quotes.toscrape.com/"

htmlObject = urllib.request.urlopen(NewsUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')


all_news = bsObject.findAll('div', {'class': 'quote'})


i = 0

for news in all_news :
    i += 1
    print(i,'번째 인용구 :',*gettagsInfo(news))
    

