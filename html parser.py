import requests
from bs4 import BeautifulSoup
fname = input('Введите название файла:')
url = 'https://arhangelsk.cian.ru/novostroyki/'
r = requests.get(url)
with open('text.html','w') as output_file:
    output_file.write(r.text)

soup = BeautifulSoup(r.text,'lxml')
urls = soup.find('div', {'data_name':'Container'}).find('a').get('href')
print(url)
with open('/Users/qeepnet/Desktop/urls/' + fname, 'w') as fout:
    fout.write(urls)
