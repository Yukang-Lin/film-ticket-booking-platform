import parsel
import re
import csv
f=open("ticket-html.txt","r")
html_data=f.read()
# print(html_data)
parse=parsel.Selector(html_data)
containers=parse.css('.container div').getall()
plists=[]
# <div class="show-list
for container in containers:
    if not re.findall('<div class="show-list.*?',container)==[]:
        plists.append(container)

for i in  range(1,len(plists)):
    print(str(i)+':')
    print(plists[i])
for plist in plists:
    timespan=re.findall('<span class="value">(.*?)分钟',plist)
    timespan=timespan[0]+'分钟'
    actors=re.findall('<a class="text-link" href="/films/celebrity/.*?" target="_blank"> (.*?)</a>',plist)
    actor=actors[0]
    # print(actor)
    plist=parsel.Selector(plist)
    moviename=plist.css('.movie-name ::text').get()
    score=plist.css('.score ::text').get()
    type=plist.css('.text-link ::text').get()
    print(moviename,score,timespan,type,actor,sep='|')
    with open('film.csv',mode='a',newline='') as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow([moviename,score,timespan,type,actor])

