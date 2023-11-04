from bs4 import BeautifulSoup
import requests

NewsUrl = "https://news.daum.net/"
html = requests.get(NewsUrl)
soup = BeautifulSoup(html.text, "lxml")
tag = soup.find('ul', {'class': 'list_newsissue'})
all_news = tag.findAll('div', {'class': 'item_issue'})

f = open("C:\\sqlite\\mysql\\code\\Code09\\Code09_14_test4_김주현.txt",'w')



# # 함수 선언부
def getBookInfo(News_tag) :
    a_list = News_tag.find('a')
    newslink = a_list['href']

    response = requests.get(newslink)
    soup = BeautifulSoup(response.text, 'lxml')
    contents = soup.find("div",{"class":"article_view"}).find("section").findAll("p")[:-1]
    for p in contents:
        f.write(p.text)
        f.close()

    return[newslink , contents]
    

for news in all_news :
        # f2.write(getBookInfo(news))
        print(getBookInfo(news))


