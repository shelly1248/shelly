import bs4
import urllib.request

## 함수 선언부
def getBookInfo(book_tag) :
    names = book_tag.find("div", {"class": "goods_name"})
    bookName = names.find("a").text
    auths = book_tag.find("span", {"class": "goods_auth"})
    bookAuth = auths.find("a").text
    bookPub = book_tag.find("span", {"class": "goods_pub"}).text
    bookDate = book_tag.find("span", {"class": "goods_date"}).text
    bookPrice = book_tag.find("em", {"class": "yes_b"}).text
    return [bookName, bookAuth, bookPub, bookDate, bookPrice]



# ## 전역 변수부
for i in range(0,30):
    bookUrl = "http://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber="+str(i)
    # print(i)
totalprice = 0


# ## 메인 코드부
htmlObject = urllib.request.urlopen(bookUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
tag = bsObject.find('ul', {'class': 'clearfix'})
all_books = tag.findAll('div', {'class': 'goods_info'})

for i in range(0,30):
    if i <31:
        for book in all_books :
            ret_list = getBookInfo(book)
            price = ret_list[-1].replace(',','') # 마지막 가격, 콤마 제거
            totalprice += int(price)
            print(ret_list)
print(totalprice)



