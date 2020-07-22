import random

a, b, c = [], [], []
for i in range(1, 10):
    rand = random.randint(0,10)
    a.append(rand)
    rand = random.randint(0,10)
    b.append(rand)
    rand = random.randint(0,10)
    c.append(rand)

test = {}
test.update({'a': a, 'b': b, 'c': c})
aoa = []
print(list(test.values()))

peresechenie = []
for elem in test.values():
    for wot in elem:
        peresechenie.append(wot)
for i in range(len(test.values())):
    if i != len(test.values()):
        print('be4:', peresechenie)
        list_of_values = list(test.values())
        peresechenie = list(set(peresechenie) & set(list_of_values[i]))
        print('after values:', list_of_values[i])
        print('After:', peresechenie)
