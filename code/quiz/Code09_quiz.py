import urllib.request
import bs4
import openpyxl
import csv

bookUrl = 'https://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05'
htmlObject = urllib.request.urlopen(bookUrl) 
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

xlsxName = f'C:\\sqlite\\mysql\\code\\quiz\\bookquiz.xlsx'
with open(xlsxName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['도서명', '저자', '출판사', '출간일', '가격'])




