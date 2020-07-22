import random
from collections import Counter
a, b, c = [], [], []
for i in range(1, 10):
    rand = random.randint(0,10)
    a.append(rand)
    rand = random.randint(0,10)
    b.append(rand)
    rand = random.randint(0,10)
    c.append(rand)
a, b, c = list(set(a)), list(set(b)), list(set(c))

test = {}
test.update({'a': a, 'b': b, 'c': c})
aoa = []
print(list(test.values()))

peresechenie = []

list_of_values = list(test.values())
for elem in list_of_values:
    i = 0
    for wot in elem:
            if elem != list_of_values[i]:
                k = 0
                for j in range(len(list_of_values)):
                    if wot in list_of_values[j]:
                        k += 1
                if k == len(list_of_values) or k == len(list_of_values) - 1:
                    peresechenie.append(wot)
    i += 1
peresechenie = list(set(peresechenie))
print(peresechenie)