import bs4
import urllib.request
import csv
import time

csvName = 'C:\\sqlite\\mysql\\code\\Code09\\booktime.csv'
with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['순위','도서명'])


## 함수 선언부
def getBookInfo(book_tag) :
    names = book_tag.find("div", {"class": "goods_name"})
    bookName = names.find("a").text

    return [bookName]

## 전역 변수부
bookUrl = "https://www.yes24.com/24/Category/Display/001001003022004"

## 메인 코드부
htmlObject = urllib.request.urlopen(bookUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
tag = bsObject.find('ul', {'class': 'clearfix'})
all_books = tag.findAll('div', {'class': 'cCont_goodsSet'})

while True:
    time.sleep(10)
    for book in all_books :
        with open(csvName, 'a', newline='') as csvFp:
            csvWriter = csv.writer(csvFp)
            csvWriter.writerow(getBookInfo(book))
            
            
    print('save')
    

