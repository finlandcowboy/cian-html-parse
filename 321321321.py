import requests
from bs4 import BeautifulSoup

fname = input('Введите название файла:')
flag = 1
while(flag):
    url = input('Введите URL:')
    r = requests.get(url)
    with open('text.html','w') as output_file:
        output_file.write(r.text)

    urls = list()
    soup = BeautifulSoup(r.text, 'lxml')

    #find_url = soup.find_all('div', {'class': '_0fce717cdb--container--1Gxqr _0fce717cdb--container-background_color--transparent--3pvxk _0fce717cdb--container-display--inline-block--3bIEb'}).find(
    #'a').get('href')
    for find_url in soup.find_all(class_ = '_0fce717cdb--container--1Gxqr _0fce717cdb--container-background_color--transparent--3pvxk _0fce717cdb--container-display--inline-block--3bIEb'):
        try:
            find_url = find_url.find('a').get('href')
        except:
            pass
        if str(find_url).startswith('https'):
            urls.append(str(find_url))
    flag = input('Надо еще? Да - 1 Нет - 0')
    if flag == '1':
        pass
    if flag == '0':
        break
urls = set(urls)
with open('/Users/qeepnet/Desktop/urls/' + fname + '.txt', 'w') as fout:
    for elem in urls:
        fout.write(elem)
        fout.write('\n')