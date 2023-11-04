import csv
import time
import datetime
import urllib.request
import bs4 



csvName = 'C:\\sqlite\\mysql\\code\\Code09\\datetime2.csv'
with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초','온도','습도','강수량','풍향'])

nateUrl = 'https://news.nate.com/weather?areaCode=11D20401'
htmlObject = urllib.request.urlopen(nateUrl) 
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')



while True:

    now = datetime.datetime.now()
    # print(now)
    tag = bsObject.find('p', {'class' : 'humidity'})
    tag_t = tag.text
    
    tag = bsObject.find('p', {'class' : 'rainfall'})
    tag_r = tag.text
    # print(tag_r)
    tag = bsObject.find('p', {'class' : 'wind'})
    tag_w = tag.text


    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H:%M:%S')
    time_list = [yymmdd, hhmmss, tag_t,  tag_r, tag_w]
    print(time_list)

    with open(csvName, 'a', newline='') as csvFp:
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(time_list)

    time.sleep(10)


    