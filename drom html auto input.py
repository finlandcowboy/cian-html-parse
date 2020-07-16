import requests
import os, datetime
from bs4 import BeautifulSoup
all_input = ''
input_list = str(input('string log: ')).split(' ')
c = 0
#fname = input("Введите название файла:")
fname = str(input_list[c])
c = c + 1

all_input = all_input + fname + ' '
flag = 1
urls = list()
while flag:
    #url = input("Введите URL:")
    url = input_list[c]
    c = c + 1

    all_input = all_input + url + ' '
    r = requests.get(url)
    with open('drom.html', 'w') as output_file:
        output_file.write(r.text)

    soup = BeautifulSoup(r.text, 'lxml')
    for find_url in soup.find_all(class_ = 'css-15mleww erw2ohd2'):
        try:
            find_url = find_url.get('href')
        except:
            pass
        urls.append(str(find_url))
    print('Len after append:', len(urls))
    #flag = input('Надо еще? Да - 1 Нет - 0')
    flag = str(input_list[c])
    c = c + 1


    all_input = all_input + flag + ' '
    if flag == '1':
        pass
    if flag == '0':
        break

urls = list(set(urls))
print('Amount:', len(urls))

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

for elem in list_urls:
    print('List:', elem)

time = datetime.datetime.today().strftime('%d.%m')
path = '/Users/qeepnet/Desktop/urls'
path = os.path.join(path, time)
try:
    os.mkdir(path)
except:
    print('Day folder alrdy exist')
path2 = os.path.join(path, fname)
try:
    os.mkdir(path2)
except:
    print('Files folder alrdy exist')
print(count)
if count == 0:
    with open(path2 + '/' + fname + '.txt', 'w') as fout:
        for elem in urls:
            elem = elem[8:-1]
            elem = elem[4:]
            fout.write(elem)
            fout.write('\n')
else:
    for i in range(count):
        with open(path2 + '/' + fname + str(i) + '.txt', 'w') as fout:
            for elem in list_urls[i]:
                elem = elem[8:]
                try:
                    elem = elem[elem.index]
                    fout.write(elem[elem.index('/'):])
                    fout.write('\n')
                except:
                    print('Error parsin links')

with open(path2 + '/' + fname +  '_LOG.txt','w') as outfile:
    outfile.write('LOG\n')
    outfile.write(all_input)