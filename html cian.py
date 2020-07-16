import requests
from bs4 import BeautifulSoup
import os, datetime
#input_list = ['test', 'https://spb.cian.ru/newobjects/list/?deal_type=sale&engine_version=2&offer_type=newobject&region=-2&year%5B0%5D=2018&p=13',
#              1, 'https://spb.cian.ru/newobjects/list/?deal_type=sale&engine_version=2&offer_type=newobject&region=-2&year%5B0%5D=2018&p=12',
#              1, 'https://spb.cian.ru/newobjects/list/?deal_type=sale&engine_version=2&offer_type=newobject&region=-2&year%5B0%5D=2018&p=11',
#              1, 'https://spb.cian.ru/newobjects/list/?deal_type=sale&engine_version=2&offer_type=newobject&region=-2&year%5B0%5D=2018&p=10', 0]
all_input = ''
c = 0
fname = input('Введите название файла:')
#fname = str(input_list[c])
c = c + 1


all_input = all_input + fname + '\n'
flag = 1
urls = list()
while(flag):
    url = input('Введите URL:')

    #url = input_list[c]
    #c = c + 1

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

    #flag = str(input_list[c])
    c = c + 1

    all_input = all_input + flag + '\n'
    if flag == '1':
        pass
    if flag == '0':
        break


urls = list(set(urls))
print('len:', len(urls))


list_urls = [[], [], [], []]
count = 0
if len(urls) > 50:
    count_lists = len(urls) // 50 + 1
    count = count_lists
    for i in range(count_lists):
        for j in range(50):
            a = 50*i+j
            if a < len(urls):
                list_urls[i].append(urls[a])

time = datetime.datetime.today().strftime("%d.%m")
path = '/Users/qeepnet/Desktop/urls'
path = os.path.join(path, time)
try:
    os.mkdir(path)
except:
    print('ALRDY RDY')
path2 = os.path.join(path, fname)
try:
    os.mkdir(path2)
except:
    print('ALRDY RDY2')
if count == 0:
    with open(path2 + '/' + fname + '.txt', 'w') as fout:
        for elem in urls:
            elem = elem[8:-1]
            if 'stati' not in elem:
                # ZHILOY /zhiloy
                # fout.write(elem[elem.index('/'):])
                # fout.write('\n')
                # WWW
                elem = elem[4:]
                fout.write(elem)
                fout.write('\n')
else:
    for i in range(count):
        with open(path2 + '/' + fname + str(i) + '.txt', 'w') as fout:
            for elem in list_urls[i]:
                elem = elem[8:-1]
                if 'stati' not in elem:
                    # ZHILOY /zhiloy
                    # fout.write(elem[elem.index('/'):])
                    # fout.write('\n')
                    # WWW
                    if elem.startswith('www'):
                        elem = elem[4:]
                fout.write(elem)
                fout.write('\n')
with open(path2 + '/' + fname +  '_LOG.txt','w') as outfile:
    outfile.write('LOG\n')
    outfile.write(all_input)

