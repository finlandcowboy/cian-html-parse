name = '/Users/qeepnet/Desktop/id murino.txt'
urls = list()
f = open(name, 'r')
for line in f:
    urls.append(line)
ulrs_new = set(urls)
a = open(name,'w')
for elem in ulrs_new:
    if elem.startswith(' '):
        pass
    else:
        a.write(elem)
