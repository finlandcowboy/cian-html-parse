import requests
import os, datetime
from bs4 import BeautifulSoup
from googletrans import Translator
Translator = Translator()
all_input = ''
input_list = list()
car = Translator.translate(input('Введите название марки машины: '), src='ru', dest='en')
input_list.append(car.text)
city = Translator.translate(input('Введите город: '), src='ru', dest='en')
path = 'https://' + str(city.text.lower()) + '.drom.ru/' + str(input_list[0]) + '/new'
print(path)
input_list.append(path)
path = path + '/all'
input_list.append(path)
for i in range(8):
    a = path + '/page' + str(i+2)
    input_list.append(a)
c = 0
fname = str(input_list[c])

all_input = all_input + fname + ' '
urls = list()
for c in range(len(input_list) - 1):
    print(input_list)
    print('FFFFFF: ', input_list[c+1])
    url = input_list[c]
    if requests.get(url).status_code == 200:

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