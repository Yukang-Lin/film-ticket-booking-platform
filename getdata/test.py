import requests
import parsel
import csv
import time

url='https://maoyan.com/board/4?offset=0'
kv={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
response=requests.get(url,headers=kv)
html_data=response.text
print(response.text)
# html_data = response.text
#
# parse = parsel.Selector(html_data)
# dds = parse.css('.board-wrapper dd')
#
# for dd in dds:
#     name = dd.css('.name a::attr(title)').get()
#     star = dd.css('.star::text').get().strip()
#     releasetime = dd.css('.releasetime::text').get()
#     score = dd.css('.score i::text').getall()
#     score = ''.join(score)
#     print(name, star, releasetime, score, sep='|')
#
#     with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
#         csv_writer = csv.writer(f)
#         csv_writer.writerow([name, star, releasetime, score])