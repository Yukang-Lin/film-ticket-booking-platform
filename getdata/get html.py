import requests

url='https://maoyan.com/cinema/14409?poi=86715464&movieId=3606'
kv={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
response=requests.get(url,headers=kv)
# response.encoding=response.apparent_encoding
html_data=response.text
print(html_data)
f=open("ticket-html.txt","w")
f.write(html_data)