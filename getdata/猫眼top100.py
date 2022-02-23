import requests
import parsel
import csv
import time
page=0
for i in range(90,91,10):
    page+=1
    print('========正在爬取第{}页数据======='.format(page))
    url='https://maoyan.com/board/4?offset={}'.format(i)
    kv={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    response=requests.get(url,headers=kv)
    response.encoding=response.apparent_encoding
    html_data=response.text
    print(html_data)

    parse=parsel.Selector(html_data)
    dds=parse.css('.board-wrapper dd')

    for dd in dds:
        name=dd.css('.name a::attr(title)').get()
        star=dd.css('.star::text').get().strip()
        releasetime=dd.css('.releasetime::text').get()
        score=dd.css('.score i::text').getall()
        score=''.join(score)
        print(name,star,releasetime,score,sep='|')

        with open('top100.csv',mode='a',encoding='utf-8',newline='') as f:
            csv_writer=csv.writer(f)
            csv_writer.writerow([name,star,releasetime,score])

    time.sleep(2)

