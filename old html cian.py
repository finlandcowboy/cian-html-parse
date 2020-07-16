import requests
from bs4 import BeautifulSoup
all_input = ''
fname = input('Введите название файла:')
all_input = all_input + fname + '\n'
flag = 1
urls = list()
while(flag):
    url = input('Введите URL:')
    all_input = all_input + url + '\n'
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
    all_input = all_input + flag + '\n'
    if flag == '1':
        pass
    if flag == '0':
        break
urls1, urls2, urls3, urls4 = list(), list(), list(), list()

urls = set(urls)

print(len(urls))
print('URLS1:', urls1, 'URLS2:', urls2, 'URLS3:', urls3, 'URLS4:', urls4)
with open('/Users/qeepnet/Desktop/urls/15.07/' + fname + '.txt', 'w') as fout:
    fout.write('LOG\n')
    fout.write(all_input)
    fout.write('\n\n\nURLS:\n')
    for elem in urls:
        elem = elem[8:-1]
        if 'stati' not in elem:
            #ZHILOY /zhiloy
            #fout.write(elem[elem.index('/'):])
            #fout.write('\n')
            #WWW
            if elem.startswith('www'):
                elem = elem[4:]

            #NO WWW
            fout.write(elem)
            fout.write('\n')
