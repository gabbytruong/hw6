# 507/206 Homework 6 Part 2
#Gabby Truong

import requests
from bs4 import BeautifulSoup


#### Part 2 ####
print('\n*********** PART 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Part 2 solution goes here

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

most_read = soup.find('div', class_ ='panel-pane pane-mostread')
print(most_read)
for x in most_read.descendants:
    if x.name =='li':
        print(x.string)
    else:
        pass
