# 507/206 Homework 6 Part 1
#Gabby Truong
import requests
from bs4 import BeautifulSoup
import sys

#### Part 1 ####
url = sys.argv[1]
#print(url)
#http://newmantaylor.com/gallery.html
print('\n*********** PART 1 ***********')
print("Mark's page -- Alt tags\n")

### Your Part 1 solution goes here

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
#print(soup)

imgs = soup.find_all('img')
#print(imgs)

for i in imgs:
#prints attributes
    try: #or if "alt" is in i.attrs:
        print(i['alt']) #print(i['alt'])
    except:
        print("No Alternate Text Provided!")
