import requests
from bs4 import BeautifulSoup
source=requests.get('https://www.codechef.com/contests').text
soup=BeautifulSoup(source,'lxml')

row=[]
table=soup.find('table')
table_rows=table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    p=[i.text for i in td]
    row.append(p)
print(row[2])
for i in range(2,len(row)):
    print(row[i])
