import requests
import time
import re
import os
import sys
# kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
kv={'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
page=0
count=0
for i in range(0,91,10):
    page+=1
    url = 'https://maoyan.com/board/4?offset={}'.format(i)
    print('========正在爬取第{}页数据======='.format(page))
    response=requests.get(url,headers=kv)
    response.encoding=response.apparent_encoding
    html_data=response.text
    # print(html_data)
    # dir_name='top100urls'
    # if not os.path.exists(dir_name):
    #     os.mkdir(dir_name)
    #<img data-src="https://p1.meituan.net/movie/ed50b58bf636d207c56989872a91f4cf305138.jpg@160w_220h_1e_1c" alt="我爱你" class="board-img" />
    urls=re.findall('<img data-src="(.*?)" alt=".*?" class="board-img" />',html_data)
    f = open("top100urls.txt", "a")
    for i in range(0,10):
        print(urls[i])
        f.write(urls[i]+'\n')
    # if urls==[]:
    #     print('fail')
    #     sys.exit()
    # for url in urls:
    #     time.sleep(0.5)
    #     count+=1
    #     file_name=count
    #     response=requests.get(url,headers=kv)
    #     with open(dir_name+'/'+str(file_name)+'.jpg','wb') as f:
    #         f.write(response.content)
    time.sleep(2)

