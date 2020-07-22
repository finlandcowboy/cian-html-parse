import requests
from bs4 import BeautifulSoup
import os, datetime
import pyperclip, collections
#input_list = ['сосновка',
#'https://spb.cian.ru/newobjects/list/?currency=2&deal_type=sale&engine_version=2&in_polygon%5B0%5D=30.2302_59.9892%2C30.2433_59.9991%2C30.2563_60.0081%2C30.2687_60.0174%2C30.2838_60.0253%2C30.3085_60.0256%2C30.3284_60.0291%2C30.3477_60.0253%2C30.3648_60.017%2C30.3841_60.0074%2C30.406_59.9988%2C30.4191_59.9892%2C30.4321_59.9795%2C30.4438_59.9709%2C30.4328_59.961%2C30.4211_59.952%2C30.4081_59.9437%2C30.3937_59.9362%2C30.3724_59.9355%2C30.3504_59.9396%2C30.3298_59.943%2C30.3058_59.9475%2C30.2797_59.9503%2C30.2584_59.9517%2C30.2378_59.9534%2C30.222_59.9613%2C30.2206_59.9727%2C30.211_59.9826%2C30.2151_59.9699%2C30.2316_59.9768&lat=60.0690146524&lon=30.6362188171&maxprice=29000000&minprice=15000000&offer_type=newobject&polygon_name%5B0%5D=%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0&room3=1&p=2',
#'1',
#'https://spb.cian.ru/newobjects/list/?currency=2&deal_type=sale&engine_version=2&in_polygon%5B0%5D=30.2302_59.9892%2C30.2433_59.9991%2C30.2563_60.0081%2C30.2687_60.0174%2C30.2838_60.0253%2C30.3085_60.0256%2C30.3284_60.0291%2C30.3477_60.0253%2C30.3648_60.017%2C30.3841_60.0074%2C30.406_59.9988%2C30.4191_59.9892%2C30.4321_59.9795%2C30.4438_59.9709%2C30.4328_59.961%2C30.4211_59.952%2C30.4081_59.9437%2C30.3937_59.9362%2C30.3724_59.9355%2C30.3504_59.9396%2C30.3298_59.943%2C30.3058_59.9475%2C30.2797_59.9503%2C30.2584_59.9517%2C30.2378_59.9534%2C30.222_59.9613%2C30.2206_59.9727%2C30.211_59.9826%2C30.2151_59.9699%2C30.2316_59.9768&lat=60.0690146524&lon=30.6362188171&maxprice=29000000&minprice=15000000&offer_type=newobject&polygon_name%5B0%5D=%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0&room3=1',
#'1',
#'https://spb.cian.ru/newobjects/list/?currency=2&deal_type=sale&engine_version=2&in_polygon%5B0%5D=30.2302_59.9892%2C30.2433_59.9991%2C30.2563_60.0081%2C30.2687_60.0174%2C30.2838_60.0253%2C30.3085_60.0256%2C30.3284_60.0291%2C30.3477_60.0253%2C30.3648_60.017%2C30.3841_60.0074%2C30.406_59.9988%2C30.4191_59.9892%2C30.4321_59.9795%2C30.4438_59.9709%2C30.4328_59.961%2C30.4211_59.952%2C30.4081_59.9437%2C30.3937_59.9362%2C30.3724_59.9355%2C30.3504_59.9396%2C30.3298_59.943%2C30.3058_59.9475%2C30.2797_59.9503%2C30.2584_59.9517%2C30.2378_59.9534%2C30.222_59.9613%2C30.2206_59.9727%2C30.211_59.9826%2C30.2151_59.9699%2C30.2316_59.9768%2C30.2302_59.9892&lat=60.0690146524&lon=30.6362188171&maxprice=24000000&minprice=15000000&offer_type=newobject&polygon_name%5B0%5D=%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0&room2=1',
#'1',
#'https://spb.cian.ru/newobjects/list?currency=2&deal_type=sale&engine_version=2&in_polygon%5B0%5D=30.2302_59.9892%2C30.2433_59.9991%2C30.2563_60.0081%2C30.2687_60.0174%2C30.2838_60.0253%2C30.3085_60.0256%2C30.3284_60.0291%2C30.3477_60.0253%2C30.3648_60.017%2C30.3841_60.0074%2C30.406_59.9988%2C30.4191_59.9892%2C30.4321_59.9795%2C30.4438_59.9709%2C30.4328_59.961%2C30.4211_59.952%2C30.4081_59.9437%2C30.3937_59.9362%2C30.3724_59.9355%2C30.3504_59.9396%2C30.3298_59.943%2C30.3058_59.9475%2C30.2797_59.9503%2C30.2584_59.9517%2C30.2378_59.9534%2C30.222_59.9613%2C30.2206_59.9727%2C30.211_59.9826%2C30.2151_59.9699%2C30.2316_59.9768%2C30.2302_59.9892&lat=60.0690146524&lon=30.6362188171&maxprice=24000000&minprice=15000000&offer_type=newobject&polygon_name%5B0%5D=%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0&room2=1&p=2',
#'1',
#'https://spb.cian.ru/newobjects/list/?currency=2&deal_type=sale&engine_version=2&in_polygon%5B0%5D=30.2302_59.9892%2C30.2433_59.9991%2C30.2563_60.0081%2C30.2687_60.0174%2C30.2838_60.0253%2C30.3085_60.0256%2C30.3284_60.0291%2C30.3477_60.0253%2C30.3648_60.017%2C30.3841_60.0074%2C30.406_59.9988%2C30.4191_59.9892%2C30.4321_59.9795%2C30.4438_59.9709%2C30.4328_59.961%2C30.4211_59.952%2C30.4081_59.9437%2C30.3937_59.9362%2C30.3724_59.9355%2C30.3504_59.9396%2C30.3298_59.943%2C30.3058_59.9475%2C30.2797_59.9503%2C30.2584_59.9517%2C30.2378_59.9534%2C30.222_59.9613%2C30.2206_59.9727%2C30.211_59.9826%2C30.2151_59.9699%2C30.2316_59.9768%2C30.2302_59.9892&lat=60.0690146524&lon=30.6362188171&maxprice=29000000&minprice=15000000&offer_type=newobject&polygon_name%5B0%5D=%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0&room3=1',
#'1',
#'https://spb.cian.ru/newobjects/list?currency=2&deal_type=sale&engine_version=2&in_polygon%5B0%5D=30.2302_59.9892%2C30.2433_59.9991%2C30.2563_60.0081%2C30.2687_60.0174%2C30.2838_60.0253%2C30.3085_60.0256%2C30.3284_60.0291%2C30.3477_60.0253%2C30.3648_60.017%2C30.3841_60.0074%2C30.406_59.9988%2C30.4191_59.9892%2C30.4321_59.9795%2C30.4438_59.9709%2C30.4328_59.961%2C30.4211_59.952%2C30.4081_59.9437%2C30.3937_59.9362%2C30.3724_59.9355%2C30.3504_59.9396%2C30.3298_59.943%2C30.3058_59.9475%2C30.2797_59.9503%2C30.2584_59.9517%2C30.2378_59.9534%2C30.222_59.9613%2C30.2206_59.9727%2C30.211_59.9826%2C30.2151_59.9699%2C30.2316_59.9768%2C30.2302_59.9892&lat=60.0690146524&lon=30.6362188171&maxprice=29000000&minprice=15000000&offer_type=newobject&polygon_name%5B0%5D=%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0&room3=1&p=2',
#'1',
#'https://spb.cian.ru/newobjects/list?currency=2&deal_type=sale&engine_version=2&in_polygon%5B0%5D=30.2302_59.9892%2C30.2433_59.9991%2C30.2563_60.0081%2C30.2687_60.0174%2C30.2838_60.0253%2C30.3085_60.0256%2C30.3284_60.0291%2C30.3477_60.0253%2C30.3648_60.017%2C30.3841_60.0074%2C30.406_59.9988%2C30.4191_59.9892%2C30.4321_59.9795%2C30.4438_59.9709%2C30.4328_59.961%2C30.4211_59.952%2C30.4081_59.9437%2C30.3937_59.9362%2C30.3724_59.9355%2C30.3504_59.9396%2C30.3298_59.943%2C30.3058_59.9475%2C30.2797_59.9503%2C30.2584_59.9517%2C30.2378_59.9534%2C30.222_59.9613%2C30.2206_59.9727%2C30.211_59.9826%2C30.2151_59.9699%2C30.2316_59.9768%2C30.2302_59.9892&lat=60.0690146524&lon=30.6362188171&maxprice=29000000&minprice=15000000&offer_type=newobject&polygon_name%5B0%5D=%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0&room3=1&p=3',
#'0']
#c = 0
fname = input('Введите название файла:')
#fname = str(input_list[c])
#c = c + 1
all_input = ''

