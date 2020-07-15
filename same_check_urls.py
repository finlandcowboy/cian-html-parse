res = list()
fname = input('ВВЕДИТЕ НАЗВАНИЕ ФАЙЛА ДЛЯ ВЫВОДА: ')
new = input('Введите название файла с новыми URL: ')
new_urls = list()
with open('/Users/qeepnet/Desktop/urls/' + new +'.txt', 'r') as input_file:
    for line in input_file:
        new_urls.append(line)
print('OLD NEW URLS', new_urls)
new_urls = new_urls[new_urls.index('URLS:\n'):-1]
print('NEW URLS', new_urls)
previous = list()
url = input("Введите старые URL: ")
while url != '':
    previous.append(url)
    url = input("Введите старые URL: ")

for elem in new_urls:
    if elem not in previous:
        res.append(elem)
with open('/Users/qeepnet/Desktop/urls/segment checker/' + fname + ' НУ.txt', 'w') as output_file:
    for elem in res:
        output_file.write(elem)
