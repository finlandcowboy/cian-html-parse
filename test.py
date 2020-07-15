import requests
from bs4 import BeautifulSoup
flag = 1
urls = list()
while(flag):
    url = input('Введите URL:')
    r = requests.get(url)
    with open('text.html','w') as output_file:
        output_file.write(r.text)


    soup = BeautifulSoup(r.text, 'lxml')

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

list_urls = [[], [], [], []]
urls = list(set(urls))
print('URLS:', urls)
print('len', len(urls))
if len(urls) > 50:
    count_lists = len(urls) // 50 + 1
    for i in range(count_lists):
        for j in range(50):
            a = 50*i+j
            if a < len(urls):
                print(a)
                list_urls[i].append(urls[a])