all_input = all_input + fname + '\n'
flag = 1
urls = list()
input_url = {}
while(flag):
    url = input('Введите URL:')
    #url = input_list[c]
    #print('Fine:', c)
    #c = c + 1

    all_input = all_input + url + '\n'
    r = requests.get(url)
    with open('text.html','w') as output_file:
        output_file.write(r.text)

    sub_list = list()
    soup = BeautifulSoup(r.text, 'lxml')

    for find_url in soup.find_all(class_ = '_0fce717cdb--container--1Gxqr _0fce717cdb--container-background_color--transparent--3pvxk _0fce717cdb--container-display--inline-block--3bIEb'):
        try:
            find_url = find_url.find('a').get('href')
        except:
            pass
        if str(find_url).startswith('https'):
            urls.append(str(find_url))
            sub_list.append(find_url)
    flag = input('Надо еще? Да - 1 Нет - 0')
    input_url.update({url: sub_list})
    #flag = str(input_list[c])
    #c = c + 1

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

temp = ''
if count == 0:
    with open(path2 + '/' + fname + '.txt', 'w') as fout:
        for elem in urls:
            elem = elem[8:-1]
            if 'stati' not in elem:
                # ZHILOY /zhiloy
                # fout.write(elem[elem.index('/'):])
                # fout.write('\n')
                # WWW
                if elem.startswith('www'):
                    elem = elem[4:]
                temp = temp + elem + '\n'
                fout.write(elem)
                fout.write('\n')
    pyperclip.copy(temp)

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
                temp = temp + elem + '\n'

    pyperclip.copy(temp)
with open(path2 + '/' + fname +  '_LOG.txt','w') as outfile:
    outfile.write('LOG\n')
    outfile.write(all_input)

#new method
cross = []
for elem in input_url.values():
    for wot in elem:
        cross.append(wot)
for i in range(len(input_url.values())):
    list_of_values = list(input_url.values())
    cross = list(set(cross) & set(list_of_values[i]))

with open(path2 + '/' + fname + ' самые кайфы.txt', 'w') as fout:
    for elem in cross:
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

