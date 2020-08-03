import requests
from bs4 import BeautifulSoup
import os, datetime
import pyperclip, collections
fname = input('Введите название файла:')
all_input = ''

all_input = all_input + fname + '\n'
flag = 1
urls = list()
input_url = {}
while(flag):
    url = input('Введите URL:')

    all_input = all_input + url + '\n'
    r = requests.get(url)
    with open('text.html', 'w') as output_file:
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
                    if i == 0:
                        temp = temp + elem + '\n'

    pyperclip.copy(temp)
with open(path2 + '/' + fname +  '_LOG.txt','w') as outfile:
    outfile.write('LOG\n')
    outfile.write(all_input)

#new method
#cross = []
#for elem in input_url.values():
#    for wot in elem:
#        cross.append(wot)
#for i in range(len(input_url.values())):
#    list_of_values = list(input_url.values())
#    cross = list(set(cross) & set(list_of_values[i]))

#new method 2
cross = []
list_of_values = list(input_url.values())
for elem in list_of_values:
    i = 0
    for wot in elem:
        if elem != list_of_values[i]:
            k=0
            for j in range(len(list_of_values)):
                if wot in list_of_values[j]:
                    k += 1
            if k == len(list_of_values) or k == len(list_of_values) - 2 or k == len(list_of_values) - 1:
                cross.append(wot)
cross = list(set(cross))
print('Cross len:', len(cross))
temp = ''
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
            temp = temp + elem + '\n'
    #pyperclip.copy(temp)
