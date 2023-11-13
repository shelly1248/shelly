import bs4
import urllib.request
import time

## 함수 선언부
def getBookInfo(News_tag) :

    names = News_tag.find("span", {"class": "tb"})
    bookName = names.find("h2").text


    a_list = News_tag.find('a')
    newslink = a_list['href']

    newnames = News_tag.find("span", {"class": "medium"}).text
    newname = newnames.split()
    newname1 = newname[:]


    # check = newnames.find("em").text

    return [bookName, newslink, *newname1]

    

NewsUrl = "https://news.nate.com/recent?mid=n0100"

htmlObject = urllib.request.urlopen(NewsUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
tag = bsObject.find('div', {'id': 'newsContents'})
all_news = tag.findAll('div', {'class': 'mlt01'})



for news in all_news :
    
    print(getBookInfo(news))

time.sleep(60)
# newnames = tag.find("span", {"class": "medium"}).text
# newname = newnames.split()
# print(newname)
